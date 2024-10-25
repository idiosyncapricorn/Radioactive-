Here’s an updated README.md with details on setting up and running the modules:

GSM Signal Sniffer and GPS Spoofer

This is a playful side project that does the following:

	1.	Listens for GSM signals using GNU Radio and gr-gsm. It initializes a software-defined radio (SDR) source and attempts to capture signals from nearby cell towers.
	2.	Spoofs GPS coordinates to a specified location (in this case, San Francisco) by sending fake latitude and longitude values to an Android device via ADB.
	3.	Makes requests through a proxy to obtain IP location data, showing the result from the ip-api.com API.

	Disclaimer: This is just for fun and experimental purposes only. Please avoid any illegal or unethical use!

Project Structure

project/
├── gsm_logger.pyx       # Cython module for logging GSM messages
├── gps_spoofer.py       # GPS spoofing module
├── setup.py             # Setup script to build Cython modules
└── run.py               # Main script to run the project

Requirements

	•	Python 3.6+
	•	GNU Radio and gr-gsm installed
	•	Cython for building the logging module
	•	ADB for GPS spoofing on Android
	•	requests library for IP location requests

Install Cython and requests if you haven’t already:

pip install cython requests

Setup Instructions

	1.	Build the Cython Logger Module:
Run the following command in the project directory to build gsm_logger.pyx:

python setup.py build_ext --inplace


	2.	Configure Your Proxy (optional):
If you’d like to use the proxy functionality, update the proxy settings in run.py:

proxies = {
    'http': 'http://yourproxyserver:port',
    'https': 'http://yourproxyserver:port',
}



Running the Project

To start the project, simply run:

python run.py

This script will:

	•	Initialize and start the GSM receiver.
	•	Start GPS spoofing on the specified latitude and longitude (San Francisco in this example).
	•	Start logging any received GSM messages into gsm_log.txt.

Modules

	•	gsm_logger: A Cython-based logger module that captures and logs GSM messages efficiently into a file.
	•	gps_spoofer: A separate Python module that uses ADB to send fake GPS coordinates to an Android device.
	•	run.py: The main execution script that coordinates the GSM signal listening, GPS spoofing, and logging functions.
