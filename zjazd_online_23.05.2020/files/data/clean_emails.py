import sys

try:
    f_in_path = sys.argv[1]
    out_f_path = sys.arg[2]
except IndexError:
    f_path = "data/emails.txt"
    out_f_path = "output/cleaned_emails.txt"

with open(f_in_path) as infile:
        clean_emails = set()
        for line in infile:
            if len(line.split("@")) == 2 and line[0] == "u":
                clean_emails.add(line)

print("".join(clean_emails))

with open(out_f_path,"a") as outfile:
        outfile.write("".join(clean_emails))

