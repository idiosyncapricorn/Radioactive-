# run.py
from gnuradio import gr, blocks
from grgsm import source_c, message

import requests
from gps_spoofer import spoof_gps
from gsm_logger import GSMLogger

# Initialize the GSM receiver and logger
src = source_c(args="rtl=0")
msg_sink = blocks.message_sink(gr.sizeof_char*1, message.MsgQueue(), False)
grgsm_receiver = grgsm.receiver()
grgsm_receiver.connect(src, 0)
grgsm_receiver.connect(grgsm_receiver, msg_sink)

# Start the radio flowgraph
src.start()
grgsm_receiver.start()

# Start GPS spoofing
latitude = 37.7749
longitude = -122.4194
spoof_gps(latitude, longitude)

# Initialize the GSM logger
logger = GSMLogger("gsm_log.txt")

# Define proxy details (replace with your own if needed)
proxies = {
    'http': 'http://yourproxyserver:port',
    'https': 'http://yourproxyserver:port',
}

# Send a test request through the proxy
response = requests.get('http://ip-api.com/json', proxies=proxies)
print("Response from IP API:")
print(response.json())

# Log GSM messages
print("Listening for cell tower signals and logging messages...")
try:
    while True:
        msg = msg_sink.get_message()
        if msg is not None:
            logger.log_message(str(msg))
except KeyboardInterrupt:
    print("Stopping GSM message logging...")
finally:
    # Stop the flowgraph
    src.stop()
    grgsm_receiver.stop()
