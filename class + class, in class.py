class Fruit:
    def __init__(self, bitter, sweet, juicy, ripe ):
        self.bitter= bitter
        self.sweet = sweet
        self.juicy = juicy
        self.ripe = ripe

    def bitterness(self):
        return self.bitter

    def sweetness(self):
        return self.sweet

    def juiciness(self):
        return self.juicy

    def ripeness(self):
        return self.ripe

    def fruit_det(self):
        return "\tYour fruit is " \
               "" \
               "" \
               "{} {} {} {} {}"