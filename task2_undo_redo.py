stack1 = []
stack2 = []

while True:
    command = input("type/undo/redo/quit: ")
    if command == "quit":
        break
    elif command[:4] == "type":
        s = command[5:]
        stack1.append(s)
        print("Document:", end=" ")
        for word in stack1:
            print(word, end="")
        print("")
        stack2 = []

    elif command == "undo":
        if stack1 == []:
            print("Nothing to undo")
        else:
            stack2.append(stack1.pop())
            print("Document:", end=" ")
            for word in stack1:
                print(word, end="")
            print("")

    elif command == "redo":
        if stack2 == []:
            print("Nothing to redo")
        else:
            stack1.append(stack2.pop())
            print("Document:", end=" ")
            for word in stack1:
                print(word, end="")
            print("")

    else:
        print("Invalid command")