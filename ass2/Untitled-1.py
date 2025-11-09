import math


class Particle:
    def __init__(self, mass, charge, name, momentum=0.):
        if mass < 0:
            print("Cannot set the mass lower than 0! It will be set to zero instead:")
            self._mass = 0.
        else:
            self._mass = mass
        self._charge = charge
        self._name = name      
        self.momentum = momentum

    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, mass):
        print('The mass attribute is read-only')

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
            raise ValueError("Cannot set the momentum lower than 0! It will be set to 0 instead:")
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

    muon.mass = -1
    muon.print_info()
    print()

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

    #muon.momentum = -1
    #muon.print_info()
    
    muon.energy = 200   
    print(f"Muon energy = {muon.energy:.2f} MeV, "\
          f"momentum = {muon.momentum:.2f} MeV, "\
            f"beta = {muon.beta:.5f}.")
    