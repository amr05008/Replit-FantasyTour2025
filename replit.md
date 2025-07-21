# Fantasy Tour de France 2025

## Overview

This is a Streamlit-based web application for tracking and displaying Fantasy Tour de France 2025 results. The application fetches data from Google Sheets and presents it in a user-friendly dashboard format with real-time updates and caching for performance optimization.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a simple single-file architecture built with Streamlit for rapid prototyping and deployment:

- **Frontend**: Streamlit web framework providing interactive UI components
- **Data Source**: Google Sheets CSV export URL for real-time data fetching
- **Caching**: Streamlit's built-in caching mechanism with TTL (Time-To-Live) configuration
- **Deployment**: Designed for easy deployment on Streamlit Cloud or similar platforms

## Key Components

### 1. Data Management
- **Google Sheets Integration**: Uses direct CSV export URL from Google Sheets for data retrieval
- **Caching Layer**: Implements 5-minute TTL caching to reduce API calls and improve performance
- **Time Conversion Utilities**: Custom functions for converting between time formats (H:MM:SS to seconds and back)

### 2. Time Calculation Engine
- **Time-to-Seconds Converter**: Handles parsing of race time strings into comparable numeric values
- **Gap Calculation**: Computes time differences between participants and race leaders
- **Error Handling**: Robust parsing that handles edge cases like empty values or malformed time strings

### 3. User Interface
- **Wide Layout Configuration**: Optimized for displaying tabular data across the full screen width
- **Custom Page Branding**: Tour de France themed with cycling emoji and descriptive title
- **Real-time Updates**: Automatic data refresh capabilities with caching optimization

## Data Flow

1. **Data Retrieval**: Application fetches CSV data from Google Sheets export URL
2. **Data Processing**: Raw time strings are converted to seconds for mathematical operations
3. **Gap Calculation**: Time differences are calculated relative to race leaders
4. **Display Formatting**: Results are converted back to human-readable time format
5. **Caching**: Processed data is cached for 5 minutes to improve performance

## External Dependencies

### Core Frameworks
- **Streamlit**: Web application framework and UI components
- **Pandas**: Data manipulation and analysis
- **Requests**: HTTP client for fetching data from Google Sheets

### Data Source
- **Google Sheets**: Primary data storage and management system
- **CSV Export URL**: Direct access to sheet data without authentication requirements

## Deployment Strategy

The application is designed for simple deployment on cloud platforms:

### Recommended Platforms
- **Streamlit Cloud**: Native deployment with automatic GitHub integration
- **Heroku**: Container-based deployment with Procfile configuration
- **Replit**: Direct Python environment execution

### Configuration Requirements
- Python environment with required packages (streamlit, pandas, requests)
- Internet access for Google Sheets data fetching
- No database setup required (uses Google Sheets as data backend)

### Performance Considerations
- Implements caching to minimize external API calls
- Uses efficient time conversion algorithms for large datasets
- Wide layout optimized for data-heavy presentations

The architecture prioritizes simplicity and rapid deployment while maintaining good performance through strategic caching and efficient data processing.