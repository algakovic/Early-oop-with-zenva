#Python language basics 7 
# Classes and Objects
# Class Fields, methods, and constructors
# Object instantiation

''' code sum entity, state and behaviour
    state represented by Fields and behaviour by methods which 
    are functions inside a class

    We create new instances of object through constructors which
    are a special type of method that help to setup all the different
    fields of a class.
'''

# Example 1: use camelCase for class names
class GameCharacter:

    # speed acting like a global variable here
    speed = 5

    # constructor method creates a new class instance and sets up the defined fields
    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.heigh = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    # first method, just a function that modifies the classes fields
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

# character 0 is a new instance of the GameCharacter class with the defined attributes
character_0 = GameCharacter('Kakarot', 65, 125, 100, 100)

# character_0.name = 'Vegeta'
# print(character_0.name)


# character_0.move(50, 100)
# print(character_0.x_pos)
# print(character_0.y_pos)

# Python language basics 8
'''subclasses superclasses and inheritance session'''

#create a subclass of GameCharacter
# has access to everything defined in #GameCharacter but not
class PlayerCharacter(GameCharacter):

    speed = 10

    # should still provide a constructor/initialiser
    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        super().move(0, by_y_amount)


class NonPlayerCharacter(GameCharacter):

    speed = 3

    def __init__(self, name, x_pos, y_pos):
        super(). __init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_x_amount, by_y_amount):
        super().move(by_x_amount, by_y_amount)
    
npc1 = NonPlayerCharacter('Kame', 200, 15)
print(npc1.name)
npc1.move(2, 1)
print(npc1.y_pos)
print(npc1.x_pos)


player_character = PlayerCharacter('Krillin', 100, 400)

print(player_character.name)
player_character.move(100)
print(player_character.x_pos)
print(player_character.y_pos)








































class fpsWeapon:

    def __init__(self, name, recoil, clipSize, dmg, firingRate, reloadSpeed, drawSpeed):
        self.name = name
        self.recoil = recoil
        self.clipSize = clipSize
        self.dmg = dmg
        self.firingRate = firingRate
        self.reloadSpeed = reloadSpeed
        self.drawSpeed = drawSpeed
        
    def reload(self):
        pass
        
    def shoot(self):
        if self.clipSize > 0:
            self.clipSize -= 1
            if self.recoil == 1:
                self.recoil +=1
            else: self.recoil +=2
        else: reload()
        

fpsWeapon_1 = fpsWeapon('Vandal', 1, 25, 40, 4.6, 3, 2)
print(fpsWeapon_1.name)
print(fpsWeapon_1.recoil)

fpsWeapon_1.shoot()
print(fpsWeapon_1.recoil)
fpsWeapon_1.shoot()
print(fpsWeapon_1.recoil)


