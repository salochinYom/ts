from lomap.classes import Buchi, Fsa
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

if __name__ == '__main__':
    #initialize the transition system
    hw_6_ts = Ts.load('lomap/tests/hw_6_ts.yaml')
    #hw_6_ts.visualize()

    #initalize the FSA
    fsa_file = 'lomap/tests/fa_and_fb.txt'
    fsa_formula = 'F a && F b'

    fsa = Fsa()
    fsa.from_formula(fsa_formula,fsa_file)
    #fsa.visualize()

    #initalize the new transition system
    product_system = Ts(name='product TS',multi=False,directed=True)

    #initalize all the nodes of the combined system
    FSA_nodes = list(fsa.g.nodes)
    #print(FSA_nodes)
    hw_6_ts_nodes = list(hw_6_ts.g.nodes)
    #print(hw_6_ts_nodes)

    #create the intial node and add it to the product system
    Is2 = FSA_nodes[0]
    Is1 = hw_6_ts_nodes[0]
    p_init_state = str(Is1) + "," + str(Is2)
    product_system.init = {p_init_state}

    #add all the nodes
    for q in list(FSA_nodes):
        for s in list(hw_6_ts_nodes):
            #print(str(q) + "," + str(s))
            product_system.g.add_node(str(q) + "," + str(s), prop="red")

    #intialize all the edges
    edgesToCheck = []
    for q in list(hw_6_ts.g.adj[str(Is1)]): #this should be all reachable states from the inital
        for s in list(fsa.g.adj[str(Is2)]): #this should be all reachable states from the inital state in the FSA
            #print(q + "," + s)
            edgesToCheck.append([Is1, Is2, q,s])
    #print(edgesToCheck)

    recursive_edge_adder(edgesToCheck, product_system, hw_6_ts, fsa, [])

    #remove unreachable nodes
    ps_nodes = list(product_system.g.nodes)
    rm_nodes = []
    for node in ps_nodes:
        #check if the node has neigbhors
        num_neighbors = len(list(product_system.g.adj[str(node)]))
        if num_neighbors == 0:
            rm_nodes.append(str(node))
    #remove the nodes
    product_system.g.remove_nodes_from(rm_nodes)

    product_system.visualize()
    #print(type(product_system))
    #print(len(product_system.g.nodes))


