import sys
if __name__ == '__main__':
    input = [float(x)*1 for x in sys.argv[1:][0].replace(" ", "").split(',')] # split each value into neural input layer (r,g,b)
    out = [sum([i*w for i,w in zip(input, weights)]) for weights in [[.5,.5,.0],[.5,.0,.5]]] # propagate values applying weights 
    print("purple" if out[1] > out[0] else "orange")