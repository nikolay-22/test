def plunder(town_, people_count_, gold_count_):
    towns_dict[town_]['people'] -= people_count_
    towns_dict[town_]['gold'] -= gold_count_
    print(f"{town_} plundered! {gold_count_} gold stolen, {people_count_} citizens killed.")
    if towns_dict[town_]['people'] == 0 or towns_dict[town_]['gold'] == 0:
        print(f"{town_} has been wiped off the map!")
        del towns_dict[town_]


def prosper(town_, gold_count_):
    if gold_count_ < 0:
        print("Gold added cannot be a negative number!")
    else:
        towns_dict[town_]['gold'] += gold_count_
        print(f"{gold_count_} gold added to the city treasury. {town_} now has {towns_dict[town_]['gold']} gold.")


towns_dict = {}
towns_info = input()
while not towns_info == "Sail":
    town, people_count, gold_count = towns_info.split("||")
    people_count = int(people_count)
    gold_count = int(gold_count)
    if town in towns_dict:
        towns_dict[town]['people'] += people_count
        towns_dict[town]['gold'] += gold_count
    else:
        towns_dict[town] = {'people': people_count, 'gold': gold_count}
    towns_info = input()
#print(towns_dict)

event = input()
while not event == "End":
    event = event.split("=>")
    if event[0] == "Plunder":
        town = event[1]
        people_count = int(event[2])
        gold_count = int(event[3])
        plunder(town, people_count, gold_count)
    elif event[0] == "Prosper":
        town = event[1]
        gold_count = int(event[2])
        prosper(town, gold_count)
    event = input()

if len(towns_dict) > 0:
    print(f"Ahoy, Captain! There are {len(towns_dict)} wealthy settlements to go to:")
    #Sort on two lines (66/100):
    #res = dict(sorted(towns_dict.items(), key=lambda x: x[0]))
    #res = dict(sorted(towns_dict.items(), key=lambda x: -x[1]['gold']))
    # Sort on one line calling attributes:
    res=dict(sorted(towns_dict.items(), key=lambda x: (-x[1]['gold'], x[0])))
    # Sort on one line with references - RUNTIME ERROR?!?!?!?!?:
    #res=dict(sorted(towns_dict.items(), key=lambda x: (-x[1][1], x[0])))
    # {'Port Royal': {'people': 420000, 'gold': 3000}, 'San Juan': {'people': 930000, 'gold': 1250}}
    for key, value in res.items():
        print(f"{key} -> Population: {value['people']} citizens, Gold: {value['gold']} kg")
    #print(res)
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")