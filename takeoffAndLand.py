'''
Code we were hoping to test if mavproxy connection was established
This Python script is designed to establish a connection to a drone using the DroneKit library (dronekit) and perform a simple takeoff and landing sequence
'''
from dronekit import connect, VehicleMode
import time
import argparse

def connect_drone():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    ip = args.connect
    vehicle = connect(ip, wait_ready=True)

    return vehicle

def arm(target):
    while not vehicle.is_armable:
        print("waiting")
        time.sleep(1)
    vehicle.simple_takeoff(target)

    while True:
        print("current :%d" % vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= target * .95:
            break
        time.sleep(1)
    print("done")
    return None

vehicle = connect_drone()
print("About to takeoff..")
vehicle.mode = VehicleMode("GUIDED")
arm(2)
vehicle.mode = VehicleMode("LAND")

time.sleep(2)

print("END OF FUNCTION")
print("Arducopter version: %s" % vehicle.version)

while True:
    time.sleep(2)
vehicle.close()
