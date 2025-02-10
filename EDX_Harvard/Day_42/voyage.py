distances ={
    "Voyage 1": 163,
    "Voyage 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main1():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from earth")
        
def main2():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")
        
def convert(au):
    return au * 149597870700

main2()
