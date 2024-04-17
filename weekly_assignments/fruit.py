
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print()
    print(f"original: {fruit_list}")

    #reversed fruit list
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    #append orange to list
    fruit_list.append('orange')
    print(f'add orange: {fruit_list}')

    #Add code to find where "apple" is located in fruit_list and 
    #insert "cherry" before "apple" in the list and print the list.
    i = fruit_list.index('apple')
    fruit_list.insert(i, 'cherry')
    print(f'add cherry before apple: {fruit_list}')

    #Add code to remove "banana" from fruit_list and print the list. 
    fruit_list.remove('banana')
    print(f'remove banana: {fruit_list}')

    #Add code to pop the last element from fruit_list and print the popped element and the list.
    removed = fruit_list.pop()
    print(f'Item removed: {removed}')
    print(f'New list: {fruit_list}')

    #Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f'sort and print: {fruit_list}')

    #Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f'clear and print: {fruit_list}')




if __name__ == "__main__":
    main()