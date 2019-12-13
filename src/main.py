#!/usr/bin/env pybricks-micropython

"""
JK 

When someone gets near our robot, it will turn around and move away from the person.
The robot will stop when someone gets in its way more than five times. 

"""
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
# Play a sound twice.
brick.sound.beep(2000) 

# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
obstacle_sensor = UltrasonicSensor (Port.S4)

# Initialize two motors with defult settings on Port B and Port C.
# These will be left and right motors of the drive base.
left_motor = Motor (Port.B)   
right_motor = Motor (Port.C)

# The wheel diameter of the Robot Educator is 56 millimeters
wheel_diameter = 56

# The axle track is the distance between the centers of each of the wheels.
# For the Robot Educator this is 114 millimeters.
axle_track = 114                                          

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
robot = DriveBase (left_motor, right_motor, wheel_diameter, axle_track)

times = 0   # start at zero

# The following loop makes the robot drive forward until it detects an 
# obstacle. Then it backs up and turns around. It keeps on doing this 
# until you stop the program.
while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive (200,0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured 
    # distance is still greater than 300 mm.
    while obstacle_sensor.distance () > 300:
        wait (2)

    times = times + 1

    # Drive backward at 100 millimeters per second. Keep going for 2 seconds.
    robot.drive_time (-100, 0, 2000)

    # Turn around at 60 degrees per second, around midpoint between 
    # the wheels. Keep going for 2 seconds.
    robot.drive_time (0, 60, 2000)
    if times > 30:
        robot.stop()
        break
