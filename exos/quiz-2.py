# Sans executer ce programme:
# trouver ce qu'affiche chaque print
# à chaque question

dictionnaire = {
	'liste': [1, 3, 4, 5, 6, 7, 8, 9],
	0: None
}


# question 1
print(dictionnaire.keys())


# question 2
print(dictionnaire['liste'])


# question 3
print(dictionnaire[0])


# question 4
print(sum(dictionnaire['liste']))


# question 5
print(dictionnaire['liste'][-1:-1])


# question 6
print(dictionnaire['liste'][::-1])


# question 7
dictionnaire['N'] = str(dictionnaire[0])[-1]
print(dictionnaire['N'])


# question 8
print([i-3 for i in dictionnaire['liste']])


# question 9
print(dictionnaire[1])