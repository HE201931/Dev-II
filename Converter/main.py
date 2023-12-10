import sqlite3
import csv
import sys


def print_success(converter):
    if converter == 0:
        print("Conversion successfully done from sqlite to csv !")
    if converter == 1:
        print("Conversion successfully done from csv to sqlite !")


def print_error(converter, error):
    if converter == 0:
        print("An error occurred while converting file from sqlite to csv : ", error)
    if converter == 1:
        print("An error occurred while converting file from csv to sqlite : ", error)


def convert_sqlite_to_csv(database_file, output_csv):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # Fetch all table names in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Loop through each table and export data to CSV
        for table in tables:
            table_name = table[0]

            # Fetch all rows from the table
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            # Fetch column names
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = [column[1] for column in cursor.fetchall()]

            # Write to CSV file
            with open(f"{output_csv}_{table_name}.csv", "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)

                # Write header
                csv_writer.writerow(columns)

                # Write data
                csv_writer.writerows(rows)

        # Close connections
        cursor.close()
        conn.close()
        print_success(0)
    except Exception as error:
        print_error(0, error)


def convert_csv_to_sqlite(csv_file, database_file, table_name):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # Create table
        with open(csv_file, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            columns = ', '.join(header)
            placeholders = ', '.join('?' for _ in header)

            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
            cursor.execute(create_table_query)

            # Insert data into table
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
            cursor.executemany(insert_query, csv_reader)

        # Commit and close connections
        conn.commit()
        cursor.close()
        conn.close()
        print_success(1)
    except Exception as error:
        print_error(1, error)


def print_help():
    print("Invalid arguments")
    print("Available : ")
    print("-tocsv input_file.db output_file.csv")
    print("-tosql input_file.csv output_file.db table_name")
    exit(0)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_help()

    print(sys.argv[1])

    if sys.argv[1] == "-tocsv":
        convert_sqlite_to_csv(sys.argv[2], sys.argv[3])
        exit(0)
    elif sys.argv[1] == "-tosql":
        convert_csv_to_sqlite(sys.argv[2], sys.argv[3], sys.argv[4])
        exit(0)
    else:
        print_help()