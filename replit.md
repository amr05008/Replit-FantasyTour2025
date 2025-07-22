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

## Recent Changes

### Latest Updates (July 22, 2025)
- **URL Sharing Enhancement**: Comprehensive social media optimization for text message sharing
  - Added Open Graph meta tags for rich link previews across all platforms
  - Implemented Twitter Cards for enhanced Twitter/X sharing experience
  - Integrated Schema.org structured data for better search engine understanding
  - Created dynamic social preview image generator using SVG for scalability
  - Added sharing buttons component with Twitter, Facebook, LinkedIn, and copy-link functionality
  - Collapsible sharing section integrated into main app header
  - SEO improvements with meta descriptions, keywords, and theme color specifications
  - Preview images automatically show current leader and stage progress
  - All sharing content dynamically updates based on real-time race data
- **Team Riders Component**: Added dedicated rider roster display as third navigation tab
  - Integrated "Replit_Riders" worksheet (GID: 667768222) as separate data source
  - Created "👥 Team Riders" tab showing all riders organized by team owner
  - Implemented team-colored displays with rider counts and summary statistics
  - Fixed data processing issues with CSV column whitespace handling
  - Each team now shows proper rider listings (Jeremy: 3 riders, Leo: 3 riders, etc.)
- **Layout Reorganization**: Improved component positioning for better user experience
  - Moved "🏆 Current Standings" section directly below header for immediate visibility
  - Repositioned stage progress information below standings table
  - Maintained all existing functionality and dark mode styling
  - Layout now follows: Header → Current Standings → Stage Progress → Analysis tabs

- **Dark Mode Visibility Fixes**: Comprehensive CSS-only styling for all UI elements
  - Fixed refresh button white background inheritance with multiple CSS targeting layers
  - Enhanced chart legend visibility with proper white text on dark backgrounds
  - Corrected Plotly chart axis title styling (fixed titlefont property error)
  - Applied universal text color overrides for consistent dark mode appearance
  - Stage legend and analysis descriptions now properly visible
  - All interactive elements (buttons, tabs, dropdowns) fully readable in dark mode
- **Stage-by-Stage Performance Charts**: Added comprehensive analytical visualization using Plotly
  - Interactive charts with dark theme integration and participant color coding
  - Cumulative Time Progression: Line charts showing total time evolution across stages
  - Individual Stage Performance: Bar charts displaying stage-specific times and winners
  - Gap Evolution Analysis: Tracks time gaps relative to leader over stages
  - Tabbed interface: "Current Standings" and "Stage Analysis" for organized navigation
  - Chart selection dropdown for easy switching between analysis views
  - Responsive design with hover tooltips and mobile optimization
- **Enhanced Data Processing**: Extended data model to capture all stage times for analytical insights
- **Dark Mode Implementation**: Implemented sleek dark-only theme design
  - Removed theme toggle for streamlined single-theme experience
  - Dark theme: #1e1e1e background, #2d2d2d cards, white text
  - All components styled for dark mode: progress bars, metrics, buttons, cards
  - Yellow jersey leader styling optimized for dark theme contrast
  - Improved readability with carefully chosen color contrasts
- **Google Sheets Integration Fixed**: Connected to "Replit Stage Data" worksheet (gid=0)
- **Enhanced Text Readability**: Increased font sizes (22-24px) and improved contrast for participant names
- **Sad Panda Feature**: Added 🐼 emoji for last place participant
- **Stage Progress Visualization**: Added comprehensive progress tracking with:
  - Progress bar showing completion percentage
  - Metrics for completed/remaining stages
  - Visual stage indicators with colored dots
  - Clear legend for stage status
- **Data Source**: Successfully connected to user's Google Sheets with 5 participants (Jeremy, Leo, Charles, Aaron, Nate)
- **Current Status**: App fully functional with real-time data updates, yellow jersey leader styling, complete dark mode visibility, comprehensive stage analysis charts, and enhanced analytical user experience

### Working Features
- Real-time Google Sheets data integration
- Tour de France yellow jersey styling for leader
- Time gap calculations and rankings
- Auto-refresh every 5 minutes
- Mobile-responsive design
- Stage progress tracking
- Sleek dark mode design with optimized contrast
- Theme-consistent UI components and styling
- Interactive stage-by-stage performance charts (Plotly integration)
- Comprehensive analytical dashboard with multiple chart types
- Team riders roster display with dedicated worksheet integration
- Three-tab navigation: Current Standings, Stage Analysis, Team Riders
- Team-colored rider cards with summary statistics

The architecture prioritizes simplicity and rapid deployment while maintaining good performance through strategic caching and efficient data processing.