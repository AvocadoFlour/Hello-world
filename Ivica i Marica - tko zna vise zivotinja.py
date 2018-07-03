Marica = []
Ivica = []
bodovi_marica = 0
bodovi_ivica = 0

def igra (Marica, Ivica):
    Marica = input('Maričine životinje odvojene razmakom')
    Marica = Marica.split()
    Ivica = input('Ivičine životinje odvojene razmakom')
    Ivica = Ivica.split()
    jedinstvene_vrijednost(Marica, Ivica)

def jedinstvene_vrijednost (Marica, Ivica):
    marica_set = set(Marica)
    ivica_set = set(Ivica)
    Marica = list(marica_set)
    Ivica = list(ivica_set)
    ubojica_marice(Marica, Ivica)

def ubojica_marice (Marica, Ivica):
    penalty = 0
    for i in range(0, len(Marica)):
        for a in range (0, len(Ivica)):
           if Marica[i] == Ivica[a]:
               penalty+=1
    bodovi_marica = len(Marica) - penalty
    bodovi_ivica = len(Ivica) - penalty
    if bodovi_ivica == bodovi_marica:
        print('Neriješeno')
    elif bodovi_ivica > bodovi_marica:
        print('Ivica')
    else:
        print('Marica')

igra (Marica, Ivica)