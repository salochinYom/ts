from lomap.classes import Buchi, Fsa
from lomap.classes import Ts

if __name__ == '__main__':
    #initialize the traffic light
    traffic_light = Ts.load('lomap/tests/hw_6_ts.yaml')
    traffic_light.visualize() #isn't there a edge between q2 and q0
