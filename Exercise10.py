import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
l1 = data.split("\n")
l2 = [item.split(",") for item in l1 if len(item)!=0]
print(l2)
with open("myiris","wb") as f :
    pickle.dump(l2,f)
with open("myiris","rb") as f:
    for i in f:
        print(i,end=" ")
