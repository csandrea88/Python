def draw_stars():

    list = [4, 6, 1, 3, 5, 7, 25]
    #list = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    
    for x in list:
  
        if isinstance(x, int):
            stars = ""
            for i in range(x):
                stars += "*"
            print stars

        elif isinstance(x, str):
            strings = ""
            lowlet = x[0].lower()
            for l in range(len(x)):
                strings += lowlet
            print strings
draw_stars()