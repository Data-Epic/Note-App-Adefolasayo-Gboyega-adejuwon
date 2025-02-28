from datetime import datetime

#create base class Note and its attributes
class Note:
    """
    A base class representing a note.
    """
    def __init__(self, content, created_at=None): #make created_at optional.
        """Initialize Note object

        Args:
            content (string): The content of the note
            created_at (datetime): The date and time of the note creation
        """
        self.content = content
        if created_at is None: #only assign if not passed.
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
        
     #create a method to show note details.        
    def display(self):
        """
        Displays the note's content and creation time.

        Returns: A formatted string containing note details.
        """
        return f"Note: {self.content}\nCreated at: {self.created_at}"
    
    
    
class TextNote(Note):
    """
    A class representing a text-based note.
    """
    def __init__(self,content,created_at):
        """Initialize a reminder note object

        Args:
            content (string): The content of the note
            created_at (string): The date time the note was created
        """
        super().__init__(content, created_at)  # Call parent's __init__
    def display(self):
        return f"Note: {self.content}\nCreated at: {self.created_at}"
    
    
    
class ReminderNote(Note):
    """
    A class representing a reminder-based note.
    """
    def __init__(self,content, created_at, reminder_time):
        """Initialize a reminder note object

        Args:
            content (string): The content of the note
            created_at (string): The date time the note was created
            reminder_time (string): The reminder time for the note
        """
        super().__init__(content, created_at)  # Call parent's __init__
        self.reminder_time = reminder_time
     
    def display(self):
        return f"Note: {self.content}\nCreated at: {self.created_at}"
     
    
    
      

class NoteManager:
    """
    A class to manage notes.
    """
    def __init__(self):
        self.notes = []
        self.next_note_id = 1  # Initialize next_note_id        
    
    def add_note(self, note_type, content, reminder_time=None):
        if note_type == "text":
            new_note = TextNote(content, datetime.now())
        elif note_type == "reminder":
            if reminder_time is None:
                print("Reminder notes require a reminder time.")
                return
            try:
                reminder_time = datetime.strptime(reminder_time, "%Y-%m-%d %I:%M %p")
            except ValueError:
                print("Invalid reminder time format. Please use䣨-MM-DD HH:MM AM/PM")
                return
            new_note = ReminderNote(content, datetime.now(), reminder_time)
        else:
            print("INVALID NOTE TYPE")
            return

        self.notes.append({"id": self.next_note_id, "note": new_note})
        self.next_note_id += 1
        print("Note added")
        
       
    def delete_note (self,note_id):
        """To delete note by its ID

        Args:
            note_id (int): The note's ID
        """
        for i,note_data in enumerate(self.notes): #Iterates through the lists of notes
            if note_data["id"] == note_id: #checks if the id exists
                del self.notes[i] #deletes the note
                print("Note deleted")
                return
        print("Note ID doesn't exist") # Print once if ID is not found
            
    def show_notes (self):
        """To show all notes
        """
        if not self.notes: #checks if the list is empty
            print ("No notes to display: Note list is empty")
        for note_data in self.notes:
            print("ID: " + str(note_data['id']))  # Print the ID
            print(note_data['note'].display())  # Call the display() method!
        
            
        
    def search_note(self, search_term):
        """To search for a keyword in note

        Args:
            search_term (string): The keyword to search for
        """
        results = []
        search_term = search_term
        
        for note_data in self.notes:  # Iterate through dictionaries
            note = note_data["note"]  # Get the Note object
            if search_term in note.content.lower():
                results.append(note_data)  # Append the dictionary

        if results:
            print("Search Results:")
            for note_data in results:
                print(note_data["note"].display())  # Display the Note object
                print("-" * 20)
        else:
            print("No matching notes found.")
        

# Create a notes manager
my_notes = NoteManager()

while True:
    print("\nNote Manager Menu:")
    print("A) Add note")
    print("B) Delete note by ID")
    print("C) Show all notes")
    print("D) Search note")
    print("E) Exit")

    choice = input("Enter your choice (A/B/C/D/E): ").upper()  # Convert to uppercase for easier comparison
    
    if choice == "A":
        note_type = input("ENTER NOTE TYPE (text/reminder): ").lower()
        content =input("ENTER NOTE CONTENT: ")
        if note_type == "reminder":
            reminder_time= input ("ENTER REMINDER TIME (YYYY-MM-DD HH:MM AM/PM): ")
            my_notes.add_note(note_type, content)
        else:
            my_notes.add_note(note_type, content)
            
    elif choice == "B":
        try:
            note_id = int(input("ENTER NOTE ID: "))
            my_notes.delete_note(note_id)
        except ValueError:
            print ("Invalid input: The input should be a number")
            
            
    elif choice == "C":
       my_notes.show_notes()
            
    
    elif choice == "D":
        search_term = input("ENTER SEARCH KEYWORD: ").lower()
        my_notes.search_note(search_term)
               
        
    elif choice == "E":
        print("Exiting Note Manager.")
        break
    
    else:
        print("Invalid choice, Please try again")

