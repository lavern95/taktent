
from taktent.agents import *
from taktent.populations.population import *
from taktent.strategies import *
from numpy import pi, cos, sin

# test the observed doppler drift of a narrowband transmission

time = 0.0
tbegin = 0.0
tend = 1.0
dt = 0.01

# Define transmitter properties

transmitter_pos = vector.Vector3D(10.0,0.0,0.0)
transmitter_vel = vector.Vector3D(0.0,0.0,0.0)
transmitter_dir = vector.Vector3D(-1.0,0.0,0.0)
transmitter_a = 1.0         # AU
transmitter_starmass = 1.0  # solarmass
transmitter_inc = 0.0

freq = 1.0e9
band = 0.1
openangle = 0.1*pi
solidangle = 4.0*pi
power = 100.0

# Define a scanning transmitter strategy:

# function to define transmitter target vector (constant direction)
def transmit_strategy(time, tinit=0.0, period_xy=0.0, period_yz=0.0, phase_xy=0.0, phase_yz=0.0):
    return vector.Vector3D(-1.0,0.0,0.0).unit()

# scanningStrategy object
strat = scanningStrategy.scanningStrategy(transmit_strategy)

# create transmitter object

tran = transmitter.Transmitter(transmitter_pos,transmitter_vel,strat,transmitter_dir,openangle,transmitter_pos.copy(), transmitter_vel.copy(),nu=freq,bandwidth=band,solidangle=solidangle,power=power, tbegin=tbegin, tend=tend)


# Define its orbital properties
transmitter.a = transmitter_a
transmitter.inclination = transmitter_inc
transmitter.mean_anomaly = 0.0
transmitter.longascend = 0.0


# Define Observer properties

observer_dir = vector.Vector3D(1.0,0.0,0.0).unit()
strat_obs = strategy.Strategy()

# Define Population and create observer at origin

popn = Population(tbegin, tend,dt)

observerID = popn.generate_observer_at_origin(observer_dir,openangle,strat_obs)

popn.agents[-1].nu_min = tran.nu*(1.0-6.0e-4)
popn.agents[-1].nu_max = tran.nu*(1.0+6.0e-4)
popn.add_agent(tran)


# Define plot limits

markersize = 0.5
wedge_length = 5.0
xmax = 20
ymax = 20

# Initialise population ready for run
popn.initialise()

# Test run for multiple steps, outputting to file
for i in range(popn.nsteps):

    print ("Time: ",popn.time)
    popn.conduct_observations()

    outputfile = 'population_'+str(i).zfill(3)+'.png'
    popn.plot(markersize,wedge_length, xmax,ymax, outputfile)
    popn.update()






