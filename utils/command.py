from .comp import *
from random import choice
from .scramble import get_scramble

events_map={
        ".3":"333",
        ".333":"333",
        ".3bf":"333bf",
        ".333bf":"333bf",
        ".4":"444",
        ".444":"444",
        ".4bf":"444bf",
        ".444bf":"444bf",
        ".5":"555",
        ".555":"555",
        ".5bf":"555bf",
        ".555bf":"555bf",
        ".6":"666",
        ".666":"666",
        ".7":"777",
        ".777":"777",
        ".clock":"clock",
        ".cl":"clock",
        ".pyr":"pyram",
        ".pyram":"pyram",
        ".py":"pyram",
        ".p":"pyram",
        ".mega":"minx",
        ".minx":"minx",
        ".skewb":"skewb",
        ".sk":"skewb",
        ".sq":"sq1",
        ".sq1":"sq1",
    }

def reader(mess):
    # separating sentence
    contents=mess.split(" ")
    contents=[i for i in contents if i!=""]
    # scrambles
    
    # First function: getting scrambles of WCA cubes
    if contents[0] in events_map.keys():
        try:
            num=int(contents[1])
        except:
            num=1
        return get_scramble(events_map[contents[0]],num)

    # second function: get WCA competition information
    elif contents[0]==".comp":
        return return_comps(contents)
    else:
        return None
