#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math

class           Values:
    user_input = 0
    NewArithAvg = 0
    
    def         __init__(self):
        self

    def         setValues(self, nbr_mesures, arith_avg, harmo_avg, ec_type):
        self.NbrMesures = nbr_mesures
        self.ArithAvg = arith_avg
        self.HarmoAvg = harmo_avg
        self.EcType = ec_type

    def         chooseLangage(self):
        langage_input = input("Vælg sprog :\nChoisissez votre langue : (dansk/français)\n")
        if langage_input == 'français':
            self.langage = 'fr'
        elif langage_input == 'dansk':
            self.langage = 'dk'
        else:
            print("Default language is \"dansk\"")
            self.langage = 'dk'

    def         print_data(self):
        if self.langage == 'dk':
            print("\tantal malinder :\t%d" % self.NbrMesures)
            print("\tstandardafvilgelse :\t%.2f" % self.EcType)
            print("\taritmetisk gennemsnit :\t%.2f" % self.ArithAvg)
            print("\tkvadratisk gennemsnit :\t%.2f" % self.QuadraAvg)
            print("\tharmonisk gennemsnit :\t%.2f\n" % self.HarmoAvg)
        elif self.langage == 'fr':
            print("\tNombre de mesures :\t%d" % self.NbrMesures)
            print("\tEcart-type :\t\t%.2f" % self.EcType)
            print("\tMoyenne arithmétique :\t%.2f" % self.ArithAvg)
            print("\tMoyenne quadratique :\t%.2f" % self.QuadraAvg)
            print("\tMoyenne harmonique :\t%.2f\n" % self.HarmoAvg)

    def         standard_deviation(self):
        res = (((pow(self.EcType, 2) + pow(self.ArithAvg, 2)) * self.NbrMesures) + pow(self.user_input, 2)) / (self.NbrMesures + 1)
        res = res - pow(self.NewArithAvg, 2)
        res = math.sqrt(res)
        return res

    def         harmonic_average(self):
        res = (self.NbrMesures + 1) / ((1 / self.user_input) + (self.NbrMesures / self.HarmoAvg))
        return res

    def         quadratic_average(self):
        res = ((pow(self.EcType, 2) + pow(self.ArithAvg, 2)) * self.NbrMesures) + pow(self.user_input, 2)
        return math.sqrt(res / (self.NbrMesures + 1))

    def         arithmetic_average(self):
        res = ((self.ArithAvg * self.NbrMesures) + self.user_input) / (self.NbrMesures + 1)
        return res

def             exec_prog(values):
    values.NewArithAvg = values.arithmetic_average()
    values.QuadraAvg = values.quadratic_average()
    values.EcType = values.standard_deviation()
    values.ArithAvg = values.NewArithAvg
    values.HarmoAvg = values.harmonic_average()
    values.NbrMesures += 1
    values.print_data()
    return 0

def             init(values):
    if values.NbrMesures <= 0 or values.ArithAvg <= 0 or values.HarmoAvg <= 0 or values.EcType <= 0:
        if values.langage == 'fr':
            print("Erreur : tous les paramètres doivent être > 0")
        if values.langage == 'dk':
            print("Fejl: alle parametre skal være > 0")
        return 0
    end_loop = 0
    while end_loop == 0:
        if values.langage == 'fr':
            user_input = input("entrez votre valeur : ")
        elif values.langage == 'dk':
            user_input = input("indtast din vaerdi : ")
        if (user_input == 'ende' and values.langage == 'dk') or (user_input == 'fin' and values.langage == 'fr'):
            end_loop = 1
        elif user_input.isdigit() == True:
            values.user_input = float(user_input)
            exec_prog(values)
    return 0

def             main():
        if len(sys.argv) != 5:
                print("Forkert antal parametre.\nMauvais nombre de paramètres.")
                return 0
        values = Values()
        values.chooseLangage()
        values.setValues(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
        init(values)
        return 0
    
main()
