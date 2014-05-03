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

/* Le grep c'est pas bien, j'espère que vous serez sanctionné ! */

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

def             print_data(ec_type, arith_avg, quadra_avg, harmo_avg):
    print("\tantal malinder :\t%d" % nbr_mesures)
    print("\tstandardafvilgelse :\t%.2f" % ec_type)
    print("\taritmetisk gennemsnit :\t%.2f" % arith_avg)
    print("\tkvadratisk gennemsnit :\t%.2f" % quadra_avg)
    print("\tharmonisk gennemsnit :\t%.2f\n" % harmo_avg)

def             exec_prog(user_input):
    global new_arith_avg, ec_type, arith_avg, quadra_avg, harmo_avg, nbr_mesures
    new_arith_avg = arithmetic_average(user_input)
    quadra_avg = quadratic_average(user_input)
    ec_type = standard_deviation(user_input)
    arith_avg = new_arith_avg
    harmo_avg = harmonic_average(user_input)
    nbr_mesures += 1
    print_data(ec_type, arith_avg, quadra_avg, harmo_avg)
    return 0

def             init():
    if nbr_mesures <= 0 or arith_avg <= 0 or harmo_avg <= 0 or ec_type <= 0:
        print "Error : all the parameters must be > 0"
        return 0
    end_loop = 0
    while end_loop == 0:
        user_input = raw_input("indtast din vaerdi : ")
        if user_input == 'ende':
            end_loop = 1
        elif user_input.isdigit() == True:
            user_input = float(user_input)
            exec_prog(user_input)
    return 0

def             main():
    if len(sys.argv) != 5:
        print "Wrong number of parameters."
        return 0
    global nbr_mesures, arith_avg, harmo_avg, ec_type
    nbr_mesures = float(sys.argv[1])
    arith_avg = float(sys.argv[2])
    harmo_avg = float(sys.argv[3])
    ec_type = float(sys.argv[4])
    init()
    return 0
    
main()
