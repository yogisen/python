s = " Je fais un Mooc sur Python"
class Phrase:
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __iter__(self):
        return IterPhrase(self.mots)

class IterPhrase:
    def __init__ (self, mots):
        self.mots = mots [:]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.mots:
            raise StopIteration
        return self.mots.pop(0)
