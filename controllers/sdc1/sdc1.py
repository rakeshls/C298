"""sdc1 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep =64
left_wheel = robot.getDevice("left_front_wheel")
right_wheel = robot.getDevice("right_front_wheel")
l_steer = robot.getDevice("left_steer")
r_steer = robot.getDevice("right_steer")
left_wheel.setPosition(float("inf"))
right_wheel.setPosition(float("inf"))
l_steer.setPosition(0)
r_steer.setPosition(0)
left_wheel.setVelocity(0)
right_wheel.setVelocity(0)


# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    left_wheel.setVelocity(10)
    right_wheel.setVelocity(10)
    
        
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
