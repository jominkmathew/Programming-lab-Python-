import csv
with open('content.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["sl.no", "Department", "Room no"])
    writer.writerow([1, "MCA", "1011"])
    writer.writerow([2, "MBA", "1021"])
    writer.writerow([2, "M.Phil", "1036"])
with open('content.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
