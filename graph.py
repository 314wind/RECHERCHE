"""
author : gouth

structure de graph et de noeud primal
"""

class Graph:

	def __init__(self):
		self.noeuds = set()
		self.nb_node = 0

	def add_node(self, id):
		self.noeuds.add(Noeud(id))
		self.nb_node +=1
 
	
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
		self.voisins = set()

	def add_voisin(self, node):
		self.voisins.add(node)

	def __str__(self):
		res = "node_id: " + str(self.id) + "\tvoisin:{"
		for node in self.voisins:
			res = res + str(node.id) +","

		return res + "}"



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
#P et U sont des ensembles
def inter(P,U):
	p = list(P) #set to list for sorting
	u = list(U)
	p = sorted(p)
	u = sorted(u)

	i = 0
	j = 0

	res = set()
	
	#print "limite de P : ", len(P)
	#print "limite de U : ", len(U)

	while(i<len(p) and j<len(u)): #fin du parcours d'un des deux tableaux
		#print "i:", i
		#print "j;", j

		if (p[i].id < u[j].id):
			i+=1
		elif (p[i].id > u[j].id):
			j+=1
		else:
			res.add(p[i])
			i+=1
			j+=1

	return res
	
#renvoie le noeud pivot candidat pour Tomita
#u \ argmax card|P inter voisin(u)|
#return 	-1 si pas de pivot mais devrait jamais arriver
#		id du noeud
#P et X object : ensemble
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

	return res

#algo de recherche de clique maximale
# 
def BronKerbosch(P, R, X):
	if len(P.union(X))==0: #ens. vide
		print "FIN"
		return R #clique maximale
	
	u = pivot(P,X)	#noeud pivot
	print "pivot u : ", u
	p = P.difference(u.voisins) # P \ voisins(u)
	for node in p:
		print "entree de boucle ==P:",len(P)," R:",len(R)," X:",len(X)
		p_tmp = inter(P, u.voisins)
		R.add(u)
		x_tmp = inter(X, u.voisins)
		print "\napres recalcule  ==P:",len(p_tmp)," R:",len(R)," X:",len(x_tmp)
		
		BronKerbosch(p_tmp, R, x_tmp)
		print "end recur"
		
		for n in P:
			print n
		print "il faut remove : U = ", u		
		P.discard(u)
		X.add(u)







def test_inter(graph):
	
	res = inter([graph.get_node(3), graph.get_node(5), Noeud(8)], graph.noeuds)

	for node in res:
		print node #expected : 3,5


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


def test_bron(graph):
	P = set()
	R = set()
	X = set()

	P = set(graph.noeuds)

	for n in P:
		print n

	BronKerbosch(P,R,X)
	
	print "\n\n\n====++CLIQUE MAX++======\n"
	for n in R:
		print n


	
	

graph = Graph()
clique_init(graph)

#test_inter(graph)
#test_pivot(graph)
test_bron(graph)





 
