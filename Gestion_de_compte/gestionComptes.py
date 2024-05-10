class CompteBancaire:
  def __init__(self, numero_compte:int, nom:str, solde:float):
    self.numero_compte: int = numero_compte
    self.nom: str= nom
    self.__solde: float = solde

  def versement(self, montant:float):
    self.__solde += montant

  def afficher_info(self):
    print(f"Non: {self.nom}, Numero de compte: {self.numero_compte}, Solde: {self.__solde}")

  def retrait(self, montant:float):
    if(montant <= self.__solde):
      self.__solde -= montant
    else:
      print("Vous ne pouvez pas faire de retrait. Solde Insuffisant")

  def agios(self):
    taxe = (5 * self.__solde) /100
    self.__solde -= taxe



client1 = CompteBancaire(1, "Kouadio", 10000 )

client1.afficher_info()
client1.versement(2500.59)
client1.afficher_info()
client1.retrait(5000)
client1.afficher_info()
client1.retrait(15000)
client1.agios()
client1.afficher_info()