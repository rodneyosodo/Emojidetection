import os
import shutil

directories = os.listdir("Working_data")
files = os.listdir("Dir")
os.chdir("Dir")
src_dir = os.getcwd()
os.chdir("../Human_data")
des_dir = os.getcwd()

for dir in directories:
	os.mkdir(dir.split(".")[0])

os.chdir("../")
counter = 0

for dir2 in directories:
	for file in files:
		source = file
		destination = des_dir + "\\" + dir2 
		os.system("mv Dir\\{} {}".format(source, destination))
		if counter % 5 == 0:
			print(counter)
			break
		counter += 1
