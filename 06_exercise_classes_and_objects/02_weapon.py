class Weapon:

    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        # if there are bullets in the weapon reduce them by -1 and return message 'shooting'
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        # if there are no bullets return 'no bullets left'
        else:
            return "no bullets left"

    def __repr__(self):  # dunder method (only implement in class)
        # returns remaining bullets
        return f"Remaining bullets: {self.bullets}"


# object

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
