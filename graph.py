"""
author : gouth

structure de graph et de noeud primal
"""

class Graph:

	def __init__(self):
		self.noeuds = []
		self.nb_node = 0

	def add_node(self, id):
		self.noeuds.append(Noeud(id))
		self.nb_node +=1
 
	#on ne verifie pas si le noeud id a deja node en voisin TODO
	def add_voisin(self, id, node):
		for n in self.noeuds:
			if(n.id == id):
				n.add_voisin(Noeud(node))
				break
				
	def get_node(self, id):
		for n in self.noeuds:
			if(n.id == id):
				return n
			
	def afficher(self):
		print "===Graph==nb node", self.nb_node, "===\n" 
		for n in self.noeuds:
			n.afficher()



class Noeud:
	def __init__(self, id):
		self.id = id
		self.voisins = []

	def add_voisin(self, node):
		self.voisins.append(node)

	def afficher(self):
		res = "node:", self.id, " voisin : "
		for node in self.voisins:
			res += "",node.id

		print res



def clique_init(graph):
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



	


#return les noeuds communs entre l'ensemble P et U
#P et U sont des tableaux
def inter(P,U):
	p = list(P)
	p = sorted(p)
	U = sorted(U)

	i = 0
	j = 0

	res = []
	
	#print "limite de P : ", len(P)
	#print "limite de U : ", len(U)

	while(i<len(p) and j<len(U)): #fin du parcours d'un des deux tableaux
		#print "i:", i
		#print "j;", j

		if (p[i].id < U[j].id):
			i+=1
		elif (p[i].id > U[j].id):
			j+=1
		else:
			res.append(p[i])
			i+=1
			j+=1

	return res
	
#renvoie le noeud pivot candidat pour Tomita
#u \ argmax card|P inter voisin(u)|
#return -1 si pas de pivot mais devrait jamais arriver
#P et X object : set
def pivot(P, X):
	noeuds = P.union(X)

	maxi = -999 #-inf
	i = 0
	res = -1

	for node in noeuds: #P U X 
		voisins = node.voisins #array
		intersect = inter(P, voisins)
		tmp = len(intersect)
		if(tmp > maxi):
			maxi = tmp
			res = node
		i+=1

	return res.id


def test_inter(graph):
	
	res = inter([graph.get_node(3), graph.get_node(5), Noeud(8)], graph.noeuds)

	for node in res:
		node.afficher() #expected : 3,5


def test_pivot(graph):
	
	X = set()
	for node in graph.noeuds:
		X.add(node)

	P = set()
	P.add(graph.get_node(1))
	P.add(graph.get_node(2))
	P.add(graph.get_node(3))
	
	res = pivot(P, X)
	print res #expected 4 in output
	
	P.clear()

	P.add(graph.get_node(4))
	res = pivot(P, X)
	print res #expected 1 in output
	
	P.clear()

	P.add(graph.get_node(5))
	P.add(graph.get_node(6))
	

	
	res = pivot(P, X)
	print res #expected 7 in output


	
	

graph = Graph()
clique_init(graph)

#test_inter(graph)
test_pivot(graph)





 
