# Real-Time QR Code Scanner

This project is a modular, real-time QR code scanner built with **Python** and **OpenCV**. It captures webcam input, detects QR codes, logs the decoded data with timestamps, and automatically opens URLs in the browser. The code is organized for easy maintenance and extension — ideal for hobby projects, automation tools, or integrations with larger systems.

---

## Features

- Real-time QR code detection via webcam
- Timestamped logging of each scanned QR code
- Automatic browser redirection for scanned URLs
- Clean, modular project structure
- Easy to extend with Flask, database, GUI, or security layers

---

## Project Structure

```
qr-scanner-project/
│
├── main.py                  # Entry point – starts webcam and scanning loop
├── requirements.txt         # Required Python dependencies
├── README.md                # This documentation
├── LICENSE                  # MIT License
├── .gitignore               # Files/folders to exclude from version control
│
├── qr_utils/                # Utility modules
│   ├── detector.py          # Handles QR code detection logic
│   ├── logger.py            # Logs scan results into CSV with timestamp
│   └── generator.py         # (Optional) Generate QR code images
│
├── saved_logs/              # Scanned QR logs stored as CSV
│   └── qr_scans.csv
│
└── examples/                # Example or test QR images (optional)
```

---

## Installation

### Requirements

- Python 3.8 or newer
- `opencv-python`
- `qrcode` (optional, for QR generation)

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

To launch the scanner:

```bash
python main.py
```

- Press `ESC` or `SPACE` to exit.
- URLs will open automatically in your default web browser.
- All scan logs are saved in `saved_logs/qr_scans.csv`.

---

## Utility Modules

| Module                 | Description                                         |
|------------------------|-----------------------------------------------------|
| `qr_utils/detector.py` | QR detection using OpenCV’s `QRCodeDetector`        |
| `qr_utils/logger.py`   | Writes scan results to CSV with current timestamp   |
| `qr_utils/generator.py`| Creates QR code images from text or URLs (optional) |

---

## Future Enhancements

| Idea                   | Purpose                                 |
|------------------------|-----------------------------------------|
| Flask Web Interface    | Scan/upload QR codes via browser        |
| SQLite or MongoDB      | Store scan history in a database        |
| QR Security Filter     | Block malicious or phishing links       |
| Multi-camera Support   | Choose input source dynamically         |
| Batch QR Generator     | Create multiple QR codes programmatically |

---

## License

This project is licensed under the **MIT License** — free for both personal and commercial use.

See the [LICENSE](./LICENSE) file for more details.

---

## Contributing

Feel free to fork this repository, suggest improvements, or submit pull requests. All kinds of contributions are welcome — from bug fixes to feature ideas and documentation improvements.

---

## Contact

Developed by **Mertcan Kankılıç**  
Email: [mertcankankilic27@gmail.com](mailto:mertcankankilic27@gmail.com)

---

> Made with passion by a builder who loves modular, clean code.