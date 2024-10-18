from gnuradio import gr
from gnuradio import blocks
from grgsm import source_c, message

# Initialize the software-defined radio source
src = source_c(args="rtl=0")

# Set up blocks to decode GSM signals
msg_sink = blocks.message_sink(gr.sizeof_char*1, message.MsgQueue(), False)
grgsm_receiver = grgsm.receiver()
grgsm_receiver.connect(src, 0)
grgsm_receiver.connect(grgsm_receiver, msg_sink)

# Start the radio flowgraph
src.start()
grgsm_receiver.start()

print("Listening for cell tower signals...")

import os

# Define the fake GPS coordinates
latitude = 37.7749
longitude = -122.4194

# Command to send the fake GPS location to the Android device
command = f"adb shell am startservice -e latitude {latitude} -e longitude {longitude} com.github.falkenapps.mocklocation/.MockLocationService"
os.system(command)

print(f"GPS spoofed to Latitude: {latitude}, Longitude: {longitude}")

import requests

# Define the proxy server (replace with your proxy server details)
proxies = {
    'http': 'http://yourproxyserver:port',
    'https': 'http://yourproxyserver:port',
}

# Send a request through the proxy
response = requests.get('http://ip-api.com/json', proxies=proxies)
print("Response from IP API:")
print(response.json())

