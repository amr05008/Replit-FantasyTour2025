# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Fantasy Tour de France 2025 is a Streamlit web application that displays real-time fantasy cycling competition results by fetching data from Google Sheets. The app features a Tour de France themed interface with yellow jersey leader styling, stage-by-stage analysis charts, and comprehensive progress tracking.

## Running the Application

### Start Development Server
```bash
streamlit run app.py --server.port 5000
```

The app will be available at `http://localhost:5000`

### Auto-refresh Feature
The app automatically refreshes data every 5 minutes using Streamlit's caching mechanism with TTL (Time-To-Live).

## Data Architecture

### Google Sheets Integration

The app pulls data from two worksheets in the same Google Sheets document:

1. **Main Stage Data** (gid=0): Contains cumulative stage times for each participant
   - Stored in `SHEET_URL` constant in app.py:100
   - Format: Participant names in Column A, stage times in columns B through V (21 stages)
   - Time format: `H:MM:SS` (e.g., `0:08:19`, `1:23:45`)
   - Participant names must exactly match: `Jeremy`, `Leo`, `Charles`, `Aaron`, `Nate`
   - Data rows start around row 10 (earlier rows contain headers)

2. **Team Riders Data** (gid=667768222): Contains rider roster assignments
   - Stored in `RIDERS_SHEET_URL` constant in app.py:100
   - Shows which professional riders each participant drafted for their fantasy team
   - Accessed via dedicated "👥 Team Riders" tab

See `GOOGLE_SHEETS_FORMAT.md` for detailed data structure requirements.

### Time Conversion System

The app uses a two-way conversion system for time calculations:

- `time_to_seconds()` (app.py:102): Converts `H:MM:SS` strings to integer seconds for mathematical operations
- `seconds_to_time_str()` (app.py:115): Converts seconds back to human-readable format
- `calculate_time_gap()` (app.py:124): Computes time differences relative to the leader

This allows for accurate gap calculations and proper sorting/ranking.

## Competition Configuration

The app has a configuration-based system for toggling between active and completed competition states:

```python
COMPETITION_CONFIG = {
    "is_complete": True,          # Toggle competition completion status
    "winner_name": "Aaron",        # Name of winner (shown when complete)
    "competition_name": "Tour de France 2025",
    "total_stages": 21,
    "completion_date": "July 27, 2025",
    "show_celebration": True       # Toggle winner celebration banner
}
```

Located at app.py:89. This allows easy reuse for future competitions (e.g., Tour de France 2026) by simply updating these values.

## UI Components and Features

### Three-Tab Navigation System

1. **🏆 Current Standings**: Main leaderboard with yellow jersey styling for the leader
2. **📊 Stage Analysis**: Interactive Plotly charts showing:
   - Cumulative Time Progression (line chart)
   - Individual Stage Performance (bar chart)
   - Gap Evolution Analysis (line chart tracking gaps over time)
3. **👥 Team Riders**: Shows each participant's drafted professional riders with team-colored cards

### Dark Mode Theme

The app uses a dark-only theme (no toggle):
- Background: `#1e1e1e`
- Cards: `#2d2d2d`
- Text: White with high contrast
- Leader styling: Yellow jersey gold (`#FFD700`) optimized for dark backgrounds

All CSS is embedded in the Streamlit app using `st.markdown()` with `unsafe_allow_html=True`.

### Winner Celebration System

When `COMPETITION_CONFIG["is_complete"] = True`:
- `create_winner_banner()` function (app.py:131) displays an animated gold gradient banner
- Leader card shows "🏆 CHAMPION" instead of "LEADER"
- Page title shows "COMPLETE ✅" status
- Confetti animation and pulsing effects

### Responsive Design

The app includes comprehensive mobile responsiveness:
- CSS media queries for tablets (≤768px) and phones (≤480px)
- Touch-friendly 44px minimum touch targets
- Adaptive column layouts that stack vertically on mobile
- Disabled hover effects on touch devices
- Optimized typography and chart scaling for small screens

### Social Media Sharing

Open Graph, Twitter Cards, and Schema.org metadata are embedded in the HTML head (app.py:18-70) for rich link previews when sharing the app URL via text message or social media.

## Key Functions and Data Flow

1. **Data Retrieval**: Fetch CSV from Google Sheets using `requests` library with TTL caching
2. **Data Processing**: Parse participant rows (searching for exact name matches around row 10+)
3. **Time Conversion**: Convert time strings to seconds for calculations
4. **Gap Calculation**: Calculate time differences relative to leader
5. **Display Formatting**: Convert back to human-readable format for UI display
6. **Caching**: All processed data cached for 5 minutes via Streamlit decorators

## Dependencies

Core packages (listed in `dependencies.txt`):
- `streamlit`: Web framework and UI components
- `pandas`: Data manipulation and CSV parsing
- `requests`: HTTP client for Google Sheets data fetching
- `plotly`: Interactive charting library for stage analysis

Install with:
```bash
pip install streamlit pandas requests plotly
```

## Deployment Platforms

The app is designed for easy deployment on:
- **Streamlit Cloud**: Recommended, native integration
- **Replit**: Direct Python execution (see `replit.md` for deployment history)
- **Heroku**: Container-based deployment

No database required - Google Sheets serves as the data backend.

## File Structure

- `app.py`: Main application file (single-file architecture)
- `config.toml`: Streamlit server configuration
- `dependencies.txt`: Python package requirements
- `README.md`: User-facing documentation
- `GOOGLE_SHEETS_FORMAT.md`: Detailed Google Sheets data format specification
- `BACKUP_STEPS.md`: Git backup instructions for Replit
- `replit.md`: Comprehensive development history and system architecture notes

## Important Notes

- The app uses a single-file architecture for simplicity and rapid deployment
- All data is public (Google Sheets link sharing must be set to "Anyone with the link can view")
- No authentication or database setup required
- The competition tracks 5 participants across 21 stages of the Tour de France
- User prefers simple, everyday language (noted in replit.md:9)
