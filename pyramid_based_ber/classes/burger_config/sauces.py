class Sauces(object):
    def __init__(self, sauces: list):
        self.sauces = sauces

    def __str__(self):
        representation = ''
        for sauce in self.sauces:
            representation = representation.__add__(sauce.__str__() + ', ')
        representation = representation[:len(representation) - 2]
        return representation
