#	File: RPG.py
#	Description: This program determines the outcome of a battle between two characters.
#	Student's Name: Christina Hoang
#	Student's UT EID: ch42297
#	Course Name: CS 313E
#	Unique Number: 86940
#
#	Date Created: 6/9/2017
#	Date Last Modified: 6/14/2017

# create weapon class
class Weapon():

	def __init__(self, type):
		self.type = type

	# string method
	def __str__(self):
		return (str(self.type))

	# damage points method
	def damage(self):
		if self.weapon == "dagger":
			return(4)
		elif self.weapon == "axe":
			return(6)
		elif self.weapon == "staff":
			return (6)
		elif self.weapon == "sword":
			return(10)
		elif self.weapon == "none":
			return(1)

# create armor class
class Armor():

	def __init__(self, type):
		self.type = type

	# string method
	def __str__(self):
		return (str(self.type))

	# armor class method
	def protection(self):
		if self.armor == "plate":
			return(2)
		elif self.armor == "chain":
			return(5)
		elif self.armor == "leather":
			return(8)
		elif self.armor == "none":
			return(10)

# create character class
class RPGCharacter():

	# initialize health, spell points, armor and weapon for all characters
	health = 0
	spellPoints = 0

	def __init__(self, name):
		self.name = name
		self.armor = "none"
		self.weapon = "none"

	# put on armor method
	def putOnArmor(self, armor):
		self.armor = str(armor)
		if self == Wizard:
			print("Armor not allowed for this character class.")
		else:
			print(self.name," is now wearing a(n) ",self.armor)
	
	# take off armor method
	def takeOffArmor(self, armor):
		self.armor = "none"
		print(self.name," is no longer wearing anything.")
	
	# wield weapon method
	def wield(self, weapon):
		# wizards cannot wield weapons
		self.weapon = str(weapon)
		if self == Wizard:
			print("Weapon not allowed for this character class")
		else:
			print(self.name," is now wielding a(n) ",self.weapon)

	# unwield weapon method
	def unwield(self, armor):
		self.weapon = "none"
		print(self.name," is no longer wielding anything.")

	# fight method
	def fight(self, opponent):
		print(self.name," attacks ",opponent.name," with a(n) ",self.weapon)
		opponent.health -= Weapon.damage(self)
		print(self.name," does ",Weapon.damage(self)," damage to ",opponent.name)
		print(opponent.name," is now down to ",str(opponent.health)," health")

		RPGCharacter.checkForDefeat(opponent)

	# check for defeat method
	def checkForDefeat(self):
		if self.health <= 0:	
			print(self.name,"has been defeated!")

	# show method
	def show(self):
		print("\n")
		print(self.name)
		print("  Current Health: ",self.health)
		print("  Current Spell Points: ",self.spellPoints)
		print("  Wielding: ",self.weapon)
		print("  Wearing: ",self.armor)
		print("  Armor Class: ",str(Armor.protection(self)))
		print("\n")

# create fighter subclass
class Fighter(RPGCharacter):

	# initialize for all fighters
	health = 40

	def __init__(self, name):
		self.name = name
	
	# string method
	def __str__(self):
		return(str(self.name))

# create wizard subclass
class Wizard(RPGCharacter):

	# initialize for all wizards
	health = 16
	spellPoints = 20

	def __init__(self, name):
		self.name = name
		self.spell = "none"
		self.armor = "none"
		self.spellCost = 0
		self.spellEffect = 0
		

	# cast spell method
	def castSpell(self, spell, opponent):
		self.spell = str(spell)
		if self.spellPoints >= 3:
			if self.spell == "Fireball":
				self.spellCost = 3
				self.spellEffect = 5
				self.spellPoints -= self.spellCost
				opponent.health -= self.spellEffect
			elif self.spell == "Lightning Bolt":
				self.spellCost = 10
				self.spellEffect = 10
				self.spellPoints -= self.spellCost
				opponent.health -= self.spellEffect
			elif self.spell == "Heal":
				self.spellCost = 6
				self.spellEffect = 6
				self.spellPoints -= self.spellCost
				opponent.health += self.spellEffect

			else:
				print("Unknown spell name. Spell failed.")
		else:
			print("Insufficient spell points")

		# check that health doesn't exceed maximum
		if opponent == "Wizard":
			if opponent.health > 16:
				opponent.health = 16
			elif self.spell == "Heal":
				print(self.name," casts ",self.spell," at ",opponent.name)
				print(self.name," heals ",opponent.name, " for ",self.spellCost," health points")
				print(opponent.name," is now at ",opponent.health," health")
			else:
				print(self.name," casts ",self.spell," at ",opponent.name)
				print(self.name," does ",self.spellEffect," damage to ",opponent.name)
				print(opponent.name," is now down to ",opponent.health," health")
		else:
			if opponent.health > 40:
				opponent.health = 40
			elif self.spell == "Heal":
				print(self.name," casts ",self.spell," at ",opponent.name)
				print(self.name," heals ",opponent.name, " for ",self.spellCost," health points")
				print(opponent.name," is now at ",opponent.health," health")
			else:
				print(self.name," casts ",self.spell," at ",opponent.name)
				print(self.name," does ",self.spellEffect," damage to ",opponent.name)
				print(opponent.name," is now down to ",opponent.health," health")			
	
def main():

	chainMail = Armor("chain")
	sword = Weapon("sword")
	staff = Weapon("staff")
	axe = Weapon("axe")

	harry = Wizard("Harry Potter")
	harry.wield(staff)

	aragorn = Fighter("Aragorn")
	aragorn.putOnArmor(chainMail)
	aragorn.wield(axe)

	harry.show()
	aragorn.show()

	harry.castSpell("Fireball",aragorn)
	aragorn.fight(harry)

	harry.show()
	aragorn.show()

	harry.castSpell("Lightning Bolt",aragorn)
	aragorn.wield(sword)

	harry.show()
	aragorn.show()

	harry.castSpell("Heal",harry)
	aragorn.fight(harry)

	harry.fight(aragorn)
	aragorn.fight(harry)

	harry.show()
	aragorn.show()

main()