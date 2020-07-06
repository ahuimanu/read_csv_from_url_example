import requests

# read file from website (assumes txt/csv flat file, not JSON)
data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

print(data.text)

# write what we get to a temp file
f = open("output.txt", "w")
f.write(data.text)
f.close()

# create a list to hold tuples that dictionaries of the CSV's fields
records = []

# open that file back up for processing
f = open("output.txt", "r")
for r in f:
    # breaks up a line of CSV into usbale "chunks"
    # https://www.w3schools.com/python/ref_string_split.asp
    parts = r.split(',')
    # make sure we got the expected number of elements
    if len(parts) == 5:
        records.append( 
            {
                "sepal_length" : parts[0],
                "sepal_width" : parts[1],
                "petal_length" : parts[2],
                "petal_width" : parts[3],
                "iris_class" : parts[4], 
            }            
        )

# loop through records
for record in records:
    print("sepal length: {0}, sepal width: {1}, petal length: {2}, petal width: {3}, class: {4}"\
          .format(record["sepal_length"], 
                  record["sepal_width"], 
                  record["petal_length"], 
                  record["petal_width"],
                  record["iris_class"]))
