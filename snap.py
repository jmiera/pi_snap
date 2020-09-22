#!/usr/bin/python3

import sys
from picamera import PiCamera
from time import sleep


def main(num_minutes, fname):
    print("Trace 5")
    camera = PiCamera()
    print("Trace 6")
    camera.start_preview()
    print("Trace 7")
    for i in range(num_minutes):
        sleep(60)
        camera.capture("snapshots/" + fname + "%s.jpg" % i)
        print("Trace 8")
        print("Saved picture in snapshots/snapshot%s.jpg" % i)
    camera.stop_preview()
    print("Trace 9")


if __name__ == "__main__":
    print("Trace 1")
    num_minutes = 10
    fname = "snapshot"
    if len(sys.argv) > 1:
        print("Trace 2")
        num_minutes = int(sys.argv[1])
    if len(sys.argv) > 2:
        fname = sys.argv[2]
    print("Trace 3")
    main(num_minutes, fname)
    print("Trace 4")
