from sqlalchemy import create_engine
# Example of ETL on porstgresql database using sqalchemy

# Function to extract table to a pandas DataFrame
def extract_table_to_pandas(tablename, db_engine):
    query = "SELECT * FROM {}".format(tablename)
    return pd.read_sql(query, db_engine)

# Connect to the database using the connection URI
connection_uri = "postgresql://user:password@host:port/database" 
db_engine = create_engine(connection_uri)

# Extract the film table into a pandas DataFrame
extract_table_to_pandas("table", db_engine)

# Transform
# Do transformations using pyspark, pandas, etc.

# Load
# Finish the .to_sql() call to write to store.table
table.to_sql("film", db_engine_dwh, schema="store", if_exists="replace")
# Run the query to fetch the data
pd.read_sql("SELECT * FROM store.table", db_engine_dwh)
