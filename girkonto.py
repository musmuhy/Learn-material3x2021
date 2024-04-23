from konto import Konto


class Girokonto (Konto):
    def __init__(self, inhaber, kreditInst, kontostand, dispo) -> None:
        super().__init__(inhaber, kreditInst, kontostand)
        self.__dispo = dispo

    def auszahlen(self, betrag: float) -> bool:
        if betrag <= self._kontostand + self.__dispo:
            self._kontostand -= betrag
            return True
        else:
            return False

    def __str__(self):
        return self._inhaber + ' : ' + self._kreditInst + ' : ' + str(self._kontostand) + ' : ' + str(self.__dispo)
