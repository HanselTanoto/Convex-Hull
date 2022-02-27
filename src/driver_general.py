import pandas as pd 
import matplotlib.pyplot as plt
import myConvexHull
import InputOutput

# Load database
data = InputOutput.chooseDataset()

# Create a DataFrame 
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target) 
print("Data shape: {}".format(df.shape))
print(df.head())

while (True):
    # Pemilihan atribut yang ingin digunakan
    atr1, atr2 = InputOutput.chooseAttribute(data)

    # Visualisasi hasil ConvexHull - iris-sepal
    plt.figure(figsize = (10, 6))
    colors = ['r','g','b','c','m','y','k','grey','violet','saddlebrown','purple']
    plt.title("{} Vs {}".format(data.feature_names[atr1], data.feature_names[atr2]).replace("_"," ").title())
    plt.xlabel(data.feature_names[atr1].title())
    plt.ylabel(data.feature_names[atr2].title())
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[atr1,atr2]].values
        hull = myConvexHull.myConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
        plt.scatter(bucket[:, 0], bucket[:, 1], c=colors[i % len(colors)], label=data.target_names[i])
        for simplex in hull.simplices:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i % len(colors)])
        plt.legend()
    x = input("\nPress enter to show figure...")
    plt.show()

    # Konfirmasi keluar program
    confirm = InputOutput.exitConfirm()
    if (confirm == 'N' or confirm == 'n'):
        break