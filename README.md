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
![image](https://user-images.githubusercontent.com/43297242/234131697-193fcfa5-ade3-422f-bfa0-4cb7cb4e3242.png)

---

but wait...
![image](https://user-images.githubusercontent.com/43297242/232600976-d36de01a-65b8-408f-bf7c-5c39be8bd6b2.png)


yes, they are. The neural network encodes multiple choices into a single matrix (your model) whereby each node is an if condition and each weight is the activator of such condition.
---

PS: of course this is a very poor AI with very low accuracy. It can only categorize 2 colors and the weights were defined at my own taste (they barely matter).
# DO NOT USE IN PRODUCTION

