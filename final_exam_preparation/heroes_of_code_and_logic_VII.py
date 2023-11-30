
# add the heroes to dicts

number_of_heroes = int(input())
hero_hp = {}
hero_mana = {}

max_hp = 100
max_mana = 200

for hero in range(number_of_heroes):
    line = input().split()
    hero_name, hp, mp = line[0], line[1], line[2]

    # one check
    if hero_name not in hero_hp:
        hero_hp[hero_name] = int(hp)
        hero_mana[hero_name] = int(mp)

# commands with the heores

command = input()
while command != 'End':
    command_info = command.split(" - ")

    instruction = command_info[0]
    hero = command_info[1]

    if instruction == 'CastSpell':
        mp_needed = int(command_info[2])
        spell_name = command_info[3]

        if mp_needed <= hero_mana[hero]:
            hero_mana[hero] -= mp_needed
            print(f'{hero} has successfully cast {spell_name} and now has {hero_mana[hero]} MP!')
        else:
            print(f'{hero} does not have enough MP to cast {spell_name}!')

    elif instruction == 'TakeDamage':
        take_dmg = int(command_info[2])
        attacker = command_info[3]
        hero_hp[hero] -= take_dmg

        if hero_hp[hero] > 0:
            print(f'{hero} was hit for {take_dmg} HP by {attacker} and now has {hero_hp[hero]} HP left!')
        else:
            print(f'{hero} has been killed by {attacker}!')

    elif instruction == 'Recharge':
        recharged_amount = int(command_info[2])
        difference_to_max = max_mana - hero_mana[hero]
        if difference_to_max > recharged_amount:
            hero_mana[hero] += recharged_amount
        else:
            hero_mana[hero] += difference_to_max
            recharged_amount = difference_to_max
        print(f'{hero} recharged for {recharged_amount} MP!')

    elif instruction == 'Heal':
        recovered_amount = int(command_info[2])
        difference_to_max = max_hp - hero_hp[hero]
        if difference_to_max > recovered_amount:
            hero_hp[hero] += recovered_amount
        else:
            hero_hp[hero] += difference_to_max
            recovered_amount = difference_to_max
        print(f'{hero} healed for {recovered_amount} HP!')

    command = input()

for hero in hero_hp:
    if hero_hp[hero] > 0:
        print(f'{hero}')
        print(f' HP: {hero_hp[hero]}')
        print(f' MP: {hero_mana[hero]}')