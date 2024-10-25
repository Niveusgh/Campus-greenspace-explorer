# CampusGreen: Interactive Green Space Explorer

## Overview
CampusGreen is a mobile-friendly web application designed to help university students and staff discover and learn about green spaces on campus. It provides an interactive map, detailed plant information, and interesting historical facts about the campus environment.

## Features
- **Homepage**: A welcoming entry point to improve user experience.
- **Interactive Campus Map**: Explore green spaces with a touch-friendly interface.
- **Green Space Details**: Learn about different types of green areas (gardens, groves, lawns).
- **Plant Species Information**: Discover native and notable plants in each green space.
- **Historical and Fun Facts**: Engage with interesting stories about plants and spaces.
- **Basic Care Tips**: Access simple plant care instructions (optional feature).
- **Green Space History**: (Potential feature) Explore the history of specific green spaces, including trivia and fun facts.
- **UK Tree Integration**: Access official University of Kentucky tree inventory data
- **Custom Tree Submissions**: Add and track user-identified trees on campus

## Technology Stack
* Backend: Python with Flask
* Frontend: HTML5, CSS3, JavaScript
* Database: 
  - SQLite for user submissions
  - CSV integration for UK tree inventory
* Mapping: Leaflet.js
* Additional Libraries:
  - Flask-SQLAlchemy for database management
  - Pandas for data processing

## Data Sources
The application uses two main data sources:
1. **UK Tree Inventory**: Official tree data from the University of Kentucky's Urban Forest Initiative
2. **User Submissions**: Custom tree identifications submitted by users

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/niveusgh/campus-greenspace-explorer.git
   cd campus-greenspace-explorer
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ``bash
   # After installing requirements
   flask db init      # Initialize the database
   flask db migrate   # Generate migration
   flask db upgrade   # Apply migration
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open a web browser and navigate to `http://localhost:5000`

## Usage
- Open the app on your mobile device or desktop browser.
- Explore the interactive map to find green spaces on campus.
- Tap on map markers to view information about each space.
- Browse plant species information and historical facts.
- Access care tips for plants by tapping the designated icon.
- If available, explore the history of specific green spaces by tapping the designated icon.

## Contributing
We welcome contributions to CampusGreen! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- University of Kentucky for providing data on campus green spaces.
- Urban Forest Initiative 

## Contact
Team 0x22 
- Charles.Key@uky.edu
- Bowen.Fan@uky.edu
- Jonathan.Dean@uky.edu
- Thea.Francis@uky.edu

Project Link: [https://github.com/Niveusgh/Campus-greenspace-explorer](https://github.com/Niveusgh/Campus-greenspace-explorer)


