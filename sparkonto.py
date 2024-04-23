from konto import Konto


class Sparkonto (Konto):
    def __init__(self, inhaber, kreditInst, kontostand, zinssatz) -> None:
        super().__init__(inhaber, kreditInst, kontostand)
        self.__zinssatz = zinssatz

    def auszahlen(self, betrag: float) -> bool:
        if betrag <= self._kontostand:
            self._kontostand -= betrag
            return True
        else:
            return False

    def __str__(self):
        return self._inhaber + ' : ' + self._kreditInst + ' : ' + str(self._kontostand) + ' : ' + str(self.__zinssatz)
