
import struct
import algo 


def test_inter(graph):
	print "\t===test_inter du graph : "
	print graph , "\n"
	##j'ai reprogramme l'intersection de deux ensemble en O(n)
	#n etant la longueur la plus petite des deux ensemble a test
	nb_node = graph.nb_node()

	P = set()
	X = set()
	j = (nb_node/2) #division entiere 
	keys = graph.keys()
	add = nb_node%2
	for i in range(1, (nb_node/2)+1+add):
		P.add(keys[i])
		X.add(keys[j])
		j+=1
	
	
	inter = algo.inter(P,X)
	assert(len(inter)==2)
	print  "intersection", P, " et " , X, "= ", inter
	print "\n\tend_test_inter==\n"
	


def test_pivot(graph):
	nb_node = graph.nb_node()
	P = set()
	X = set()
	
	P.add(1) 
	P.add(2) 
	P.add(3)
	res = algo.pivot(P, X, graph)

	assert(res==1) 	


	P.add(4)
	res = algo.pivot(P, X, graph)
	assert(res==2)
	
	P.clear()
	
	P.add(5)
	P.add(6)
	res = pivot(P, X)
	assert(res==7) 


def test_bron(graph):
	P = set()
	R = set()
	X = set()

	P = set(graph.noeuds)
	"""
	for n in P:
		print n
	"""
	BronKerbosch(P,R,X)
	
	print "\n====++CLIQUE MAX++======\n"
	for n in R:
		print n


def test_structure():
	"""
	# ADD_NODE(ID)
	"""
	graph = struct.Graph()
	graph.add_node(1)
	assert(graph.nb_node() == 1)
	graph.add_node(1)
	assert(graph.nb_node() == 1)
	graph.add_node(2)
	assert(graph.nb_node() == 2)
	assert(len(graph.values()) == 2)
	assert(len(graph.effective_values())==0)


	"""
	#ADD_VOISIN(ID, NODE)
	"""

	graph.add_voisin(1, 2)
	assert(graph.nb_node() == 2)
	assert(len(graph.values()) == 2)
	assert(len(graph.effective_values())==1)

	graph.add_voisin(1, 2)
	assert(graph.nb_node() == 2)
	assert(len(graph.values()) == 2)
	assert(len(graph.effective_values())==1)

	graph.add_voisin(1, 3)
	assert(graph.nb_node() == 3)
	assert(len(graph.values()) == 3)
	assert(len(graph.effective_values())==2)

	graph.add_voisin(2, 3)
	assert(graph.nb_node() == 3)
	assert(len(graph.values()) == 3)
	assert(len(graph.effective_values())==2)

	print graph
	print graph.values()
	print graph.effective_values()