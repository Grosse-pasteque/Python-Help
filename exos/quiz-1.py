# Sans executer ce programme:
# trouver ce qu'affiche chaque print
# à chaque question


liste = [1, 2, 3, 4]


# question 1
print(isinstance(liste, list))


# question 2
liste.append(5)
print(liste)


# question 3
liste.remove(3)
print(liste)


# question 4
print(liste[liste.index(4)])


# question 5
print(int(str(liste)[:].split(', ')[2])**2-1)


# question 6
print('hey:', str(sum(liste)**2), '!')


# question 7
print(liste.pop(0))