# Fantasy Tour de France 2025

A Streamlit web application for tracking Fantasy Tour de France 2025 results with real-time data from Google Sheets.

## Features

- Real-time participant rankings from Google Sheets data
- Tour de France yellow jersey styling for the leader
- Automatic time gap calculations
- Clean, responsive interface optimized for readability
- Auto-refresh functionality every 5 minutes

## Live Demo

The app displays current standings for 5 participants:
- Aaron (Current Leader - Yellow Jersey)
- Jeremy
- Leo
- Charles
- Nate

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install streamlit pandas requests
   ```
3. Run the application:
   ```bash
   streamlit run app.py --server.port 5000
   ```

## Data Source

The app connects to a Google Sheets document containing:
- Participant names and stage times
- Real-time updates as the Tour de France progresses
- Automatic calculation of time gaps and rankings

## Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Data Source**: Google Sheets CSV export
- **Styling**: Custom CSS with Tour de France theme

## Configuration

The app includes proper server configuration in `.streamlit/config.toml` for deployment compatibility.

## Deployment

This app is designed to work on various platforms including:
- Streamlit Cloud
- Replit
- Heroku
- Any platform supporting Python web applications

## License

MIT License