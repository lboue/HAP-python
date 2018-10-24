"""An example of how to setup and start an Accessory.

This is:
1. Create the Accessory object you want.
2. Add it to an AccessoryDriver, which will advertise it on the local network,
    setup a server to answer client queries, etc.
"""
import logging
import signal

from pyhap.accessory import Bridge
from pyhap.accessory_driver import AccessoryDriver
import pyhap.loader as loader

# The below package can be found in the HAP-python github repo under accessories/
from accessories.TemperatureSensor import TemperatureSensor
from accessories.WindowCovering import WindowCovering

logging.basicConfig(level=logging.INFO)


def get_bridge(driver):
    """Call this method to get a Bridge instead of a standalone accessory."""
    bridge = Bridge(driver, 'Bridge')
    temp_sensor = TemperatureSensor(driver, 'Sensor 2')
    temp_sensor2 = TemperatureSensor(driver, 'Sensor 1')
    cover1 = WindowCovering(driver, 'Cover1')
    #set_info_service(temp_sensor, firmware_revision=1)
    temp_sensor2.set_info_service(firmware_revision=1,  manufacturer="Brand",
                                     model="model", serial_number="0123456789")
    bridge.add_accessory(temp_sensor)
    bridge.add_accessory(temp_sensor2)
    bridge.add_accessory(cover1)

    return bridge


def get_accessory(driver):
    """Call this method to get a standalone Accessory."""
    return TemperatureSensor(driver, 'MyTempSensor')


# Start the accessory on port 51826
driver = AccessoryDriver(port=51826)

# Change `get_accessory` to `get_bridge` if you want to run a Bridge.
#driver.add_accessory(accessory=get_accessory(driver))
driver.add_accessory(accessory=get_bridge(driver))

# We want SIGTERM (kill) to be handled by the driver itself,
# so that it can gracefully stop the accessory, server and advertising.
signal.signal(signal.SIGTERM, driver.signal_handler)

# Start it!
driver.start()
