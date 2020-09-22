#!/usr/bin/python3

import sys
from picamera import PiCamera
from time import sleep


def main(num_minutes, fname):
    camera = PiCamera()
    camera.start_preview()
    for i in range(num_minutes):
        sleep(60)
        camera.capture("snapshots/" + fname + "%s.jpg" % i)
        print("Saved picture in snapshots/" + fname + "%s.jpg" % i)
    camera.stop_preview()


if __name__ == "__main__":
    num_minutes = 10
    fname = "snapshot"
    if len(sys.argv) > 1:
        num_minutes = int(sys.argv[1])
    if len(sys.argv) > 2:
        fname = sys.argv[2]
    print("Running pi-snap for %i minutes" % num_minutes)
    print("All files will be saved as " + fname + "#.jpg")
    main(num_minutes, fname)
