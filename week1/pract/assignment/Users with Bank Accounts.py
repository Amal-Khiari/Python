class BankAccount:
    accounts = []  # Liste au niveau de la classe pour suivre tous les comptes

    def __init__(self, int_rate=0.01, balance=0):
        """
        Constructeur de la classe BankAccount.
        :param int_rate: Taux d'intérêt (par défaut 1%).
        :param balance: Solde initial (par défaut 0).
        """
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)  # Ajoute automatiquement le compte à la liste

    def deposit(self, amount):
        """
        Dépose un montant dans le compte.
        :param amount: Montant à déposer.
        :return: self (pour permettre le chaînage des méthodes).
        """
        self.balance += amount
        return self

    def withdraw(self, amount):
        """
        Retire un montant du compte.
        Si le solde est insuffisant, applique une pénalité de 5$.
        :param amount: Montant à retirer.
        :return: self (pour permettre le chaînage des méthodes).
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5  # Pénalité de 5$
            print("Fonds insuffisants : pénalité de 5$ appliquée.")
        return self

    def display_account_info(self):
        """
        Affiche les informations du compte (solde actuel).
        :return: self (pour permettre le chaînage des méthodes).
        """
        print(f"Solde : ${self.balance}")
        return self

    def yield_interest(self):
        """
        Applique un intérêt au solde si celui-ci est positif.
        :return: self (pour permettre le chaînage des méthodes).
        """
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        """
        Affiche les informations de tous les comptes.
        """
        print("\nInformations de tous les comptes :")
        for account in cls.accounts:
            account.display_account_info()

    def __del__(self):
        """
        Supprime le compte de la liste des comptes lorsqu'il est détruit.
        """
        BankAccount.accounts.remove(self)
        print(f"Compte avec solde ${self.balance} supprimé.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création de deux comptes
    account1 = BankAccount()  # Taux d'intérêt et solde par défaut
    account2 = BankAccount(int_rate=0.02, balance=100)  # Taux d'intérêt de 2% et solde initial de 100$

    # Opérations sur le compte 1 avec chaînage de méthodes
    account1.deposit(100).deposit(50).deposit(200).withdraw(75).yield_interest().display_account_info()

    # Opérations sur le compte 2 avec chaînage de méthodes
    account2.deposit(200).deposit(150).withdraw(50).withdraw(75).withdraw(100).withdraw(200).yield_interest().display_account_info()

    # Affichage des informations de tous les comptes
    BankAccount.print_all_accounts()

    # Suppression d'un compte (pour démontrer la méthode __del__)
    del account1