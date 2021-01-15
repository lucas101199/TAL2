f = open("Q5bis.txt", "r")
out = open("decoup.txt", "w")
out.write("<s>")
line_full = ""
for line in f:
    line_full += line[:-1] + " "
    if line[0] == ".":
        next_ = f.readline()
        if next_[0].isupper() or next_ == "<SAUT-LIGNE/>\n":
            out.write(line_full)
            out.write("</s>\n<s>")
            line_full = ""
        if next_ != "<SAUT-LIGNE/>\n":
            out.write(next_[:-1])
        if next_.isnumeric():
            out.write(next_)
        if line == "":
            out.write(line_full)
            out.write("</s>")
    if line[-1].islower():
        next_ = f.readline()
        if next_ == "<SAUT-LIGNE/>\n":


