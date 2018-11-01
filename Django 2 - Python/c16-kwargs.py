def capitals(title, ending='', **kwargs):
    print(title)
    for country, capital in kwargs.items():
        print("The capital of {} is {}".format(country, capital))

    if ending:
        print(ending)


capitals("List your countries", 'Goodbye',
         France='Paris', Germany='Berlin')

# extract kwargs as a dictionnary
kwargs = {'France': 'Paris',
          'Germany': 'Berlin'}
capitals("List your countries", **kwargs)
