from contextlib import contextmanager
import time
import sqlite3

@contextmanager
def timer():
    before = time.time()
    yield
    after = time.time()
    print(f"Loop took: {after - before}")
    
    
# 2. Database connection
@contextmanager
def database(filename):
    conn = sqlite3.connect(filename)
    yield conn
    conn.close()
    print(f"Closing the {conn}")

# 3. Temporary file writer
@contextmanager
def temp_file(filename):
    file = open(filename , "w")
    yield file
    file.close()
    print("file closed!")
    
   

# Test all 3:
if __name__ == "__main__":
    # Test timer
    with timer():
        time.sleep(1)
    
    # Test database
    with database('test.db') as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
        print("Table created!")
    
    # Test temp file
    with temp_file('output.txt') as f:
        f.write("Hello from context manager!\n")
        print("file created")