class Hero:
    def __init__(hero, health, name):
        health = 100
        hero.health = health
        hero.name = name
    def damage_a(hero, health, name, dmg_a):
        hero.name = "Arthur"
        hero.health -= dmg_a
        print(f"{hero.name} took {dmg} damage, and now has {hero.health} health.")
    def damage_m(hero, health, name, dmg_m):
        hero.name = "Morgana"
        hero.health -= dmg_m
        print(f"{hero.name} took {dmg} damage, and now has {hero.health} health.")

dmg_a = 10
dmg_m = 0
heros = Hero(dmg_a, dmg_m)
heros.damage_a(health, name, dmg_a)
heros.damage_m(health, name, dmg_m)
