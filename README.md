# Purple rAIn
### The simplest neural network in existence (2 lines of code with no 3-party dependency)

What it does?
Classifies if the given RGB input resolves to purple or orange (approximately)

Run:
``` python
> python .\purple_rain.py "150,100,150"
> purple
```

Graph of the neural network with 2 layers:
<img width="100%" alt="purple rain" src="https://user-images.githubusercontent.com/43297242/234350164-6156f3de-ecba-4bfc-bf79-9c3050d5ab3a.png">

---

but wait...
![image](https://user-images.githubusercontent.com/43297242/232600976-d36de01a-65b8-408f-bf7c-5c39be8bd6b2.png)


yes, they are. 
---
The neural network encodes multiple choices into a single matrix (your model) whereby each node is an if condition and each weight defines the likelihood to activate the ~if condition~ (neuron) for any given input.

PS: of course this is a very poor AI with very low accuracy. It can only categorize 2 colors and the weights were defined at my own taste (they barely matter).
# DO NOT USE IN PRODUCTION

