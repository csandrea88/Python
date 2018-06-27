
def make_dict(name, favorite_animal):
  
  new_dict = {}

  for i in range(len(name)):

    new_dict[name[i]]=favorite_animal[i]

  print new_dict


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

make_dict(name, favorite_animal)