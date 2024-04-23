class Konto:
    def __init__(self, inhaber, kreditInst, kontostand) -> None:
        self._inhaber = inhaber
        self._kreditInst = kreditInst
        self._kontostand = kontostand

    def einzahlen(self, betrag: float) -> None:
        self._kontostand += betrag

    def get_inhaber(self):
        return self._inhaber
