# Employee Salaries Sorting - SPPU Practical

n = int(input("Enter total number of employees: "))

salaries = []

# Taking input for salaries
for i in range(n):
    sal = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(sal)

# Create two separate lists manually for sorting
sel_list = []
bub_list = []
for s in salaries:
    sel_list.append(s)
    bub_list.append(s)


# --- 1. SELECTION SORT (Ascending Order) ---
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if sel_list[j] < sel_list[min_index]:
            min_index = j
            
    # Swap elements manually
    temp = sel_list[i]
    sel_list[i] = sel_list[min_index]
    sel_list[min_index] = temp


# --- 2. BUBBLE SORT (Ascending Order) ---
for i in range(n):
    for j in range(0, n - i - 1):
        if bub_list[j] > bub_list[j + 1]:
            # Swap elements manually
            temp = bub_list[j]
            bub_list[j] = bub_list[j + 1]
            bub_list[j + 1] = temp


# --- DISPLAY RESULTS ---
print("\n--- OUTPUT ---")
print("Sorted by Selection Sort:", sel_list)
print("Sorted by Bubble Sort:   ", bub_list)


# --- 3. DISPLAY TOP 5 HIGHEST SALARIES ---
print("\n--- TOP 5 HIGHEST SALARIES ---")
if n == 0:
    print("No records found.")
else:
    # Decide how many to print (if total employees are less than 5)
    count = 5
    if n < 5:
        count = n
        
    # Print from the end of the sorted list backwards
    for i in range(count):
        print(sel_list[n - 1 - i])