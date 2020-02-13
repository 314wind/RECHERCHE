   
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
    
    print ("DEBUG :")
    print_set(P, noeuds, X)
    
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
	print ("====track==== : \nR:",)
	print ("{",)
	print (R ,"}",)
	print ("\tP:",)
	print ("{",)
	print (P ,"}",)
	print ("\tX:",)
	print ("{",)
	print (X, "}")
	print ("\n//")
    
    
#algo de recherche de clique maximale
# 
def BronKerbosch(P, R, X):
	#print_set(P,R,X)
	if (len(P)== 0 and len(X)==0): #ens. vide
		print ("Clique found : ")
		#print_set({}, R, {})
		return R #clique maximale
	
	u = pivot(P,X)	#noeud pivot
	#print "pivot u : ", u
	p = P.difference(u.voisins) # P \ voisins(u)
	print ("P :")
	print_set(P, {}, {})
	print ("u.voisins")
	print_set(u.voisins, {}, {})
	print ("p")
	print_set(p, {}, {})

	assert(len(p) < len(P))

	for node in p:
		
		p_tmp = inter(P, u.voisins)
		R.add(u)
		x_tmp = inter(X, u.voisins)
		
		BronKerbosch(p_tmp, R, x_tmp)
	
		P.discard(u)
		X.add(u)




	
	
