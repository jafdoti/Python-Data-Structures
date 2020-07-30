"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_reader = csv.reader(csv_file, delimiter=separator, quotechar=quote) 
        return next(csv_reader)


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
    table = []
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator, 
                                   quotechar=quote)
        for row in csvreader:
            table.append(row)
            #print(row)
    return table

# test_table = read_csv_as_list_dict('isp_csv_files/table4.csv', ',', '"')
# print(test_table)


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator, 
                                   quotechar=quote)
        for row in csvreader:
            table[row[keyfield]] = row
    return table

# test_table = read_csv_as_nested_dict('isp_csv_files/table1.csv', 'Field1', ',', '"') 
# test_table = read_csv_as_nested_dict('isp_csv_files/table2.csv', 'Field2', ',', '"') 
# print(test_table)

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, 
                                    fieldnames, 
                                    delimiter=separator, 
                                    quotechar=quote, 
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(table)


# write_csv_from_list_dict('output1.csv', [{'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14}, 
#                                          {'a': 20, 'b': 21, 'c': 22, 'd': 23, 'e': 24}, 
#                                          {'a': 30, 'b': 31, 'c': 32, 'd': 33, 'e': 34}, 
#                                          {'a': 40, 'b': 41, 'c': 42, 'd': 43, 'e': 44}], 
#                                          ['a', 'b', 'c', 'd', 'e'], ',', '"') 