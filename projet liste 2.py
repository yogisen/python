# ask to user to enter the movies names
# add movie in one list
# find movies with same name
# organisze movies with alphabetic name (asc order)
# print list
# add nmovies start

again ='o' # continuer
movies_table = []

while again == 'o':
    movie_to_add = input('please enter a movie : ')

    if movie_to_add.lower() in [movie[0].lower() for movie in movies_table]:
        print('{0} in DEJA a table '.format(movie_to_add))
    else:
        note = input(' enter one note on 5 for this movie : ')
        movies_table.append((movie_to_add, note))

    again = input('do you want to continued ? o/n :')
    print('')

movies_table.sort()
print(movies_table)

