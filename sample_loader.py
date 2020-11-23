import pandas as pd 

# in python, # comment off a single line while """(some content)""" comment off multiple lines

data_frame = pd.read_csv("toy.csv")

print(data_frame)

# to access a column and turn it into a list
names = list(data_frame["name"])
# print(names)

# to sort according to an attribute (a specific column)
print("\nsorted result #1")
sorted_df_1 = data_frame.sort_values(by=['name'])
print(sorted_df_1)


# to sort according to multiple attributes
print("\nsorted result #2")
sorted_df_2 = data_frame.sort_values(by=['name', 'count'])
print(sorted_df_2)