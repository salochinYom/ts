from lomap.classes import Buchi, Fsa

# note, you may need to enter the full path to this file, depending on your environment
fsa_file = 'lomap/tests/fa_and_fb.txt'
fsa_formula = 'F a && F b'

# note, you may need to enter the full path to this file, depending on your environment
buchi_file = 'lomap/tests/fga_and_fb.txt'
buchi_formula = 'F G a && F b'

# instantiate an FSA from a file
F = Fsa()
F.from_formula(fsa_formula,fsa_file)

# instantiate a Buchi from a file
B = Buchi()
B.from_formula(buchi_formula,buchi_file)

B.init # initial state
B.final # final state

# visualize
B.visualize()

# get next state(s) for a given input
B.next_state('T0_init','a') # state is 'T0_init', input is 'a'
B.next_state('T0_init','ab') 
B.next_state('T0_init','a && b') # this is equivalent to the line above