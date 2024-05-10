class CompteBancaire:
  list_compte_bancaire = []

  def __init__(self, numero_compte:int, nom:str, solde:float):
    self.numero_compte: int = numero_compte
    self.nom: str= nom
    self.__solde: float = solde
    CompteBancaire.list_compte_bancaire.append(self)


  def versement(self, montant:float):
    self.__solde += montant

  def afficher_info(self):
    print(f"Nom: {self.nom}, Numero de compte: {self.numero_compte}, Solde: {self.__solde}")

  def retrait(self, montant:float):
    if(montant <= self.__solde):
      self.__solde -= montant
    else:
      print("Vous ne pouvez pas faire de retrait. Solde Insuffisant")

  def agios(self):
    taxe = (5 * self.__solde) /100
    self.__solde -= taxe

  @classmethod
  def ajout_compte(cls, compte):
    cls.list_compte_bancaire.append(compte)

  @classmethod
  def afficher_comptes(cls):
    for compte in cls.list_compte_bancaire:
      print(f"Nom: {compte.nom}, Numero de compte: {compte.numero_compte}, Solde: {compte.__solde}")




client1 = CompteBancaire(1, "Kouadio", 10000 )
client2 = CompteBancaire(35, "Yao", 5000 )
client3 = CompteBancaire(25, "Konan", 26800 )

client1.afficher_info()
client1.versement(2500.59)
client1.afficher_info()
client1.retrait(5000)
client1.afficher_info()
client1.retrait(15000)
client1.agios()
client1.afficher_info()
print("********************")
CompteBancaire.afficher_comptes()