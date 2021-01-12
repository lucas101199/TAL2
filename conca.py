import os
import shutil

directory = "../TP1/corpus_topic/"
f = open("all_topic.txt", "a")

for subdir in os.listdir(directory):
    file = os.path.join(directory, subdir)
    filename = file + "/all.txt"
    shutil.copyfile(filename, "all_topic.txt")
    f.write('\n')
