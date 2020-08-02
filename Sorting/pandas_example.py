import pandas as pd
import csv

# statistics =  [
# {'player': '1', 'stat1': '3', 'stat2': '4', 'stat3': '5'},
# {'player': '1', 'stat1': '2', 'stat2': '1', 'stat3': '8'},
# {'player': '3', 'stat1': '4', 'stat2': '1', 'stat3': '6'},
# {'player': '3', 'stat1': '8', 'stat2': '7', 'stat3': '3'}]
# 
# fields = ['stat2', 'stat3']
# 
# data = pd.DataFrame(statistics)
# 
# # Convert stat data to int
# data[fields] = data[fields].astype(int)
# print(data)
# 
# # Sum it up
# gb_df = data.groupby('player').sum()
# print(gb_df)
# 
# new_dict = gb_df.transpose().to_dict()
# print(new_dict)

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
#     table = []
#     with open(filename, newline='') as csvfile:
#         csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
#         for row in csvreader:
#             table.append(row)
#     return table
#     
    df = pd.read_csv(filename)
    print(df)
    print(df.transpose().to_dict())

read_csv_as_list_dict("master1.csv", ",", "'")