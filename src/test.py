from agents import *
from populations.population import *
from numpy import pi

print (vector)
# test code imports key classes, makes a transmitter and an observer object, and plots them

transmitter_pos = vector.Vector3D(10.0,0.0,0.0)
transmitter_vel = vector.Vector3D(0.0,0.0,0.0)
freq = 1.0e9
band = 1.0e8
solidangle = 0.1*pi
power = 100.0

openangle = 0.1*pi

markersize = 0.5
wedge_length = 5.0
xmax = 20
ymax = 20

time = 0.0

transmitter_dir = vector.Vector3D(0.0,1.0,0.0)
observer_dir = vector.Vector3D(1.0,0.0,0.0)

popn = Population(time)

tran = transmitter.Transmitter(transmitter_pos,transmitter_vel,transmitter_dir,openangle,transmitter_pos, 1.0,1.0,1.0,freq,band,solidangle,power)

popn.generate_observer_at_origin(observer_dir,openangle)
popn.add_agent(tran)

popn.plot(markersize,wedge_length, xmax,ymax)









