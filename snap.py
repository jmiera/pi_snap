#!/usr/bin/python3

import sys
from picamera import PiCamera
from time import sleep


def main(num_minutes):
    camera = PiCamera()
    camera.start_preview()
    for i in range(num_minutes):
        sleep(60)
        camera.capture("snapshots/snapshot%s.jpg" % i)
    camera.stop_preview()


if __name__ == "main":
    num_minutes = 10
    if len(sys.argv > 1):
        num_minutes = int(sys.argv[1])
    main(num_minutes)
