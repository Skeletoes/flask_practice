# BMW Motorrad Catalog Application

## About the Project

BMW Motorrad Catalog is a desktop application that allows you to browse and explore a comprehensive catalog of BMW motorcycles. The application provides detailed information about various motorcycle models, including specifications, engine details, and pricing information.

### Features
- **Browse Motorcycles**: View all available BMW motorcycle models on the home page
- **Detailed Views**: Click on any motorcycle to see detailed specifications and information
- **Model Filtering**: Explore specific motorcycle models filtered by model type
- **Responsive Design**: Clean and intuitive user interface built with HTML, CSS, and Flask
- **Lightweight**: Desktop application with an embedded web server

---

## Requirements

### Python Requirements
- Python 3.7+
- Flask
- Flask-WebGUI
- SQLite3 (included with Python)

### System Requirements
- Windows, macOS, or Linux
- At least 100MB free disk space
- 512MB RAM minimum

---

## Installation

### Prerequisites
Ensure you have Python 3.7+ installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Option 1: From Source Code (Development)

1. **Clone or download the project** to your local machine
   ```bash
   cd flask_practice
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install flask flaskwebgui
   ```

5. **Ensure the database file exists**:
   - The `database.db` file should be in the same directory as `main.py`
   - If missing, you'll need to populate it with BMW motorcycle data

6. **Run the application**:
   ```bash
   python main.py
   ```

### Option 2: Using the Bundled Executable

A pre-built Windows executable is available in the `dist/` folder:
1. Navigate to the `dist/` folder
2. Double-click `BMW-MOTORRAD.exe` to launch the application
3. No Python installation or dependencies needed

---

## How to Use

1. **Start the Application**
   - Run `python main.py` (from source) or double-click `BMW-MOTORRAD.exe` (executable)
   - The application window will open on your desktop

2. **Browse Motorcycles**
   - The home page displays a grid of all available BMW motorcycle models
   - Each card shows the motorcycle name and image

3. **View Details**
   - Click on any motorcycle card to view detailed specifications
   - Details include: Model Name, Year, Engine Type, Displacement, Horsepower, Price, and Description

4. **Explore Models**
   - Use the navigation to explore different motorcycle models
   - Models are organized by type

---

## Project Structure

```
flask_practice/
├── main.py                      # Main application file
├── database.db                  # SQLite database with motorcycle data
├── README.md                    # This file
├── templates/                   # HTML templates
│   ├── layout.html             # Base template with styling
│   ├── home.html               # Home page listing all bikes
│   ├── bike.html               # Individual bike details page
│   └── specific-model.html     # Model-specific view page
├── static/                      # Static files
│   ├── style.css               # CSS styling
│   └── images/                 # Image assets and icons
├── dist/                        # Pre-built executables (Windows)
│   └── BMW-MOTORRAD.exe        # Windows executable
└── build/                       # PyInstaller build artifacts
```

---

## Database Schema

The application uses a SQLite database with a `Motorbikes` table containing the following fields:

| Column | Type | Description |
|--------|------|-------------|
| ModelTypeID | INTEGER | Unique model type identifier |
| ModelName | TEXT | Name of the motorcycle model |
| Description | TEXT | Detailed description |
| Year | INTEGER | Model year |
| EngineType | TEXT | Type of engine (e.g., "Twin", "Inline-4") |
| Displacement | INTEGER | Engine displacement in cc |
| Horsepower | INTEGER | Engine horsepower |
| BasePrice | DECIMAL | Base price of the motorcycle |
| ImageURL | TEXT | URL or path to the motorcycle image |

---

## Building a Windows Executable

If you want to create your own Windows executable:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --windowed --onefile --add-data "templates;templates" --add-data "static;static" --add-data "database.db;." --name BMW-MOTORRAD --icon "static/images/BMW-Logo.ico" main.py
   ```

3. The executable will be generated in the `dist/` folder

---

## Troubleshooting

### "Database file not found" error
- Ensure `database.db` is in the same directory as `main.py`
- The database must contain motorcycle data in the `Motorbikes` table

### Application won't start
- Make sure Flask and Flask-WebGUI are installed: `pip install flask flaskwebgui`
- Check that port 8000 is not already in use

### Styling issues
- Ensure the `static/style.css` file is present in the project directory
- The application looks for static files in the `static/` folder

---

## Technologies Used

- **Flask**: Web framework for building the application
- **Flask-WebGUI**: Desktop application wrapper
- **SQLite3**: Lightweight database for storing motorcycle data
- **Python**: Backend programming language
- **HTML/CSS**: Frontend interface
- **PyInstaller**: For creating standalone executables

---

## License

This project is part of a Flask learning practice repository.

---

## Contact & Support

For issues or questions related to this project, please refer to the source code repository or contact the project maintainer.
