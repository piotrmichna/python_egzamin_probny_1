def name_sorter(names):
    male = []
    female = []
    for name in names:
        if name[-1] == 'a':
            female.append(name)
        else:
            male.append(name)

    male.sort()
    female.sort()

    return 'female: ' + str(female) + ', male: ' + str(male)


if __name__ == '__main__':
    names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
    print(name_sorter(names))
