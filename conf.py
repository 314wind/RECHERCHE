"""
fichier configuration initiale du graph

author : gouth

"""

def clique_init(graph):
	graph.clear()

	for i in range(1, 8): #ajout de 7 noeuds
		graph.add_node(i)

	 
	graph.add_voisin(1, 2) #le noeud 1 a pour voisin le noeud 2
	graph.add_voisin(1, 3)
	graph.add_voisin(1, 4)

	graph.add_voisin(2, 1)
	graph.add_voisin(2, 3)
	graph.add_voisin(2, 4)
	graph.add_voisin(2, 5)

	graph.add_voisin(3, 1)
	graph.add_voisin(3, 2)
	graph.add_voisin(3, 4)

	graph.add_voisin(4, 1)
	graph.add_voisin(4, 2)
	graph.add_voisin(4, 3)

	graph.add_voisin(5, 6)
	graph.add_voisin(5, 7)

	graph.add_voisin(6, 5)
	graph.add_voisin(6, 7)

	graph.add_voisin(7, 5)
	graph.add_voisin(7, 6)


def clique_init2(graph):
	graph.clear()

	for i in range(1, 9): #ajout de 8 noeuds
		graph.add_node(i)

	 
	graph.add_voisin(1, 2) #le noeud 1 a pour voisin le noeud 2
	graph.add_voisin(1, 3)
	graph.add_voisin(1, 4)

	graph.add_voisin(2, 1)
	graph.add_voisin(2, 3)
	graph.add_voisin(2, 4)
	graph.add_voisin(2, 5)

	graph.add_voisin(3, 1)
	graph.add_voisin(3, 2)
	graph.add_voisin(3, 4)

	graph.add_voisin(4, 1)
	graph.add_voisin(4, 2)
	graph.add_voisin(4, 3)

	graph.add_voisin(5, 6)
	graph.add_voisin(5, 7)
	graph.add_voisin(5, 8)
	graph.add_voisin(5, 2)

	graph.add_voisin(6, 5)
	graph.add_voisin(6, 7)
	graph.add_voisin(6, 8)

	graph.add_voisin(7, 5)
	graph.add_voisin(7, 6)
	graph.add_voisin(7, 8)
	
	graph.add_voisin(8, 5)
	graph.add_voisin(8, 6)
	graph.add_voisin(8, 7)


def clique_init3(graph):
	graph.clear()

	for i in range(1, 7): 
		graph.add_node(i)

	 
	graph.add_voisin(1, 2) #le noeud 1 a pour voisin le noeud 2
	graph.add_voisin(1, 5)

	graph.add_voisin(2, 1)
	graph.add_voisin(2, 3)
	graph.add_voisin(2, 5)

	graph.add_voisin(3, 2)
	graph.add_voisin(3, 4)

	graph.add_voisin(4, 3)
	graph.add_voisin(4, 5)
	graph.add_voisin(4, 6)

	graph.add_voisin(5, 1)
	graph.add_voisin(5, 2)
	graph.add_voisin(5, 4)


	graph.add_voisin(6, 4)


def clique_init_wiki(graph):
	graph.clear()

	for i in range(1, 7):
		graph.add_node(i)

	graph.add_voisin(1, 2)
	graph.add_voisin(1, 5)

	graph.add_voisin(2, 1)
	graph.add_voisin(2, 3)
	graph.add_voisin(2, 5)
	
	graph.add_voisin(3, 2)
	graph.add_voisin(3, 4)

	graph.add_voisin(4, 3)
	graph.add_voisin(4, 5)
	graph.add_voisin(4, 6)

	graph.add_voisin(5, 1)
	graph.add_voisin(5, 2)
	graph.add_voisin(5, 4)

	graph.add_voisin(6, 4)