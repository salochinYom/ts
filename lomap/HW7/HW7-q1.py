from lomap.classes import Buchi, Fsa
from lomap.classes import Ts


def find_accepting_path(product_system, fsa_accepting_states):
    """
    Finds an accepting path in the product system.
    :param product_system: The product transition system (Ts object).
    :param fsa_accepting_states: A list of accepting states in the FSA.
    :return: A list representing the accepting path, or None if no path exists.
    """
    from collections import deque

    # Initialize BFS queue with the initial state
    initial_state = list(product_system.init)[0]
    print(initial_state)
    queue = deque([(initial_state, [initial_state])])  # (current_node, path_to_node)
    print(queue)

    while queue:
        current_node, path = queue.popleft()

        print(current_node)

        # # Check if the current node satisfies the acceptance condition
        # ts_state, fsa_state = current_node.split(",")
        if current_node in fsa_accepting_states:
            return path  # Found an accepting path

        # Add neighbors to the queue
        for neighbor in product_system.g.adj[current_node]:
            if neighbor not in path:  # Avoid cycles
                queue.append((neighbor, path + [neighbor]))

    return None  # No accepting path found

def recursive_edge_adder(edgesToCheck, transition_system, ts1, fsa, known_edges):
    if len(edgesToCheck) > 0:
        IsA = edgesToCheck[0][2]
        IsB = edgesToCheck[0][3]
        #add new edges to the thing
        transition_system.g.add_edge(str(edgesToCheck[0][0]) + ","+ str(edgesToCheck[0][1]), str(edgesToCheck[0][2]) + ","+ str(edgesToCheck[0][3]))
        #transition_system.visualize()
        #remove the first edge and put it into known edges
        known_edges.append(edgesToCheck.pop(0))
        #print(known_edges)
        #iterate over all neighbors of the ts
        for q in list(ts1.g.adj[str(IsA)]):
            #iterate over all the next states of the FSA
            for s in list(fsa.next_state(str(IsB), hw_6_ts.g.nodes[str(IsA)]['prop'])):
                #print(str(q) + ' , ' + str(s))
                #check against edges we have been to
                have_been_to = False
                for i in range(len(known_edges)):
                    if known_edges[i][0] == IsA and known_edges[i][1] == IsB and known_edges[i][2] == q and known_edges[i][3] == s:
                        have_been_to = True
                #add to the list of edges to check
                print(have_been_to)
                if not have_been_to:
                    print("hello world")
                    edgesToCheck.append([IsA, IsB, q,s])
    
        print(len(edgesToCheck))
        transition_system = recursive_edge_adder(edgesToCheck, transition_system, ts1, fsa, known_edges)


if __name__ == '__main__':
    #initialize the transition system
    hw_6_ts = Ts.load('lomap/tests/hw_6_ts.yaml')
    hw_6_ts.visualize()

    #initalize the FSA
    fsa_file = 'lomap/tests/fa_and_fb.txt'
    fsa_formula = 'F a && F b'

    fsa = Fsa()
    fsa.from_formula(fsa_formula,fsa_file)
    fsa.visualize()

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

    #print(hw_6_ts.g.nodes[str(Is1)]['prop'])
    #print(str(Is1))
    #product_system.visualize()

    #initalize edges to check
    edgesToCheck = []
    for q in list(hw_6_ts.g.adj[str(Is1)]): #things adjacent to init of ts system
        for s in list(fsa.next_state(str(Is2), hw_6_ts.g.nodes[str(Is1)]['prop'])): #things adjacent in the FSA based off the prop in the current ts state
            #print(str(q) + " " + str(s))
            edgesToCheck.append([Is1, Is2, q, s])
    #print(edgesToCheck)

    #run the recursive thing
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
    
    #solution to part 1
    product_system.visualize()


