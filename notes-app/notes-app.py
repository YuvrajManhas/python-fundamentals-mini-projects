import json
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent = 4)

def load_notes():
    try:
        with open ("notes.json") as file:
            notes = json.load(file)
            return notes
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_note():
    notes = load_notes()

    note_title = input("Enter the title of the note: ")
    note_content = input("Enter the content: ")

    note = {
        "id" : len(notes) + 1,
        "title" : note_title,
        "content" : note_content
    }

    notes.append(note)
    save_notes(notes)

    print("Note added successfully!. ")

def view_notes():
    notes = load_notes()

    print("\nShowing all notes: ")
    print("-" * 30)
    for note in notes:
        print(f'''Note {note["id"]}.''')
        print("Title:", note["title"])
        print("Content:", note["content"])
        print("-" * 30)

def search_note():
    target = input("Enter the word you want to search: ").lower()

    notes = load_notes()
    found = False
    for note in notes:
        if target in note["title"].lower() or target in note["content"].lower():
            print("\nNote found in database")
            print(f'''Note {note["id"]}.''')
            print("Title:", note["title"])
            print("Content:", note["content"])
            found = True


    if not found:
        print("Note does not exist. ")

def delete_note():
    target =  int(input("Enter the Note ID you want to delete: "))

    notes = load_notes()
    for note in notes:
        if note["id"] == target:
            notes.remove(note)
            for index, note in enumerate(notes, start=1):
                note["id"] = index
            save_notes(notes)
            print("\nNote deleted successfully. ")
            return

    print("\nNote does not exist. ")

def main():
    while True:
        print("\n===== NOTES APP =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            search_note()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            print("Thank you for using Notes App!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()