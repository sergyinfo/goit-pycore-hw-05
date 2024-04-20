"""
Task 3: A Python script that reads a log file and displays the count of logs by level.
"""
import sys

def parse_log_line(line: str) -> dict:
    """
    Parse a single log line and return its components as a dictionary.

    :param line: str
    :return: dict
    """
    parts = line.split(maxsplit=3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str):
    """
    Load log entries from a file and parse each line into a dictionary.

    :param file_path: str
    :return: list
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # Ensure the line is not just whitespace
                    yield parse_log_line(line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Unicode decoding error in file '{file_path}'. Ensure the file is in UTF-8 format or specify the correct encoding.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs to include only those of a specific level.

    :param logs: list
    :param level: str
    :return: list
    """
    return (log for log in logs if log['level'].upper() == level.upper())

def count_logs_by_level(logs: list) -> dict:
    """
    Count the number of logs for each level.

    :param logs: list
    :return: dict
    """
    count = {}
    for log in logs:
        level = log['level']
        if level in count:
            count[level] += 1
        else:
            count[level] = 1
    return count

def display_log_counts(counts: dict):
    """
    Display the counts of logs by level in a formatted table.

    :param counts: dict
    """
    print("Log Level | Count")
    print("-----------------")
    for level, count in counts.items():
        print(f"{level:<10} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <path_to_log_file> [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) > 2:
        log_level = sys.argv[2]
        logs = load_logs(log_file_path)  # Reload logs for filtering since logs is a generator
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nDetails of logs for level '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
