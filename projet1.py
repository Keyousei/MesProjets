from random import randint, seed
def nom_carte(carte) :	#Assigne le nom traditionnel aux cartes de valeur 1,11,12,13 et imprime la carte piochée.
	if carte == 1 :
		carte = "as"
	elif carte == 11 :
		carte = "valet"
	elif carte == 12 :
		carte = "dame"
	elif carte == 13 :
		carte = "roi"
	return("La carte tiree est : " + str(carte))
def carte_speciale(carte) : 
	if carte > 10 :		#Assigne la valeur de 10 pour le valet, la dame, et le roi.
		carte = 10
	elif carte == 1 :	#Assigne la valeur de 0 pour l'as temporairement.
		carte = 0
	return carte
def calcul_as(carte_as, totale) :	#Calcule si les as doivent valoir 1 ou 11 à l'avantage du joueur.
	if carte_as >= 1 and totale + 11 + 1 * (carte_as - 1) <= 21 :
		return 11 + 1 * (carte_as - 1)
	else :
		return 1 * (carte_as)
print("Bienvenue au Blackjack")
graine = int(input("Entrez la graine : "))	#Permet de rentrer le seed.
seed(graine)
argent = int(input("Veuillez entrer la quantité d'argent en votre possession : "))	#Le joueur indique combien il a d'argent.
jouer = 1	#Lorsque jouer = 1, le joueur veut (re)jouer. Si jouer = 2, le joueur ne veut plus (re)jouer.
while jouer == 1 :	#Tant que le joueur voudra rejouer.
	n_cartes = totale = carte_as = totale_as = Totale = 0	
	piocher = 1	#Lorsque piocher = 1, le joueur voudra (re)piocher. Si piocher = 2, le joueur ne veut plus (re)jouer.
	mise = int(input("Veuillez entrer votre mise (vous avez : " + str(argent) + ") : "))	#Entrée de la valeur de la mise.
	argent -= mise	#Argent de la mise soustraite 
	while Totale < 21 and piocher == 1 :	#Le joueur pioche autant de fois tant qu'il en aura envie et que la valeur totale de sa main est inférieure à 21.
		carte = randint(1,13)	#Carte piochée par le joueur générée pseudo-aléatoirement.
		print(nom_carte(carte))	#Imprime la carte piochée par le joueur.
		carte = carte_speciale(carte)	#Assigne d'autre valeurs pour les cartes "spéciales".
		if carte == 0 :		#Si la carte piochée par le joueur est un as,
			carte_as += 1	#le compteur d'as dans la main du joueur augmente de 1.
		n_cartes += 1		#Le nombre de cartes dans la main du joueur est augmenté de 1.
		totale += carte 	#Rajout de la valeur de la carte piochée dans la valeur actuelle de la main du joueur sans compter les as.
		totale_as = calcul_as(carte_as, totale) #Calcul de la valeur actuelle de tous les as dans la main du joueur.
		Totale = totale + totale_as #Valeur totale de la main du joueur.
		if Totale < 21 :	#Si la valeur totale de la main du joueur est inférieure à 21,
			piocher = int(input("Souhaitez-vous une carte ? (1: oui, 2: non) ")) #demande au joueur s'il veut piocher.
	if Totale > 21 :	#Si la valeur totale de la main du joueur est supérieure à 21.
		print("Vous avez sauté")	#Imprime quel le joueur a sauté et donc a perdu.
	else :
		print("Vous avez obtenu " + str(Totale) + " points")	#Imprime la valeur totale de la main du joueur.
		print("La banque joue :")	#C'est au tour de la banque
		banque_n_cartes = banque_totale = banque_carte_as = banque_totale_as = banque_Totale = 0
		while banque_Totale < 17 :	#Tant que la valeur de sa main est inférieure à 17, la banque continuera à piocher
			banque_carte = randint(1,13)	#Carte piochée par la banque générée pseudo-aléatoirement.
			print(nom_carte(banque_carte))	#Imprime la carte piochée par la banque.
			banque_carte = carte_speciale(banque_carte)	#Assigne d'autre valeurs pour les cartes "spéciales".
			if banque_carte == 0 :		#Si la carte piochée par la banque est un as,
				banque_carte_as += 1	#le compteur d'as dans la main de la banque augmente de 1.
			banque_n_cartes += 1	#Le nombre de cartes dans la main de la banque est augmenté de 1.
			banque_totale += banque_carte 	#Rajout de la valeur de la carte piochée dans la valeur actuelle de la main de la banque sans compter les as.
			banque_totale_as = calcul_as(banque_carte_as, banque_totale)	#Calcul de la valeur actuelle de tous les as dans la main de la banque.
			banque_Totale = banque_totale + banque_totale_as	#Valeur totale de la main de la banque.
		if banque_Totale <= 21 :	#Si la valeur totale de la main de la banque est inférieure ou égale à 21,
			print("La banque a obtenu " + str(banque_Totale) + " points")	#Imprime la valeur totale de la main de banque.
		if Totale > banque_Totale or banque_Totale > 21 or (Totale == banque_Totale and n_cartes == 2 and Totale == 21 and banque_n_cartes > 2)  :	#Conditions de victoires du joueur.
			if banque_Totale > 21 :	#Si la valeure totale de la main de la banque est supérieure à 21,
				print("La banque a sauté")	#imprime que la banque a sauté.
			print("Vous gagnez " + str(mise))	#Imprime que le joueur a gagné, ainsi que la valeur de ses gains.
			argent += mise*2	#Le joueur récupère sa mise, ainsi que son gain.
		elif Totale < banque_Totale or (Totale == banque_Totale and banque_n_cartes == 2 and banque_Totale == 21 and n_cartes > 2) :	#Conditions de défaites du joueur.
			print("La banque gagne")	#Imprime que la banque a gagné
		else :
			print("Égalité")	#Imprime que qu'il y a une égalité entre la banque et le joueur.
			argent += mise		#Le joueur récupère la mise qu'il avait parié.
	jouer = int(input("Souhaitez-vous jouer une autre partie ? (1: oui, 2: non) "))	#Demande au joueur s'il veut rejouer.