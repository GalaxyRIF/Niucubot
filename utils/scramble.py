import pickle
from random import choice
# reading scramble file
file = open(r"data.pkl", "rb")
# dat.pkl
# D:\Desktop\Things\WCA\dat.pkl
scramble_dict = pickle.load(file)
file.close()

def get_scramble(event,number=1):
    scrambles=[]
    for i in range(number):
            while True:
                scr=choice(scramble_dict[event])
                if not scr in scrambles:
                    scrambles.append(scr)
                    break
    txt=""
    for i in range(number):
        txt+=f"{i+1}. {scrambles[i]}\n"
    return txt[:-1]