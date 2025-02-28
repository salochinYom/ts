import networkx as nx

from lomap.classes import Ts

def recursive_edge_adder(edgesToCheck, transition_system, ts1, ts2, known_edges):
    if len(edgesToCheck) > 0:
        IsA = edgesToCheck[0][2]
        IsB = edgesToCheck[0][3]
        #add new edges to the thing
        transition_system.g.add_edge(str(edgesToCheck[0][0]) + ","+ str(edgesToCheck[0][1]), str(edgesToCheck[0][2]) + ","+ str(edgesToCheck[0][3]))
        #transition_system.visualize()
        #remove the first edge and put it into known edges
        known_edges.append(edgesToCheck.pop(0))
        #add edges to the thing
        for q in list(ts1.g.adj[str(IsA)]):
            for s in list(ts2.g.adj[str(IsB)]):
                #print(q + "," + s)
                #check this edge against every other edge we have been to
                have_been_to = False
                for i in range(len(known_edges)):
                    if known_edges[i][0] == IsA and known_edges[i][1] == IsB and known_edges[i][2] == q and known_edges[i][3] == s:
                        have_been_to = True

                #check against every edge that we need to check
                # for i in range(len(edgesToCheck)):
                #     if edgesToCheck[i][0] == IsA and edgesToCheck[i][1] == IsB and edgesToCheck[i][2] == q and edgesToCheck[i][3]:
                #         have_been_to = True

                
                if not have_been_to:
                    edgesToCheck.append([IsA, IsB, q,s])
        
        #show the edge list
        #print(edgesToCheck)

        transition_system = recursive_edge_adder(edgesToCheck, transition_system, ts1, ts2, known_edges)
    #print(known_edges)
    return transition_system
if __name__ == '__main__':
    #initialize the traffic light
    traffic_light = Ts.load('lomap/tests/traffic_light.yaml')
    #traffic_light.visualize() #isn't there a edge between q2 and q0

    #initialize pedestrian signal
    pedestrian_signal = Ts.load('lomap/tests/pedestrian_signal.yaml')
    #pedestrian_signal.visualize()

    #initalize the new transition system
    product_system = Ts(name='product TS',multi=False,directed=True)
    
    #chose the start state as the initial states of both system
    Is1 = list(traffic_light.g.nodes)[0]
    Is2 =list(pedestrian_signal.g.nodes)[0]
    p_init_state = str(Is1) + "," + str(Is2)
    #print(p_init_state)
    product_system.init = {p_init_state}

    #add all the nodes
    for q in list(traffic_light.g.nodes):
        for s in list(pedestrian_signal.g.nodes):
            #print(str(q) + "," + str(s))
            product_system.g.add_node(str(q) + "," + str(s), prop="red")

    #initialize the list of edges
    # a list of edges is a list of 2 part tuples that start with the start position and ends with the
    edgesToCheck = []
    for q in list(traffic_light.g.adj[str(Is1)]):
        for s in list(pedestrian_signal.g.adj[str(Is2)]):
            #print(q + "," + s)
            edgesToCheck.append([Is1, Is2, q,s])
    print(edgesToCheck)


    #use natrual recursion to iterate through the things
    #assume the inital state is at indice 0
    #print(list(traffic_light.g.adj['q1']))
    recursive_edge_adder(edgesToCheck, product_system, traffic_light, pedestrian_signal, [])


    product_system.visualize()




