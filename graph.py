"""
author : gouth

structure de graph et de noeud primal
"""
import conf #fichier ou il y a les setups de graphs pour les tests
import test #fichier ou y'a les procedures de tests
import struct
import algo


	



graph = struct.Graph()
"""
#une clique maxi {1,2,3,4}
clique_init(graph)
#test_inter(graph)
#test_pivot(graph)
test_bron(graph)
"""


#deux clique maxi {1,2,3,4} et {5,6,7,8}
conf.clique_init(graph)
print (graph)
#test.test_inter(graph)
test.test_pivot(graph)
test.test_bron(graph)
test.test_structure()





 
