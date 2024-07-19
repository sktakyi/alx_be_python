#assign & compute variables
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
              print(f"Current shopping list: {shopping_list}")
              item = input("Enter the item to add: ")
              shopping_list.append(item)
              print(f"Added item in shopping list: {shopping_list}")
              pass      
        elif choice == '2':
              print(f"Current shopping list: {shopping_list}")
              item1 = input("Item to be removed: ")
              shopping_list.remove(item1)
              print(f"Removed item in shopping list: {shopping_list}")
              pass
        elif choice == '3':
              print(f"Current shopping list: {shopping_list}")
              shopping_list.sort()
              print(f"Sorted shopping list: {shopping_list}")
              pass        
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()