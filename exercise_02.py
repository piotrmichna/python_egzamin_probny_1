def name_sorter(names):
    male=[]
    female=[]
    for name in names:
        if name[-1]=='a':
            female.append(name)
        else:
            male.append(name)
    return 'female: '+str(female)+', male: '+str(male)

