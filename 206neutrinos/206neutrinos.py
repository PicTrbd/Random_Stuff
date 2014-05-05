#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import calc

def             exec_prog(values):
    values.NewArithAvg = values.arithmetic_average()
    values.QuadraAvg = values.quadratic_average()
    values.EcType = values.standard_deviation()
    values.ArithAvg = values.NewArithAvg
    values.HarmoAvg = values.harmonic_average()
    values.NbrMesures += 1
    values.print_data()
    values.add_to_history()
    return 0

def             parsing_command(values):
    if values.langage == 'fr':
        user_input = input("entrez votre valeur : ")
    elif values.langage == 'dk':
        user_input = input("indtast din vaerdi : ")
    if (user_input == 'ende' and values.langage == 'dk') or \
    (user_input == 'fin' and values.langage == 'fr'):
        return 1
    elif (user_input == 'historisk' and values.langage == 'dk') or \
    (user_input == 'historique' and values.langage == 'fr'):
        values.history()
    elif (user_input == 'historisk -c' and values.langage == 'dk') or \
    (user_input == 'historique -c' and values.langage == 'fr'):
        values.history_clear()
    elif user_input == 'fr':
        values.langage = 'fr'
    elif user_input == 'dk':
        values.langage = 'dk'
    elif user_input.isdigit() == True:
        values.user_input = float(user_input)
        exec_prog(values)
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
        end_loop = parsing_command(values)
    return 0

def             main():
        if len(sys.argv) != 5:
            print("Forkert antal parametre.\nMauvais nombre de paramètres.")
            return 0
        values = class_test.Values()
        values.chooseLangage()
        values.setValues(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
        init(values)
        return 0
    
main()
