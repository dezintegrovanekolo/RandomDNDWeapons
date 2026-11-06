import random

weapons = [ "Club(light)", "Dagger(finesse,light)", "Greatclub(two handed)", "Handaxe(light)", "Javelin", 
            "Lighthammer(light)", "Mace", "Quarterstaff(versatile)", "Sickle(light)", "Spear(versatile)",
            "Battleaxe(versatile)", "Flail", "Glaive(Heavy, reach, two handed)", "Greataxe(heavy, two handed)",
            "halberd(heavy, reach, two handed)", "Lance(reach, special)", "Longsword(versatile(1d10))",
            "Maul(heavy, two handed)", "Morningstar", "Pike(heavy, reach, two handed)", "Rapier(Finesse)", 
            "scimitar(finesse, light)", "Shortsword(finesse, light)", "Trident(versatile(1d8))", "War pick", 
            "Warhammer(versatile(1d8))... seems like its 40K", "Whip(finesse, reach)" ]

damage = [ "1d4", "1d8", "1d6", "1d10", "1d12", "2d6" ]

dmgweighted = random.choices(damage, weights=(7, 6, 9, 2, 1, 2)) #k = (number) EXP: allows me to test multiple times when put into the list

dmgtype = [ "slash", "pierce", "blunt" ]

print(random.choice(weapons))
print(dmgweighted)
print(random.choice(dmgtype))