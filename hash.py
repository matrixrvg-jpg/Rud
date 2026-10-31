# Hash Table using Chaining - SPPU Practical

# Create a hash table of size 10 using a list of empty lists
hash_table = []
for i in range(10):
    hash_table.append([])

while True:
    print("\n--- HASH TABLE PROGRAM ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        key = int(input("Enter key (number): "))
        val = input("Enter value (data): ")
        
        # Division method hash function
        pos = key % 10
        
        # Insert key-value pair into the chain at index 'pos'
        hash_table[pos].append([key, val])
        print("Data inserted successfully!")
        
    elif ch == 2:
        key = int(input("Enter key to search: "))
        pos = key % 10
        
        found = 0
        for i in range(len(hash_table[pos])):
            if hash_table[pos][i][0] == key:
                print("Key found! Value is:", hash_table[pos][i][1])
                found = 1
                break
        
        if found == 0:
            print("Key not found in hash table.")
            
    elif ch == 3:
        key = int(input("Enter key to delete: "))
        pos = key % 10
        
        deleted = 0
        for i in range(len(hash_table[pos])):
            if hash_table[pos][i][0] == key:
                del hash_table[pos][i]
                print("Key deleted successfully!")
                deleted = 1
                break
        
        if deleted == 0:
            print("Key not found.")
            
    elif ch == 4:
        print("\n--- HASH TABLE CONTENTS ---")
        for i in range(10):
            print("Index", i, ":", hash_table[i])
            
    elif ch == 5:
        print("Exiting program...")
        break
        
    else:
        print("Wrong choice! Please enter between 1 and 5.")