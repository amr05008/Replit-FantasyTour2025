# Fantasy Tour de France 2025

A Streamlit web application for tracking Fantasy Tour de France 2025 results with real-time data from Google Sheets.

## Features

- Real-time participant rankings from Google Sheets data
- Tour de France yellow jersey styling for the leader
- Interactive stage-by-stage performance charts
- Team roster displays with professional riders
- Automatic time gap calculations
- Clean, responsive interface optimized for mobile and desktop
- Auto-refresh functionality every 5 minutes
- Winner celebration mode for completed competitions

## Live Application

🌐 **Deployed on Streamlit Cloud** - Visit the live app to see current standings and analysis

The app displays current standings for 5 participants:
- Aaron (🏆 Champion - Tour de France 2025)
- Jeremy
- Leo
- Charles
- Nate

## Local Development

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/amr05008/Replit-FantasyTour2025.git
   cd Replit-FantasyTour2025
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser to `http://localhost:8501`

## Data Source

The app connects to a Google Sheets document containing:
- Participant names and cumulative stage times (21 stages)
- Team rider rosters for each participant
- Real-time updates as the competition progresses
- Automatic calculation of time gaps and rankings

See [GOOGLE_SHEETS_FORMAT.md](GOOGLE_SHEETS_FORMAT.md) for detailed data structure requirements.

## Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Charts**: Plotly
- **Data Fetching**: Requests
- **Data Source**: Google Sheets CSV export
- **Styling**: Custom CSS with Tour de France theme
- **Deployment**: Streamlit Cloud

## Deployment

### Streamlit Cloud (Current Host)

This app is deployed on **Streamlit Cloud** with automatic deployments from GitHub:

1. Push changes to the `main` branch
2. Streamlit Cloud automatically redeploys
3. Changes are live in ~2 minutes

**Requirements:**
- `requirements.txt` with all dependencies
- `.streamlit/config.toml` for server configuration
- `app.py` as the main application file

See [STREAMLIT_MIGRATION.md](STREAMLIT_MIGRATION.md) for complete migration documentation.

### Alternative Platforms

The app can also be deployed on:
- **Railway** - Modern hosting with GitHub integration
- **Render** - Free tier with auto-deploys
- **Google Cloud Run** - Containerized deployment
- **Heroku** - Traditional PaaS hosting

## Project Documentation

- [CLAUDE.md](CLAUDE.md) - Project overview and architecture
- [STREAMLIT_MIGRATION.md](STREAMLIT_MIGRATION.md) - Deployment migration guide
- [GOOGLE_SHEETS_FORMAT.md](GOOGLE_SHEETS_FORMAT.md) - Data format specifications
- [replit.md](replit.md) - Historical development notes

## License

MIT License