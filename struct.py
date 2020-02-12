class Graph:

	def __init__(self):
		self.noeuds = dict()

	def add_node(self, id):
		self.noeuds[id] = set() #init les voisins a une liste vide
 
	
	#ajoute un node en voisin de id
	#si node n'est pas une cle, elle est ajoutee
	def add_voisin(self, id, node):
		if node not in self.noeuds.keys():
			self.add_node(node)
		self.noeuds[id].add(node)

			
	def __str__(self):
		print ("===Graph==nb node", len(self.noeuds), "===\n" )
		return str(self.noeuds)

	def clear(self):
		self.noeuds.clear()

	def nb_node(self):
		return len(self.noeuds)

	def values(self):
		return self.noeuds.values()

	def effective_values(self):
		res = set()
		for array in self.noeuds.values():
			for elem in array:
				res.add(elem)
		return res

	def get_voisins(self, id):
		return self.noeuds[id]

	def keys(self):
		return self.noeuds.keys()

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



