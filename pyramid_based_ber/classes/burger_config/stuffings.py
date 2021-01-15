class Stuffings(object):
    def __init__(self, stuffings: list):
        self.stuffings = stuffings

    def __str__(self):
        representation = ''
        for stuffing in self.stuffings:
            representation = representation.__add__(stuffing.__str__() + ', ')
        representation = representation[:len(representation) - 2]
        return representation
