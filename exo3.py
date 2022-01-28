from abc import ABC, abstractmethod



class Voiture(ABC):

    rouler = False # Voiture à l'arrêt

    @abstractmethod
    def demarrer(self):
        pass


class Moteur():

    def v8(self):
        print("Accélération puissante")
    
    def calme(self):
        print("Peu bruyant")
    

class Sieges():

    def confort(self):
        print("Siège cuir confort ++")

    def baquet(self):
        print("Sièges de course")

    def bon_marche(self):
        print("On fait ce qu'on peut...")
 

class Jantes():

    def carbone(self):
        print("Réduction de poids")    

    def tole(self):
        print("Le moins cher possible")  

    def alu(self):
        print("Le style avant tout") 


class Vitres():

    def tintees(self):
        print("Vitres tintées")

    def transparentes(self):
        print("Intérieur visible")

class Aileron():

    def competition(self):
        print("Plaquage au sol")

    def aucun(self):
        print("Pas d'aileron")


class Voiture_puissante(Voiture, Moteur, Sieges, Jantes, Vitres, Aileron):
    def demarrer(self):
        self.rouler = True
        self.v8()
        self.baquet()
        self.carbone()
        self.tintees()
        self.competition()
        print("A fond les ballons !")
   
class Voiture_confortable(Voiture, Moteur, Sieges, Jantes, Vitres, Aileron):
    def demarrer(self):
        self.rouler = True
        self.calme()
        self.confort()
        self.alu()
        self.tintees()
        self.aucun()
        print("Confort")

class Voiture_citadine(Voiture, Moteur, Sieges, Jantes, Vitres, Aileron):   
    def demarrer(self):
        self.rouler = True
        self.calme()
        self.bon_marche()
        self.tole()
        self.transparentes()
        self.aucun()
        print("Au moins c'est pas trop cher")

voit = Voiture_puissante()
voit.demarrer()

