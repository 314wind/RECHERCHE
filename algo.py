"""
fichier contenant les algos principaux 

author : gouth

"""
#return les noeuds communs entre l'ensemble P et U
#P et U sont des ensembles
#O(nlog(n)) pour le tri puis simple parcours O(n)
def inter(P,U):
	p = list(P) #set to list for sorting
	u = list(U)
	p = sorted(p)
	u = sorted(u)

	i = 0
	j = 0

	res = set()
	
	#print ("limite de P : ", len(P))
	#print ("limite de U : ", len(U))

	while(i<len(p) and j<len(u)): #fin du parcours d'un des deux tableaux
		#print ("i:", i)
		#print ("j;", j)

		if (p[i] < u[j]):
			i+=1
		elif (p[i] > u[j]):
			j+=1
		else:
			res.add(p[i])
			i+=1
			j+=1

	return res
	
#renvoie le noeud pivot candidat pour BronKerbosch
#u \ argmax card|P inter voisin(u)|
#return 	-1 si pas de pivot mais devrait jamais arriver
#			id du noeud sinon
#P et X object : ensemble
#O(n^2log(n)) a verif
def pivot(P, X, graph):

    noeuds = P.union(X)
    assert(len(P) + len(X) >= len(noeuds))
    """
    print ("DEBUG :")
    print_set(P, noeuds, X)
    """
    maxi = -1 
    i = 0
    res = -1
    
    for node in noeuds: #P U X 
        voisins = graph.get_voisins(node) #set
        intersect = inter(P, voisins)
        tmp = len(intersect)
        if(tmp > maxi):
            maxi = tmp
            res = node
        i+=1

    return res


def print_set(P,R,X):
	print ("============track============\n")
	print ("P:", P,"\tR:", R, "\tX:", X)
	print ("-----------------------------\n")

#algo de recherche de clique maximale
# 
def BronKerbosch(P, R, X, G, depth):
	print("\n\nlevel :", depth,"\n")
	#print_set(P,R,X)
	if (len(P)== 0 and len(X)==0): #ens. vide
		print ("\t\t\tClique found : ")
		print_set({}, R, {})
		return R #clique maximale
	
	u = pivot(P,X,G)	#noeud pivot Tomita et al
	ens_u = set()		#set(u) in order to perform union later	 
	ens_u.add(u)
	assert(len(ens_u)==1)
	voisins = G.get_voisins(u)
	p = P.difference(voisins) 
	
	assert(len(p) <= len(P))
	
	print_set(P,R,X)
	"""
	print ("pivot u : ", u)
	print ("will itereting over ", p)
	"""
	for node in p:
		#print ("looking node :", node, "at level " , depth)	
		p_tmp = inter(P, voisins)
		R.union(ens_u) 
		#print ("prev X :", X , " inter ", voisins ,)
		x_tmp = inter(X, voisins)
		#print ("next X : ", x_tmp)
		BronKerbosch(p_tmp, R, x_tmp, G, depth+1)
	
		P.discard(u)
		prev_len = len(X)
		#print ("prev X", X, "union ", u,)
		X.add(u)
		#print ("next X", X) 
		assert(len(X) == prev_len+1 or len(X) == prev_len)




	
	
