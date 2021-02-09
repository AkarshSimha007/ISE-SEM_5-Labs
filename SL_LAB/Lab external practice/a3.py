def atomicDic():

    ad = {
        "H": "Hydrogen",
        "O": "Oxygen",
        "N": "Nitrogen",
        "He": "Helium"
    }


    for i in ad.keys():
        print(i, ad[i])

    newele = input("Enter symbol of new element:")
    newname = input("Enter name of the element:")
    ad[newele] = newname

    for i in ad.keys():
        print(i, ad[i])

    print(len(ad))

    searchele = input("Enter element to be searched:")
    if searchele in ad.keys():
        print("Element Found")
    else:
        print(f"{searchele} not Found!")
