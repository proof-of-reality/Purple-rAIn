import sys
if __name__ == '__main__':
    input = sys.argv[1:][0]
    fstLayer = [float(x)*1 for x in input.split(',')]
    sndLayer = [.5,.5] # orange, purple
    orange = fstLayer[0]*sndLayer[0] + fstLayer[1]*sndLayer[0]
    purple = fstLayer[0]*sndLayer[1] + fstLayer[2]*sndLayer[1]
    print("purple" if purple > orange else "orange")