



def dictntotups(my_dict):
        
    tuple_list = []

    for key, value in my_dict.iteritems():
        
        tuple_list.append("({}, {})".format(key, value))
    
    print tuple_list
    #return tuple_list

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

dictntotups(my_dict)