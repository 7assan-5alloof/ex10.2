# Open file
file = open(input("Enter file name: "))

# Create hisotgram of hour value associated with sent email
histogram = dict()
for line in file:
    if "From " in line:
        words = line.split()
        del(words[:5])
        clock = words[0].split(":")
        hour = clock[0]
        histogram[hour] = histogram.get(hour, 0) + 1

# Display histogram sorted by hour
histogram = sorted([(hour, frequency) for hour, frequency in histogram.items()])
for pair in histogram:
    for item in pair:
        if type(item) == str:
            print(item, end=" ")
        else:
            print(item)
