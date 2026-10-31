

n = int(input("Enter total members: "))

names = []
books_list = []

# Taking input
for i in range(n):
    name = input("Enter member name: ")
    names.append(name)
    
    b = input("Enter books (comma separated): ")
    if b == "":
        books_list.append([])
    else:
        # Split by comma
        temp = b.split(",")
        clean_books = []
        for book in temp:
            clean_books.append(book.strip())
        books_list.append(clean_books)

print("\n--- OUTPUT ---")

# 1. Average number of books borrowed
total_books = 0
for i in range(n):
    total_books = total_books + len(books_list[i])

avg = total_books / n
print("1. Average books borrowed:", avg)


# 2. Count members with 0 books
zero_members = 0
for i in range(n):
    if len(books_list[i]) == 0:
        zero_members = zero_members + 1

print("3. Members with 0 books:", zero_members)


# 3. Count frequency of each book using lists
all_books = []
counts = []

for i in range(n):
    for b in books_list[i]:
        # Check if book already counted
        found = False
        for j in range(len(all_books)):
            if all_books[j] == b:
                counts[j] = counts[j] + 1
                found = True
                break
        if found == False:
            all_books.append(b)
            counts.append(1)


# 4. Find highest, lowest and mode books
if len(all_books) > 0:
    max_pos = 0
    min_pos = 0
    
    for i in range(len(counts)):
        if counts[i] > counts[max_pos]:
            max_pos = i
        if counts[i] < counts[min_pos]:
            min_pos = i
            
    print("2. Most borrowed book:", all_books[max_pos], "(", counts[max_pos], "times)")
    print("   Least borrowed book:", all_books[min_pos], "(", counts[min_pos], "times)")
    
    print("4. Most frequent book (Mode):", all_books[max_pos])
else:
    print("2. No books were borrowed.")
    print("4. Mode: None")