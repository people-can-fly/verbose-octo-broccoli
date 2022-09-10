test_file = "cars-sample35.txt"

price = []
maintenance_cost = []
number_of_doors = []
number_of_passengers = []
luggage_capacity = []
safety_rating = []
classification_of_vehicle = []

# used core module to read file , instead of csv module.

with open(test_file, 'r') as f:
    for line in f:
        line_list = line.split(',')  # str to list
        price.append(line_list[0])
        maintenance_cost.append(line_list[1])
        number_of_doors.append(line_list[2])
        number_of_passengers.append(line_list[3])
        luggage_capacity.append(line_list[4])
        safety_rating.append(line_list[5])
        classification_of_vehicle.append(line_list[6].strip())  # stripping new line


## 1
price_med_index = [i for i, j in enumerate(price) if j == "med"]
print(f"Price 'med' index: {price_med_index}")

## 2
passengers_price_med = [number_of_passengers[i] for i in price_med_index]

###
""" below is a naive approach we are iterating again for price_med_index"""
# passengers_price_med = [number_of_passengers[i] for i, j in enumerate(price) if j == "med"]

print(f"Passengers with price 'med': {passengers_price_med}")

## 3
high_price_high_maintenance = [i for i, j in enumerate(price) if j == "high" and maintenance_cost[i] != "low"]
print(f"Vehicle with maintenance over low and price high: {high_price_high_maintenance}")

## 4
nlist = [[1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E']]

# flist = []
# for x in nlist:
#     for y in x:
#         flist.append(y)
# print(flist)

flatten_list = [i for sublist in nlist for i in sublist]
print(f"flatten list: {flatten_list}")


## 5

def makedict(mylist, x):
    """will return empty dict if x is out if range for mylist"""
    new_dict = dict()
    if x <= len(mylist):
        for i in range(x):
            new_dict[f"A{i}"] = mylist[i]
    return new_dict


###### Using dictionary comprehension
"""this is similar to list comprehension """
# def makedict(mylist, x):
#     return {f"A{i}": mylist[i] for i in range(x) if x<= len(mylist)}

print(f"new dict: {makedict(luggage_capacity, 5)}")



## 6
seven_price_dict = makedict(price, 7)
seven_luggage_dict = makedict(luggage_capacity, 7)

print(f"A4 price: {seven_price_dict.get('A4')}, A4 luggage: {seven_luggage_dict.get('A4')}")
