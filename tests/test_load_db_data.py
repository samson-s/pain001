import os
import sqlite3
import pytest
from pain001.db.load_db_data import sanitize_table_name, load_db_data


# Test sanitize_table_name function
def test_sanitize_table_name():
    assert sanitize_table_name("valid_table_name") == "valid_table_name"
    assert sanitize_table_name("invalid table name") == "invalid_table_name"
    assert sanitize_table_name("123invalidname") == "table_123invalidname"
    assert sanitize_table_name("table!@#name") == "table___name"


# Test load_db_data function
def test_load_db_data(tmp_path):
    # Create a temporary SQLite database
    db_file = tmp_path / "test.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create a test table and insert data
    cursor.execute(
        "CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)"
    )
    cursor.execute("INSERT INTO test_table (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Bob')")
    conn.commit()
    conn.close()

    # Test loading data from the table
    data = load_db_data(db_file, "test_table")
    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[1]["name"] == "Bob"

    # Test FileNotFoundError
    with pytest.raises(FileNotFoundError):
        load_db_data("non_existent.db", "test_table")

    # Test sqlite3.OperationalError for non-existent table
    with pytest.raises(sqlite3.OperationalError):
        load_db_data(db_file, "non_existent_table")


# If the script is executed directly, run the tests
if __name__ == "__main__":
    pytest.main()
