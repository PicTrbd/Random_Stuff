#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math

nbr_mesures = 0
arith_avg = 0
harmo_avg = 0
quadra_avg = 0
ec_type = 0
new_arith_avg = 0

def             standard_deviation(user_input):
    res = (((pow(ec_type, 2) + pow(arith_avg, 2)) * nbr_mesures) + pow(user_input, 2)) / (nbr_mesures + 1)
    res = res - pow(new_arith_avg, 2)
    res = math.sqrt(res)
    return res

def             harmonic_average(user_input):
    res = (nbr_mesures + 1) / ((1 / user_input) + (nbr_mesures / harmo_avg))
    return res

def             quadratic_average(user_input):
    res = ((pow(ec_type, 2) + pow(arith_avg, 2)) * nbr_mesures) + pow(user_input, 2)
    return math.sqrt(res / (nbr_mesures + 1))

def             arithmetic_average(user_input):
    res = ((arith_avg * nbr_mesures) + user_input) / (nbr_mesures + 1)
    return res

def             print_data(langage):
    if langage == 'dk':
        print("\tantal malinder :\t%d" % nbr_mesures)
        print("\tstandardafvilgelse :\t%.2f" % ec_type)
        print("\taritmetisk gennemsnit :\t%.2f" % arith_avg)
        print("\tkvadratisk gennemsnit :\t%.2f" % quadra_avg)
        print("\tharmonisk gennemsnit :\t%.2f\n" % harmo_avg)
    elif langage == 'fr':
        print("\tNombre de mesures :\t%d" % nbr_mesures)
        print("\tEcart-type :\t\t%.2f" % ec_type)
        print("\tMoyenne arithmétique :\t%.2f" % arith_avg)
        print("\tMoyenne quadratique :\t%.2f" % quadra_avg)
        print("\tMoyenne harmonique :\t%.2f\n" % harmo_avg)

def             exec_prog(user_input, langage):
    global new_arith_avg, ec_type, arith_avg, quadra_avg, harmo_avg, nbr_mesures
    new_arith_avg = arithmetic_average(user_input)
    quadra_avg = quadratic_average(user_input)
    ec_type = standard_deviation(user_input)
    arith_avg = new_arith_avg
    harmo_avg = harmonic_average(user_input)
    nbr_mesures += 1
    print_data(langage)
    return 0

def             init(langage):
    if nbr_mesures <= 0 or arith_avg <= 0 or harmo_avg <= 0 or ec_type <= 0:
        if langage == 'fr':
            print("Erreur : tous les paramètres doivent être > 0")
        if langage == 'dk':
            print("Fejl: alle parametre skal være> 0")
        return 0
    end_loop = 0
    while end_loop == 0:
        if langage == 'fr':
            user_input = input("entrez votre valeur : ")
        elif langage == 'dk':
            user_input = input("indtast din vaerdi : ")
        if (user_input == 'ende' and langage == 'dk') or (user_input == 'fin' and langage == 'fr'):
            end_loop = 1
        elif user_input.isdigit() == True:
            user_input = float(user_input)
            exec_prog(user_input, langage)
    return 0

def             main():
        if len(sys.argv) != 5:
                print("Forkert antal parametre.\nMauvais nombre de paramètres.")
                return 0
        global nbr_mesures, arith_avg, harmo_avg, ec_type
        nbr_mesures = float(sys.argv[1])
        arith_avg = float(sys.argv[2])
        harmo_avg = float(sys.argv[3])
        ec_type = float(sys.argv[4])
        langage_input = input("Vælg sprog :\nChoisissez votre langue : (dansk/français)\n")
        if langage_input == 'français':
            langage = 'fr'
        elif langage_input == 'dansk':
            langage = 'dk'
        else:
            print("Default language is \"dansk\"")
            langage = 'dk'
        init(langage)
        return 0
    
main()
