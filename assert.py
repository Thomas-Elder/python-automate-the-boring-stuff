#! python3

import traceback

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):

    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
            if 'red' not in intersection.values():
                intersection[key] = 'red' 
    
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)

for x in range(0,10):
    switchLights(market_2nd)
    print(market_2nd)
