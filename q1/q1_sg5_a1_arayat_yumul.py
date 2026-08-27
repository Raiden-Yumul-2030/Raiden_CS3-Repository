class Hero:
    def __init__(hero, health, name):
        hero.health = health
        hero.name = name
    def damage(hero, dmg):
        hero.health -= dmg
        print(f"{hero.name} took {dmg} dmg and now has {hero.health} health left")

Names = ["Arthur", "Morgana"]
Hero_Damage = [10, 0]
Hero_Health = [100, 100]

for i in range(len(Names)):
    health = Hero_Health[i]
    name = Names[i]
    dmg = Hero_Damage[i]
    heros = Hero(health, name)
    heros.damage(dmg)

