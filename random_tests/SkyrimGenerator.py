# Skyrim Class and/or Name Generator

import random

warrior = ["warrior", "berzerker", "reaver"]
one_handed = ["sword", "axe", "mace", "dagger"]
two_handed = ["great sword", "great axe", "great hammer"]
w_weapon_types = [one_handed, two_handed]
mage = ["pure mage", "battle mage"]
primary_schools = ["destruction", "conjuration"]
second_schools = ["restoration", "alteration", "illusion"]
rogue = ["thief", "assassin", "ranger"]
r_weapon_types = [one_handed, "bows"]
light_or_heavy = ("light", "heavy")
primary_classes = [warrior, mage, rogue]
sec_rand = random.SystemRandom()


def choose_primary_class():
	return sec_rand.choice(primary_classes)


def warrior_sub_weapons(wsub):
	if wsub == "warrior":
		prim = sec_rand.choice(one_handed)+" and "+"shield"
		return prim
	elif wsub == "berzerker":
		return "a "+sec_rand.choice(two_handed)
	elif wsub == "reaver":
		prim1 = sec_rand.choice(one_handed)
		prim2 = sec_rand.choice(one_handed)
		if prim1 == prim2:
			return "two "+prim1+"s"
		else:
			return prim1 + " and " + prim2


def mage_sub_weapons(msub):
	if msub == "pure mage":
		primary = sec_rand.choice(primary_schools)
		secondary = sec_rand.choice(second_schools)
		weap = primary + " and " + secondary + " magic"
		return weap
	elif msub == "battle mage":
		ch = [one_handed, primary_schools]
		prim = sec_rand.choice(ch)
		if prim == one_handed:
			primary = "a "+sec_rand.choice(prim)
			secondary = sec_rand.choice(second_schools) + " magic"
		elif prim == primary_schools:
			primary = sec_rand.choice(prim) + " magic"
			ch = ["shield", second_schools]
			sec = sec_rand.choice(ch)
			if sec == "shield":
				secondary = "a shield"
			else:
				secondary = sec_rand.choice(second_schools)+" magic"
		weap = primary + " and " + secondary
		return weap


def rogue_sub_weapons(rsub):
	if rsub == "thief":
		return "a dagger"
	elif rsub == "assassin":
		weap = sec_rand.choice(one_handed)
		if weap == "axe":
			return "an "+weap
		else:
			return "a "+weap
	elif rsub == "ranger":
		return "a bow"


def choose_sub_class(prim_class):
	return sec_rand.choice(prim_class)


def choose_sub_weapons(sub):
	if sub == "warrior" or sub == "berzerker" or sub == "reaver":
		return warrior_sub_weapons(sub)
	elif sub == "pure mage" or sub == "battle mage":
		return mage_sub_weapons(sub)
	elif sub == "thief" or sub == "assassin" or sub == "ranger":
		return rogue_sub_weapons(sub)


def armor_type():
	return sec_rand.choice(light_or_heavy) + " armour"


def print_roll(p_name, p_race, p_class, p_weapons, p_armour):
	if p_class == "assassin":
		article = " an "
	else:
		article = " a "
	print("Thy name be "+p_name+" and ye be"+article+p_race+" "+p_class+", wearing "+p_armour+" and wielding "+p_weapons+".")


lines = open("SkyrimRaces.txt").readlines()
line = lines[0]
races = line.split()
race = sec_rand.choice(races)

# name = sec_rand.choice(names)
name = "Prisoner"
primary_class = choose_primary_class()
sub_class = choose_sub_class(primary_class)
armour = armor_type()
weapons = choose_sub_weapons(sub_class)

print_roll(name, race, sub_class, weapons, armour)
