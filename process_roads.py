# process_roads.py
import pandas as pd
import pyodbc

# --- Configuration ---
# Adjust these details if your SQL Server setup is different
DB_DRIVER = "{ODBC Driver 17 for SQL Server}" # Or "{SQL Server}", or other installed driver
DB_SERVER = "LAPTOP-BGAFPDGE\SQLEXPRESS"  # Or "localhost\\SQLEXPRESS" if using a named instance
DB_NAME = "RoadsDB"
TABLE_NAME = "Roads"

# Connection string
conn_str = (
    f"Driver={DB_DRIVER};"
    f"Server={DB_SERVER};"
    f"Database={DB_NAME};"
    f"Trusted_Connection=yes;" # Uses Windows Authentication
)

def clean_data(csv_filepath="roads.csv"):
    """Reads and cleans data from the CSV file."""
    print(f"Reading data from {csv_filepath}...")
    df = pd.read_csv(csv_filepath)
    
    # Remove rows with any missing values
    df_before_dropna = len(df)
    df = df.dropna()
    df_after_dropna = len(df)
    print(f"Removed {df_before_dropna - df_after_dropna} rows with missing values.")
    
    # Standardize decimals for length_km
    df["length_km"] = df["length_km"].round(2)
    print("Standardized 'length_km' to 2 decimal places.")
    
    return df

def create_table_if_not_exists(cursor):
    """Creates the Roads table if it doesn't already exist."""
    try:
        # Check if table exists
        cursor.execute(f"SELECT OBJECT_ID(N'{TABLE_NAME}', N'U')")
        table_exists = cursor.fetchone()[0] is not None

        if not table_exists:
            print(f"Table '{TABLE_NAME}' does not exist. Creating table...")
            cursor.execute(f"""
            CREATE TABLE {TABLE_NAME} (
                road_id VARCHAR(10) PRIMARY KEY,
                name VARCHAR(50),
                length_km DECIMAL(10,2),
                condition VARCHAR(10),
                geometry VARCHAR(MAX) -- Using VARCHAR(MAX) for potentially longer WKT strings
            )
            """)
            print(f"Table '{TABLE_NAME}' created successfully.")
        else:
            print(f"Table '{TABLE_NAME}' already exists. Truncating table before loading new data...")
            cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}") # Clear existing data for a fresh load
            print(f"Table '{TABLE_NAME}' truncated.")

    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error related to table creation/check: {sqlstate}")
        raise

def load_data_to_sql(df, conn):
    """Loads the DataFrame into the SQL Server table."""
    print(f"Attempting to load data into SQL Server table '{TABLE_NAME}'...")
    with conn.cursor() as cursor:
        create_table_if_not_exists(cursor)
        
        print(f"Inserting {len(df)} rows into '{TABLE_NAME}'...")
        insert_count = 0
        for _, row in df.iterrows():
            try:
                cursor.execute(f"""
                INSERT INTO {TABLE_NAME} (road_id, name, length_km, condition, geometry)
                VALUES (?, ?, ?, ?, ?)
                """, row["road_id"], row["name"], row["length_km"], row["condition"], row["geometry"])
                insert_count += 1
            except pyodbc.Error as ex:
                sqlstate = ex.args[0]
                print(f"Error inserting row: {row['road_id']}. SQLSTATE: {sqlstate}")
                # Optionally, decide whether to continue or stop on error
                # raise # Uncomment to stop on first error
        
        conn.commit()
        print(f"Successfully inserted {insert_count} rows into '{TABLE_NAME}'.")

def main():
    df_cleaned = clean_data()
    
    if df_cleaned.empty:
        print("No data to load after cleaning. Exiting.")
        return

    try:
        print(f"Connecting to SQL Server: Server='{DB_SERVER}', Database='{DB_NAME}'...")
        conn = pyodbc.connect(conn_str)
        print("Successfully connected to SQL Server.")
        
        load_data_to_sql(df_cleaned, conn)
        
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Database connection or operation error: {sqlstate}")
        print("Please ensure SQL Server is running, the database '{DB_NAME}' exists,")
        print("and the ODBC driver '{DB_DRIVER}' is correctly specified and installed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()