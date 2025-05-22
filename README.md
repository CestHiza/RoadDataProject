# Road Data Processing and Visualization Project

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline for synthetic road data. It includes scripts to generate road data, clean it, load it into a SQL Server database, validate the data using SQL, generate basic metadata, and visualize the roads in QGIS.

## Project Structure


RoadDataProject/
├── .gitignore          # Specifies intentionally untracked files that Git should ignore
├── generate_metadata.py # Python script to generate roads_metadata.xml
├── generate_roads.py   # Python script to generate synthetic roads.csv
├── process_roads.py    # Python script to clean roads.csv and load data into SQL Server
├── roads.csv           # Generated synthetic road data (created by generate_roads.py)
├── roads_metadata.xml  # Generated metadata file (created by generate_metadata.py)
├── validate_roads.sql  # SQL script for data validation checks
└── venv/               # Python virtual environment (should be in .gitignore)


## Features

* **Data Generation:** Creates a CSV file (`roads.csv`) with synthetic road information including ID, name, length, condition, and basic WKT geometry.
* **Data Cleaning & Loading:** Cleans the generated data (handles missing values, standardizes formats) and loads it into a `Roads` table in a SQL Server database (`RoadsDB`).
* **SQL Validation:** Provides SQL queries to perform integrity checks on the loaded data.
* **Metadata Generation:** Creates a basic XML metadata file (`roads_metadata.xml`).
* **QGIS Visualization:** The `roads.csv` file can be imported into QGIS to visualize the road geometries.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python (3.6+)
* Visual Studio Code (or any other code editor)
* SQL Server (Developer Edition or Express Edition recommended)
* SQL Server Management Studio (SSMS)
* QGIS
* Git

## Setup and Installation

1.  **Clone the repository (if applicable, otherwise follow project setup):**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install Python libraries:**
    ```bash
    pip install pandas pyodbc
    ```

4.  **Set up SQL Server:**
    * Ensure SQL Server is running.
    * Using SSMS, create a new database named `RoadsDB`.

## Running the Project

1.  **Generate Synthetic Road Data:**
    ```bash
    python generate_roads.py
    ```
    This will create `roads.csv`.

2.  **Clean Data and Load into SQL Server:**
    * **Important:** Before running, open `process_roads.py` and verify the database connection details:
        * `DB_DRIVER`: (e.g., `"{ODBC Driver 17 for SQL Server}"`)
        * `DB_SERVER`: (e.g., `"localhost"` or `"localhost\\SQLEXPRESS"`)
        * `DB_NAME`: Should be `"RoadsDB"`
    * Run the script:
        ```bash
        python process_roads.py
        ```

3.  **Validate Data in SQL Server:**
    * Open `validate_roads.sql` in SSMS (ensure you are connected to `RoadsDB`).
    * Execute the script to perform data integrity checks.

4.  **Generate Metadata:**
    ```bash
    python generate_metadata.py
    ```
    This will create `roads_metadata.xml`.

5.  **Visualize in QGIS:**
    * Open QGIS.
    * Go to `Layer > Add Layer > Add Delimited Text Layer...`.
    * Browse to and select `roads.csv`.
    * Under "Geometry Definition", choose "Well known text (WKT) geometry", select the `geometry` field, and ensure the geometry type is "LineString".
    * Click "Add".

## Author

* Hiza Mvuendy (Update with your name/GitHub profile if desired)

## License

This project is open source and available under the [MIT License](LICENSE.md). (Optional: If you want to add a license, create a `LICENSE.md` file with the MIT license text, or choose another license).
