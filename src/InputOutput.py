"""
Modul untuk menangani proses I/O dengan user beserta validasinya
"""

from sklearn import datasets

def chooseDataset():
    while (True):
        print("\nList of Datasets:")
        print("1. Iris plants dataset")
        print("2. Wine recognition dataset")
        print("3. Breast cancer wisconsin (diagnostic) dataset")
        db = input("Choose database (1/2/3): ")
        if (db == '1' or db == '2' or db == '3'):
            break
        print("Invalid input, try again!")
    if (db == '1'):
        data = datasets.load_iris()
    elif (db == '2'):
        data = datasets.load_wine()
    elif (db == '3'):
        data = datasets.load_breast_cancer()
    return data

def chooseAttribute(data):
    print("\nList of Attributes:")
    for i in range (len(data.feature_names)):
        print("[{:2d}] {}".format(i, data.feature_names[i]))
    while (True):
        atr1 = int(input("Choose first attribute (number)  : "))
        if (atr1 in range(0,len(data.feature_names))):
            break
        print("Invalid input, try again!\n")
    while (True):
        atr2 = int(input("Choose second attribute (number) : "))
        if (atr2 in range(0,len(data.feature_names))):
            break
        print("Invalid input, try again!\n")
    return atr1, atr2

def exitConfirm():
    while (True):
        x = input("\nContinue? (Y/N): ")
        if (x == 'Y' or x == 'y' or x == 'N' or x == 'n'):
            break
        print("Invalid input, try again!")
    return x