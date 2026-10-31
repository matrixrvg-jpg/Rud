# Real-time Undo/Redo System using Stacks - SPPU Practical

current_text = input("Enter initial document text: ")

undo_stack = []
redo_stack = []

while True:
    print("\n--- TEXT EDITOR MENU ---")
    print("1. Make a Change")
    print("2. Undo Action")
    print("3. Redo Action")
    print("4. Display Document State")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        undo_stack.append(current_text)
        redo_stack = []
        current_text = input("Enter new text: ")
        print("-> Change saved successfully!")
        
    elif choice == '2':
        if len(undo_stack) > 0:
            redo_stack.append(current_text)
            current_text = undo_stack.pop()
            print("-> Undo performed successfully!")
            print("   Current Text:", current_text if current_text != "" else "[Document is empty]")
        else:
            print("-> Error: Nothing to undo!")
            
    elif choice == '3':
        if len(redo_stack) > 0:
            undo_stack.append(current_text)
            current_text = redo_stack.pop()
            print("-> Redo performed successfully!")
            print("   Current Text:", current_text if current_text != "" else "[Document is empty]")
        else:
            print("-> Error: Nothing to redo!")
            
    elif choice == '4':
        print("\n--- CURRENT DOCUMENT STATE ---")
        print(current_text if current_text != "" else "[Document is empty]")
        print("------------------------------")
        
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")