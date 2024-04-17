import csv
from datetime import datetime

def main():
    
    PRODUCT_NUMBER = 0
    QUANTITY = 1
    total_items_ordered = 0
    now = datetime.now()
    subtotal = 0.0


    try:
        products_dict = read_dictionary("products.csv", PRODUCT_NUMBER)

        print()
        print("Kohl Foods") 
        print()

        with open('request.csv', 'rt') as requests:
            reader = csv.reader(requests)
            next(reader)
            
            for row_list in reader:

                ordered_product = row_list[PRODUCT_NUMBER]
                amount_ordered = int(row_list[QUANTITY])

                item = products_dict[ordered_product] 

                
                product = item[1]
                price = float(item[2])

                print(f"{product}: {amount_ordered} @ ${price}")
                total_items_ordered += amount_ordered
                subtotal += price*amount_ordered

        print(f"{product}: {amount_ordered} @ ${price}")
        print()
        print(f"Number of items: {total_items_ordered} ")
        print(f"Subtotal: {round(subtotal, 2)}")
        print(f"Sales Tax: {round(subtotal*0.06, 2)}  ")
        print(f"Total: {round(subtotal+(subtotal*0.06), 2)}")
        print()
        print('Thank you for shopping at Kohl Foods')
        print(now.strftime("%a %b  %d %X %Y"))
    
    except FileNotFoundError as file_err:
        print(file_err)
    except PermissionError as per_err:
        print(per_err)
    except KeyError as key_err:
        print(f"This key does not exist: {key_err}")
    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
        to use as the keys in the dictionary.
    Return: a compound dictionary that contains
    the contents of the CSV file.
    """

    dictionary = {} #creates an empty dictionary

    with open(filename, "rt") as csv_file: #will open any file put into it for reading
        reader = csv.reader(csv_file)#reads file
        next(reader)#skips first row 

        for row_list in reader: #iterates through the list of information in the provided csv file. 
            if len(row_list) != 0: #if the line has information on it
                key = row_list[key_column_index] #retrive the key information
                dictionary[key] = row_list #store current row in dictionary

    return dictionary 


if __name__ == "__main__":
    main()