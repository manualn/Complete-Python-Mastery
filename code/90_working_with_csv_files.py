import csv

#with open("data.csv", "w") as file:
    #writer = csv.writer(file)
    #writer.writerow(["transaction_id", "product_id", "price"])  
    # similarly add second row
    #writer.writerow([1000, 1, 5])
    #writer.writerow([1000, 2, 15])


with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)