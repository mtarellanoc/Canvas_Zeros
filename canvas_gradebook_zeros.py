import os
import sys

most_recent_csv = ["",-1]
for file in os.listdir('.'):
    if file.endswith('.csv'):
        timestamp = os.path.getmtime(file)
        if timestamp > most_recent_csv[1]:
            most_recent_csv = [file, timestamp]

csv_file = most_recent_csv[0]

if csv_file not in os.listdir("."):
    print(f"file: {csv_file} not found.")
    sys.exit()
print(f"reading {csv_file}")
with open(csv_file,"r") as file:
    file_records = file.readlines()

i = 0
while i < len(file_records):
    while True:
        if (",," not in file_records[i]) or (i < 2):
            break
        file_records[i] = file_records[i].replace(",,", ",0,")
    i = i + 1

with open(f"{csv_file.split('.')[0]}_with_zeros.csv","w") as new_file:
    for line in file_records:
        new_file.write(line)

print(f"{csv_file.split('.')[0]}_with_zeros.csv has been created.")

