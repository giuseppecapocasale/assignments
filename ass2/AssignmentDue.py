import math

class Particle:
    def __init__(self, mass, charge, name, momentum=0.):   #self e' la chiamata a qualunque metodo
                                                             #per rendere un argomento opzionale bisogna dargli un valore di default nella definizione di funzione
        self.mass = mass
        self.charge = charge
        self.name = name                #così non sono read only
        self.momentum = momentum

#vogliamo che l'utente possa accedere a energia, beta, gamma,... con l'operatore dot
#per emulare attributi come se esistessero, usiamo le properties

    @property           #si def una funz che ha un metodo (perché siamo dentro una classe), che ha il nome dell'attrib che vogliamo emulare (energia)
    def energy(self):
        return math.sqrt(self.mass**2 + self.momentum**2)
    
    @energy.setter
    def energy(self, energy):       #gli devo passare il valore che sto settando (energia)
        if energy < self.mass:
            print("Particle's energy can not be lower then its own mass!")
        else:
            self.momentum =math.sqrt(energy**2 - self.mass**2)  #devo cambiare l'impulso, perché è ciò che esiste come variabile


    @property
    def beta(self):
        return self.momentum/self.energy       #perché non energy?
    
    @beta.setter
    def beta(self, beta):
        if (beta < 0) or (beta > 1):
            print("Values of beta lowerthan 0 or greater than 1 are non physical!")
        elif (beta >= 1.) and (self.mass <= 0.):
            print("Cannot set beta = 1 for a massive particle!")
        else:
            self.momentum = beta * self.energy

    def print_info(self):
        print(f"Particle: {self.name} of mass {self.mass} MeV and charge {self.charge}|e|")
        print(f"The particle momentum is {self.momentum} MeV")

if __name__ == '__main__':
    muon = Particle(mass=105.6, charge=-1, name='Muon', momentum=100)    #se non si mette l'impulso la macchina considera il valore di default
    print(f"Muon energy = {muon.energy} MeV")
    muon.energy = 50        #errore!
    muon.energy = 200
    print(f"Muon energy = {muon.energy} MeV")
    muon.print_info()
    muon.momentum = 20
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    muon.energy = 200
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    print()
#input()     #la macchina legge il codice fino a qua
#Bisogna fare la stessa cosa per le partecelle Alfa e i Protoni





#Fin qui tutto bene. Tra le specifiche, tuttavia, è richiesto che la massa, la carica,... siano read only; serve anche verificare che l'utente non setti l'impulso minore di zero
#Allora "self.mass", "self.charge",... devono diventare PRIVATE e successivamente bisogna "setterarle"

class Particle:
    def __init__(self, mass, charge, name, momentum=0.):
        self._mass = mass
        self._charge = charge
        self._name = name                
        self._momentum = momentum

#Le variabili posso rendere private dopo perché il decoratore "@property" mi salva tutto il codice precedente

    @property
    def mass(self):
        return self._mass
    
    @property
    def charge(self):
        return self._charge
    
    @property
    def name(self):
        return self._name
    
    @property
    def momentum(self):     #ora sono read only perché non hanno un setter
        return self._momentum
    
    @property
    def energy(self):
        return math.sqrt(self._mass**2 + self._momentum**2)
    
    @energy.setter
    def energy(self, energy):
        if energy < self._mass:
            print("Particle's energy can not be lower then its own mass!")
        else:
            self._momentum =math.sqrt(energy**2 - self._mass**2)

    @property
    def beta(self):
        return self.momentum/self.energy
    
    @beta.setter
    def beta(self, beta):
        if (beta < 0) or (beta > 1):
            print("Values of beta lowerthan 0 or greater than 1 are non physical!")
        elif (beta >= 1.) and (self.mass <= 0.):
            print("Cannot set beta = 1 for a massive particle!")
        else:
            self.momentum = beta * self.energy

    def print_info(self):
        print(f"Particle: {self.name} of mass {self.mass} MeV and charge {self.charge}|e|")
        print(f"The particle momentum is {self.momentum} MeV")

if __name__ == '__main__':
    muon = Particle(mass=105.6, charge=-1, name='Muon', momentum=100)    #se non si mette l'impulso la macchina considera il valore di default
    print(f"Muon energy = {muon.energy} MeV")
    muon.energy = 50        #errore!
    print(f"Muon energy = {muon.energy} MeV")
    muon.print_info()
    #muon.momentum = 20      #errore!: propety "momentum" pf "Particle" object has no setter
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    #muon.energy = 200       #errore!: propety "momentum" pf "Particle" object has no setter
    muon.energy = 200
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    print()
    





#Potrei anche mettere un setter e farmi printare che la massa (es.) non può essere cambiata

class Particle:
    def __init__(self, mass, charge, name, momentum=0.):
        self._mass = mass
        self._charge = charge
        self._name = name      
        if momentum < 0:
            print("Cannot set the momentum lower than 0!")          
        self._momentum = momentum

    @property
    def mass(self):
        return self._mass       #perché non return mass?
    
    @mass.setter
    def mass(self, mass):
        if mass < 0:
            print("Cannot set the mass lower than 0!")
        self._mass = mass

    @property
    def charge(self):
        return self._charge
    
    @property
    def name(self):
        return self._name
    
    @property
    def momentum(self):     #ora sono read only perché non hanno un setter
        return self._momentum
    
    @momentum.setter
    def momentum(self, momentum):
        if momentum < 0:
            print("Cannot set the momentum lower than 0!")
            print("Muon momentum will be set to 0 instead:")
            self._momentum = 0
        else:
            self._momentum = momentum

    @property
    def energy(self):
        return math.sqrt(self._mass**2 + self._momentum**2)
    
    @energy.setter
    def energy(self, energy):
        if energy < self._mass:
            print("Particle's energy can not be lower then its own mass!")
        else:
            self._momentum =math.sqrt(energy**2 - self._mass**2)

    @property
    def beta(self):
        return self.momentum/self.energy
    
    @beta.setter
    def beta(self, beta):
        if (beta < 0) or (beta > 1):
            print("Values of beta lowerthan 0 or greater than 1 are non physical!")
        elif (beta >= 1.) and (self.mass <= 0.):
            print("Cannot set beta = 1 for a massive particle!")
        else:
            self.momentum = beta * self.energy

    def print_info(self):
        print(f"Particle: {self.name} of mass {self.mass} MeV and charge {self.charge}|e|")
        print(f"The particle momentum is {self.momentum} MeV")

if __name__ == '__main__':
    muon = Particle(mass=105.6, charge=-1, name='Muon', momentum=100)    #se non si mette l'impulso la macchina considera il valore di default
    muon.mass = -1
    print(f"Muon energy = {muon.energy} MeV")
    muon.energy = 50        #errore!
    muon.energy = 200
    print(f"Muon energy = {muon.energy} MeV")
    muon.print_info()
    muon.momentum = 20      #errore!: propety "momentum" pf "Particle" object has no setter
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    muon.momentum = -1
    muon.energy = 200       #errore!: propety "momentum" pf "Particle" object has no setter
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    print()
    



#Aggiungiamo Alfa e Protoni


class Particle:
    def __init__(self, mass, charge, name, momentum=0.):
        self._mass = mass
        self._charge = charge
        self._name = name      
        self._momentum = momentum

    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, mass):
        if mass < 0:
            print("Cannot set the mass lower than 0! It will be set to zero instead:")
            self._mass = 0.
        else:
            self._mass = mass


    @property
    def charge(self):
        return self._charge
    
    @property
    def name(self):
        return self._name
    
    @property
    def momentum(self):     #ora sono read only perché non hanno un setter
        return self._momentum

    @momentum.setter
    def momentum(self, momentum):
        if momentum < 0:
            print("Cannot set the momentum lower than 0! It will be set to 0 instead:")
            self._momentum = 0.
        else:
            self._momentum = momentum


    @property
    def energy(self):
        return math.sqrt(self._mass**2 + self._momentum**2)
    
    @energy.setter
    def energy(self, energy):
        if energy < self._mass:
            print("Particle's energy can not be lower then its own mass!")
        else:
            self._momentum =math.sqrt(energy**2 - self._mass**2)

    @property
    def beta(self):
        return self.momentum/self.energy
    
    @beta.setter
    def beta(self, beta):
        if (beta < 0) or (beta > 1):
            print("Values of beta lower than 0 or greater than 1 are non physical!")
        elif (beta >= 1.) and (self.mass <= 0.):
            print("Cannot set beta = 1 for a massive particle!")
        else:
            self.momentum = beta * self.energy

    def print_info(self):
        print(f"Particle: {self.name} of mass {self.mass} MeV, charge {self.charge}|e|, momentum {self.momentum} MeV.")





class Proton(Particle):

    MASS = 938.     #MeV
    CHARGE = +1
    NAME = "Proton"

    def __init__(self, momentum=0.):
        Particle.__init__(self, mass=Proton.MASS, charge=Proton.CHARGE, name=Proton.NAME, momentum=momentum)





if __name__ == '__main__':

    muon = Particle(mass=105.6, charge=-1, name='Muon', momentum=100)    #se non si mette l'impulso la macchina considera il valore di default
    muon.print_info()
    print()

    #muon.mass = -1
    #muon.print_info()
    #print()

    muon.energy = 50        #errore!
    print()

    muon.energy = 200
    muon.print_info()
    print()
    print()

    muon.momentum = 20   
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    print()

    muon.momentum = -1
    muon.print_info()
    print()
    
    muon.energy = 200   
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    