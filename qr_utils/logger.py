
import csv
from datetime import datetime

def log_qr_data(data, path="saved_logs/qr_scans.csv"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([now, data])
