import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
rightreverse = 20
rightforward = 21
leftreverse = 19
leftforward = 26

leftsensor = 22
rightsensor = 25

movementpins = [rightreverse, rightforward, leftreverse, leftforward]
sensorpins = [leftsensor, rightsensor]

for gpin in movementpins:
    GPIO.setup(gpin, GPIO.OUT)
    GPIO.output(gpin, GPIO.LOW)

for gpin in sensorpins:
    GPIO.setup(gpin, GPIO.IN)

def move_forward():
    GPIO.output(leftforward, GPIO.HIGH)
    GPIO.output(rightforward, GPIO.HIGH)
    GPIO.output(leftreverse, GPIO.LOW)
    GPIO.output(rightreverse, GPIO.LOW)

def move_right():
    GPIO.output(leftforward, GPIO.HIGH)
    GPIO.output(rightforward, GPIO.LOW)
    GPIO.output(leftreverse, GPIO.LOW)
    GPIO.output(rightreverse, GPIO.LOW)

def move_left():
    GPIO.output(leftforward, GPIO.LOW)
    GPIO.output(rightforward, GPIO.HIGH)
    GPIO.output(leftreverse, GPIO.LOW)
    GPIO.output(rightreverse, GPIO.LOW)

def stop():
    GPIO.output(leftforward, GPIO.LOW)
    GPIO.output(rightforward, GPIO.LOW)
    GPIO.output(leftreverse, GPIO.LOW)
    GPIO.output(rightreverse, GPIO.LOW)

def left_sensor_hit_tape():
    return GPIO.input(leftsensor)

def right_sensor_hit_tape():
    return GPIO.input(rightsensor)


try: 
    while True:
        current_right_sensor_hit_tape = right_sensor_hit_tape()
        current_left_sensor_hit_tape = left_sensor_hit_tape()

        if not current_right_sensor_hit_tape and not current_left_sensor_hit_tape:
            print("moving forward")
            move_forward()
        elif current_left_sensor_hit_tape and current_left_sensor_hit_tape:
            print("stopping")
            stop()
        elif current_right_sensor_hit_tape:
            print("moving right")
            move_right()
        elif current_left_sensor_hit_tape:
            print("moving left")
            move_left()
except KeyboardInterrupt:
    print("\nProgram Terminated")
finally:
    GPIO.cleanup()