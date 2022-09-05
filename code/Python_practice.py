# counties_dict = {} #dict

# counties_dict["Arapahoe"] = 422829 
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438

# #print(counties_dict) print out dict
# # print(len(counties_dict)) lenght of dict
# #print(counties_dict.items()) items in dict
# #print(counties_dict.keys()) keys in dict
# #print(counties_dict.values()) values in dict

# # print(counties_dict.get("Denver")) get a specifc value
# # print(counties_dict['Arapahoe']) - same ^

# ##### list of dict 

# voting_data = []

# # appending to list 
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# # print(voting_data)

# voting_data.append({"county":"El Paso", "registered_voters": 461149})

# # print(voting_data)

# voting_data.pop(0)

# # print(voting_data)

# voting_data.pop(0)
# voting_data.pop()
# voting_data.insert(0,{"county":"El Paso", "registered_voters": 461149})
# voting_data.append({"county":"Denver", "registered_voters": 463353})

# # print(voting_data)

# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

# print(voting_data)

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# Iterate Through a Dictionary

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys(): # keys
#     print(county)

# for voters in counties_dict.values(): #values
#     print(voters)

# for county in counties_dict: # values
#     print(counties_dict[county])

# for county in counties_dict: #value
#     print(counties_dict.get(county))

#Get the Key-Value Pairs of a Dictionary

# #Format
# for key, value in dictionary_name.items():
#     print(key, value)

# for county, voters in counties_dict.items():
#     print(county + 'county has ' + str(voters) + 'registered voters.')

 #  Iterate Through a List of Dictionaries
#  Get Each Dictionary in a List of Dictionaries


# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# # for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):

#       print(voting_data[i]['county'])

# Get the Values from a List of Dictionaries

# for county_dict in voting_data: # get only the values use nested for loop
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data: # registered voters 

#      print(county_dict['registered_voters'])

# Using F-Strings with Dictionaries

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

# # for county, voters in counties_dict.items():
# #     print(county + " county has " + str(voters) + " registered voters.")

# # for county, voters in counties_dict.items(): # using f string
# #     print(f"{county} county has {voters} registered voters.")

#   # Multiline F string
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# # message_to_candidate = (
# #     f"You received {candidate_votes} number of votes. "
# #     f"The total number of votes in the election was {total_votes}. "
# #     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)



# # Import the datetime class from the datetime module.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)


# To reduce the confusion on importing a module with the same name as a class we can use an abbreviated alias dt for the datetime module.

# Import the datetime class from the datetime module.
# import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# import csv
# print( dir(dt))
# print( dir(csv))

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# election_data.close()

# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)
  
# Indirect Path to the File
# import os

# # print(dir(os))
# print(dir(os.path))


# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file.
#     #  txt_file.write("Arapahoe, ")
#     #  txt_file.write("Denver, ")
#     #  txt_file.write("Jefferson")

#     #  Write three counties to the file.
#     #  txt_file.write("Arapahoe, Denver, Jefferson")

#      # Write three counties to the file.
#      txt_file.write('Counties in the Election\n')
#      txt_file.write('-'*30 + '\n')
#      txt_file.write("Arapahoe\nDenver\nJefferson")