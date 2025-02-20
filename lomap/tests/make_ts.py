import networkx as nx

from lomap.classes import Ts

if __name__ == '__main__':

    ts = Ts(name='Simple TS',multi=False,directed=True) # Initialize empty TS; give it a name, make it directed, but not a multi-graph

    # Let's assume 3 nodes, q0, q1, q2, q3
    # Inital node is q0
    # Nodes have self loops and go in a cycle 0 -> 1 -> 2 -> 3 -> 0

    ts.init = {'q0'}

    # Add nodes one at a time
    ts.g.add_node('q0')

    # Or add a list of nodes
    ts.g.add_nodes_from(['q1','q2'])

    # Display list of nodes
    print(ts.g.nodes())

    # Add some labels
    ts.g.nodes['q0']['prop'] = 'green'
    ts.g.nodes['q1']['prop'] = 'yellow'
    ts.g.nodes['q2']['prop'] = 'red'
    
    # This can also be done when the node is added
    ts.g.add_node("q3", prop="blue")

    # Add some edges
    ts.g.add_edge('q0','q1')
    
    # Or as a list
    ts.g.add_edges_from([('q1','q2'),('q2','q3'),('q3','q0'),('q0','q0'),('q1','q1'),('q2','q2'),('q3','q3')])

    # Look at successors (result is an iterator, hence the list comprehension)
    print('Successors of q0: ',[q for q in ts.g.successors('q0')])

    # Look at predecessors (result is an iterator, hence the list comprehension)
    print('Predecessors of q0: ',[q for q in ts.g.predecessors('q0')])

    # Examine node labels
    print('Labels on q0: ',ts.g.nodes['q0']['prop'])

    # Handy networkx functions exist for things like reachability
    print('Reachable states from q0: ',nx.descendants(ts.g,'q0'))

    # Visualize
    ts.visualize()