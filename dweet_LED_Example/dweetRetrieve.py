# ==================================================== #
# ============== Import libraries that matter ======== #
import dweepy
# ==================================================== #

# ==================================================== #

# Get thing name sourced from dweet.io
thing = input("Enter the thing name: " )

# Assign data variables
# Use the names copied verbatim from the thing  
data1 = input("Retrieve IoT data #1 from the thing: " )

data2 = input("Retrieve IoT data #2 from the thing: " )

data3 = input("Retrieve IoT data #3 from the thing: " )

thing_info = dweepy.get_latest_dweet_for(thing)
# thing_info is a list of dictionaies

# ==================================================== #


# ==================================================== #
# ============== Start retrieving data =============== #

#Store "thing_info" as a dictionary; slice 0th entry
this_dict = thing_info[0]

date_created = this_dict['created']

dateNow = date_created[:10]

stamptime = date_created[11:19]

tempC = this_dict['content'][str(data1)]

tempF = (int(tempC)*(9/5))*32

humidity = this_dict['content'][str(data2)]

pressure = this_dict['content'][str(data3)]

print("Status update for", thing)
print("Date", dateNow)
print("Time", stamptime)
print("Current temperature is...", tempC, "C")
print("Current temperature is...", tempF, "F")
print("Current humidity is...", humidity)
print("Current humidity is...", pressure)
