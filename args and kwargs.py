class car:
    def __init__(self, **kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']

audi = car(c='red', s=200)
bmw = car(c='black', s=250)

print(audi.speed)
print(audi.color)