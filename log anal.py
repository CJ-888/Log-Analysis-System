from datetime import datetime

# Class to handle log file reading
class LogReader:
    def __init__(self, filename):  # Enter Filename
        self.filename = filename
        self.logs = []  # Stores log lines as a list

    def readlogs(self):
        "Function to read and store the file line by line in a list"
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.logs = [line.strip() for line in file.readlines()]
                print("Logs Loaded:", self.logs)
        except FileNotFoundError:
            print("Error: Log file not found.")

    def getlogs(self):
        return self.logs


# Class to analyze log data
class LogAnalyzer:
    def __init__(self, logs):  # Fixed __init_
        self.logs = logs
        self.failedattps = {}  # Dictionary to store failed logins per user
        self.logintracker = {}  # Dictionary to track login times per user

    def analyzelogs(self):
        "Function to log and detect user's login attempts"
        for log in self.logs:
            parts = log.split(",")  # Assuming CSV format: "user, status, timestamp"
            if len(parts) == 3:
                user, status, timestamp = parts
                timestamp = timestamp.strip()

                # Track all login attempts (failed or successful)
                if user not in self.logintracker:
                    self.logintracker[user] = []
                self.logintracker[user].append(timestamp)

                # Track failed login attempts
                if status.strip().lower() == "failed":
                    if user in self.failedattps:
                        self.failedattps[user] += 1
                    else:
                        self.failedattps[user] = 1

    def getfailedattempts(self):
        return self.failedattps

    def getlogintimestamps(self):
        return self.logintracker


# Class to generate and display reports
class ReportGenerator:
    def __init__(self, failedattps, logintimes):  # Fixed __init_
        self.failedattps = failedattps
        self.logintimes = logintimes

    def generatereport(self):
        print("\nSecurity Report:")
        if not self.failedattps:
            print("No failed login attempts detected.")
        else:
            for user, attempts in self.failedattps.items():
                print(f"User: {user}, Failed Attempts: {attempts}")

        print("\nLogin Tracker Report:")
        for user, timestamps in self.logintimes.items():
            print(f"User: {user}, Total Logins: {len(timestamps)}")
            for time in timestamps:
                print(f"  - {time}")


# Main function
def main():
    log_reader = LogReader("auth_logs.txt")  # Log file name
    log_reader.readlogs()

    logs = log_reader.getlogs()
    print("Logs Read:", logs)

    log_analyzer = LogAnalyzer(logs)
    log_analyzer.analyzelogs()

    failed_attempts = log_analyzer.getfailedattempts()
    login_timestamps = log_analyzer.getlogintimestamps()

    print("Failed Attempts:", failed_attempts)
    print("Login Timestamps:", login_timestamps)

    report = ReportGenerator(failed_attempts, login_timestamps)
    report.generatereport()


# Run the program
if __name__ == "__main__":  # Fixed condition
    main()
