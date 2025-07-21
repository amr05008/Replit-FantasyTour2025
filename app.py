import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Fantasy Tour de France 2025",
    page_icon="🚴",
    layout="wide"
)

# Google Sheets CSV export URL - "Replit Stage Data" worksheet
SHEET_URL = "https://docs.google.com/spreadsheets/d/1_dYs_80Xdi39_-vtZYxt6l4Mj_0jFuHSf4p79zcBI4M/export?format=csv&gid=0"

def time_to_seconds(time_str):
    """Convert time string (H:MM:SS) to seconds for comparison"""
    try:
        if pd.isna(time_str) or time_str == "0:00:00" or time_str == "":
            return 0
        parts = str(time_str).split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        return hours * 3600 + minutes * 60 + seconds
    except:
        return 0

def seconds_to_time_str(seconds):
    """Convert seconds back to time string format"""
    if seconds == 0:
        return "0:00:00"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}:{minutes:02d}:{secs:02d}"

def calculate_time_gap(leader_time, participant_time):
    """Calculate time gap between leader and participant"""
    gap_seconds = participant_time - leader_time
    if gap_seconds == 0:
        return "Leader"
    return f"+{seconds_to_time_str(gap_seconds)}"

@st.cache_data(ttl=300)  # Cache for 5 minutes
def fetch_data():
    """Fetch data from Google Sheets CSV export"""
    try:
        # Use session to handle redirects properly
        session = requests.Session()
        response = session.get(SHEET_URL, allow_redirects=True)
        response.raise_for_status()
        
        # Read CSV data
        from io import StringIO
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)
        
        return df
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None

def process_data(df):
    """Process the raw CSV data to get current standings"""
    if df is None:
        return None
    
    # Find the participant rows
    participants = ['Jeremy', 'Leo', 'Charles', 'Aaron', 'Nate']
    participant_data = {}
    
    # Find the latest stage with data (non-zero times)
    latest_stage = 1
    
    try:
        # Look for participant rows in the dataframe
        for idx, row in df.iterrows():
            participant_name = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ""
            
            if participant_name in participants:
                # Find the latest stage with actual time data
                stage_times = []
                for col_idx in range(1, min(22, len(row))):  # Stages 1-21
                    if col_idx < len(row):
                        time_val = row.iloc[col_idx]
                        if pd.notna(time_val) and str(time_val).strip() != "0:00:00" and str(time_val).strip() != "":
                            stage_times.append((col_idx, time_val))
                            latest_stage = max(latest_stage, col_idx)
                
                if stage_times:
                    # Get the most recent time
                    latest_time = stage_times[-1][1]
                    participant_data[participant_name] = {
                        'time': latest_time,
                        'time_seconds': time_to_seconds(latest_time),
                        'stage': latest_stage
                    }
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        return None
    
    if not participant_data:
        st.error("No participant data found in the spreadsheet")
        return None
    
    # Sort by time (ascending - lowest time wins)
    sorted_participants = sorted(
        participant_data.items(), 
        key=lambda x: x[1]['time_seconds']
    )
    
    # Calculate gaps from leader
    leader_time = sorted_participants[0][1]['time_seconds']
    for name, data in sorted_participants:
        data['gap'] = calculate_time_gap(leader_time, data['time_seconds'])
        data['position'] = sorted_participants.index((name, data)) + 1
    
    return sorted_participants, latest_stage

def main():
    # Title and header
    st.title("🚴 Fantasy Tour de France 2025")
    st.markdown("### General Classification Standings")
    
    # Add refresh button
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🔄 Refresh", help="Refresh data from Google Sheets"):
            st.cache_data.clear()
            st.rerun()
    
    # Fetch and process data
    with st.spinner("Fetching latest standings..."):
        df = fetch_data()
        processed_data = process_data(df)
    
    if processed_data is None:
        st.error("Unable to load standings data. Please check the Google Sheets connection.")
        return
    
    sorted_participants, latest_stage = processed_data
    
    # Display current stage info with progress visualization
    st.info(f"📊 Current standings after Stage {latest_stage}")
    
    # Stage Progress Visualization
    total_stages = 21
    progress_percentage = (latest_stage / total_stages) * 100
    remaining_stages = total_stages - latest_stage
    
    # Create progress bar section
    st.markdown("### 🏁 Tour Progress")
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.progress(progress_percentage / 100)
        st.markdown(f"**Stage {latest_stage} of {total_stages}** ({progress_percentage:.1f}% complete)")
    
    with col2:
        st.metric("Stages Completed", latest_stage, delta=None)
    
    with col3:
        st.metric("Stages Remaining", remaining_stages, delta=None)
    
    # Visual stage indicator
    st.markdown("#### Stage Status")
    stage_indicators = ""
    for stage in range(1, total_stages + 1):
        if stage <= latest_stage:
            stage_indicators += "🟢 "  # Completed stages
        elif stage == latest_stage + 1:
            stage_indicators += "🔴 "  # Next stage
        else:
            stage_indicators += "⚪ "  # Future stages
    
    st.markdown(f"**Stages 1-21:** {stage_indicators}")
    st.markdown("🟢 Completed | 🔴 Next | ⚪ Future")
    
    # Create standings table
    st.markdown("---")
    st.markdown("### 🏆 Current Standings")
    
    # Custom CSS for Tour de France styling
    st.markdown("""
    <style>
    .leader-row {
        background-color: #FFD700 !important;
        font-weight: bold;
    }
    .standings-table {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display standings
    for i, (participant, data) in enumerate(sorted_participants):
        position = data['position']
        time_str = data['time']
        gap = data['gap']
        
        # Create columns for the display
        pos_col, name_col, time_col, gap_col = st.columns([1, 3, 2, 2])
        
        # Apply yellow background for leader
        if position == 1:
            container = st.container()
            with container:
                st.markdown(f"""
                <div style="background-color: #FFD700; padding: 15px; border-radius: 8px; margin: 8px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 24px; font-weight: bold; color: #000000;">🥇 {position}. {participant}</span>
                        <span style="font-size: 20px; font-weight: bold; color: #000000;">{time_str}</span>
                        <span style="font-size: 18px; color: #B8860B; font-weight: bold;">👑 LEADER</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Regular participant display
            total_participants = len(sorted_participants)
            if position == total_participants:
                # Last place gets sad panda
                medal = f"{position}. 🐼"
            elif position == 2:
                medal = "🥈"
            elif position == 3:
                medal = "🥉"
            else:
                medal = f"{position}."
            
            st.markdown(f"""
            <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; margin: 8px 0; border: 2px solid #e9ecef; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 22px; font-weight: bold; color: #212529;">{medal} {participant}</span>
                    <span style="font-size: 18px; font-weight: 600; color: #495057;">{time_str}</span>
                    <span style="font-size: 16px; color: #dc3545; font-weight: 600;">{gap}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Additional information
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_participants = len(sorted_participants)
        st.metric("Total Participants", total_participants)
    
    with col2:
        leader_name = sorted_participants[0][0]
        st.metric("Current Leader", leader_name)
    
    with col3:
        if len(sorted_participants) > 1:
            gap_to_second = sorted_participants[1][1]['gap']
            st.metric("Gap to 2nd Place", gap_to_second)
        else:
            st.metric("Gap to 2nd Place", "N/A")
    
    # Footer
    st.markdown("---")
    st.markdown(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Data refreshes every 5 minutes*")
    st.markdown("*🟡 Yellow highlight indicates the current General Classification leader*")

if __name__ == "__main__":
    main()
