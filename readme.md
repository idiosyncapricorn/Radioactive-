GSM Signal Sniffer and GPS Spoofer

This is a playful side project that does the following:

	1.	Listens for GSM signals using GNU Radio and gr-gsm. It initializes a software-defined radio (SDR) source and attempts to capture signals from nearby cell towers.
	2.	Spoofs GPS coordinates to a specified location (in this case, San Francisco) by sending fake latitude and longitude values to an Android device via ADB.
	3.	Makes requests through a proxy to obtain IP location data, showing the result from the ip-api.com API.

Disclaimer: This is just for fun and experimental purposes only. Please avoid any illegal or unethical use!