# gps_spoofer.py
import os

def spoof_gps(latitude, longitude):
    """
    Spoofs GPS coordinates on an Android device using ADB.
    """
    command = (
        f"adb shell am startservice -e latitude {latitude} "
        f"-e longitude {longitude} com.github.falkenapps.mocklocation/.MockLocationService"
    )
    os.system(command)
    print(f"GPS spoofed to Latitude: {latitude}, Longitude: {longitude}")