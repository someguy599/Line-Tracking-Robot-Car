##Bill of Materials:
Raspberry Pi and breadboard
3V-6V DC 1:120 Gear Motor TT Motor (2x)
L298n Dual H-Bridge Motor Driver
3Pcs Infrared Obstacle Avoidance Sensor (2x)
Batteries
Wires

##Goal
The overall goal of this project was to develop a lane tracing robot car. I built a car that would be able to follow a path that was created using black electrical tape. The car would use attached infrared sensors that wouldn't be able to detect the black tape. This way, the car would directly travel on the black tape as the sensors wouldn't perceive any obstacles in their way.

##How I Did This
I began this project by assembling the main chassis of the car. Once the main chassis was done, I moved onto dealing with the electricals. I first made a connection between the motors and the motor driver. In the Dual H-Bridge motor driver, there are two motor connectors, the motor A connector and the motor B connector, which connect directly to the motors. I made a connection between the 2 DC TT motors and Motor A and Motor B connectors on the Dual H-Bridge motor driver. There are also power connectors on the H-Bridge motor driver. There is one port for ground, and one port for power supply input, which will be connected with the batteries. Finally, there are 4 motor controller pins on the motor driver, and these pins will be connected with the GPIO pins. Each pair of pins affects one motor, and in each pair, one pin makes the motor spin clockwise while the other makes it spin counterclockwise. This is what will be used to make the robot car move.

Next, I attach the infrared sensors to the car. The Infrared Obstacle Avoidance Sensors has 3 pins, one for 5 volt, one for ground, and the last one for output. These pins will be used to connect the sensors to the Raspberry Pi GPIO pins. The infrared sensor has two LED’s, one transmitter and one receiver. The transmitter LED shoots out an infrared ray, and if there is an object in the way, the ray is reflected back and is received by the receiver LED and the output is made high. This is how the sensors are able to alert whether there is some object in front of them.
