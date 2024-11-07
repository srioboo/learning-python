try:
    print("Testo con formtao {}".format())
except Exception as e:
    # raise Exception("Ha ocurrido un error") # antes de 3.11
    e.add_note("Ha ocurrido un error") # desde 3.11
    print(e.__notes__)

