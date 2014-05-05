import math
import sys

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
        self.BaseNbrMesures = nbr_mesures
        self.BaseArithAvg = arith_avg
        self.BaseHarmoAvg = harmo_avg
        self.BaseEcType = ec_type

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
            print("\tkvadratisk gennemsnit : %.2f" % self.QuadraAvg)
            print("\tharmonisk gennemsnit :\t%.2f\n" % self.HarmoAvg)
        elif self.langage == 'fr':
            print("\tNombre de mesures :\t%d" % self.NbrMesures)
            print("\tEcart-type :\t\t%.2f" % self.EcType)
            print("\tMoyenne arithmétique :\t%.2f" % self.ArithAvg)
            print("\tMoyenne quadratique :\t%.2f" % self.QuadraAvg)
            print("\tMoyenne harmonique :\t%.2f\n" % self.HarmoAvg)

    def         add_to_history(self):
        file = open("history", 'a')
        if self.langage == 'dk':
            file.write("Værdigrundlag : " + str(int(self.BaseNbrMesures)) + " " + str(int(self.BaseArithAvg)) + " " + str(int(self.BaseHarmoAvg)) + " " + str(int(self.BaseEcType)))
            file.write("\nVaerdi : " + str(int(self.user_input)))
            file.write("\n\tantal malinder :\t" + str(int(self.NbrMesures)))
            file.write("\n\tstandardafvilgelse :\t" + str(round(self.EcType, 2)))
            file.write("\n\taritmetisk gennemsnit :\t" + str(round(self.ArithAvg)))
            file.write("\n\tkvadrastisk gennemsnit :" + str(round(self.QuadraAvg)))
            file.write("\n\tharmonisk gennemsnit :\t" + str(round(self.HarmoAvg)))
        elif self.langage == 'fr':
            file.write("Valeurs de base : " + str(int(self.BaseNbrMesures)) + " " + str(int(self.BaseArithAvg)) + " " + str(int(self.BaseHarmoAvg)) + " " + str(int(self.BaseEcType)))
            file.write("\nValeur : " + str(int(self.user_input)))
            file.write("\n\tNombre de mesures :\t" + str(int(self.NbrMesures)))
            file.write("\n\tEcart-type :\t\t" + str(round(self.EcType, 2)))
            file.write("\n\tMoyenne arithmétique :\t" + str(round(self.ArithAvg)))
            file.write("\n\tMoyenne quadratique :\t" + str(round(self.QuadraAvg)))
            file.write("\n\tMoyenne harmonique :\t" + str(round(self.HarmoAvg)))
        file.write("\n____________________________\n")
        file.close()

    def         history(self):
        file = open("history", 'r')
        file_str = file.read()
        print(file_str)
        file.close()

    def         history_clear(self):
        file = open("history", 'w').close()

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
