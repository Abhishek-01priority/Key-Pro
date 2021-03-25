import pandas as pd
import os
from collections import OrderedDict


filenames = os.listdir("/home/abhishek/Desktop/Key-Pro/Dataset")

os.chdir("/home/abhishek/Desktop/Key-Pro/Dataset")

for name in filenames:

	df = pd.read_csv(name,encoding= 'unicode_escape')

	df.columns = ['words']

	# print("Old dictionary = " + str(len(df["words"])))

	df["words"] = df["words"].str.split(" ")

	temp = []
	new_dict = []

	for word in df["words"]:
		temp.append(word[0])

	new_dict = list(OrderedDict.fromkeys(temp))

	# print("New dictionary = " + str(len(new_dict)))

	Dic = pd.DataFrame(new_dict)

	os.chdir("/home/abhishek/Desktop/Key-Pro/Dataset_2")

	Dic.to_csv(name)

	os.chdir("/home/abhishek/Desktop/Key-Pro/Dataset")