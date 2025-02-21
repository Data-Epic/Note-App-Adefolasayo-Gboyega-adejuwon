from datetime import datetime

#create base class Note and its attributes
class Note:
    def __init__(self, content,created_at):
        self.content= content
        self.created_at=datetime.now()
        
     #create a method to show note details.        
    def display(self):
        return f"Note: {self.content}\nCreated at: {self.created_at}"
    
    
    
class TextNote(Note):
    def __init__(self,content,created_at):
        super().__init__(content, created_at)  # Call parent's __init__
    def display(self):
        return f"Note: {self.content}\nCreated at: {self.created_at}"
    
    
    
class ReminderNote(Note):
    def __init__(self,content, created_at, ReminderDate, ReminderTime):
        super().__init__(content, created_at)  # Call parent's __init__
        self.ReminderDate=ReminderDate
        self.ReminderTime = ReminderTime
     
    def display(self):
        return f"Note: {self.content}\nCreated at: {self.created_at}"
     
    
    
      

class NoteManager:
    
    def __init__(self):
        self.notes = []
    
    def add_note (self,note_type,content,reminder_time=None):
        if note_type == "text":
            new_note = TextNote(content,) #adds a new text note
        elif note_type =="reminder":
            new_note = ReminderNote(content, reminder_time) #adds a new reminder note
        
        self.notes.append({"id":self.next_note_id,"note":new_note})
        self.next_note_id += 1 # increases note id by 1
        print("Note added")
        
       
    def delete_note (self,note_id):
        for i,note_data in enumerate(self.notes): #Iterates through the lists of notes
            if note_data["id"] == note_id: #checks if te id exists
                del self.notes[note_id] #deletes the note
                print("Note deleted")
            
    def show_note (self):
        if not self.notes: #checks if the list is empty
            print ("List is empty")
        for note_data in self.notes:
            print("ID: " + str(note_data['id']))  # Print the ID
            print(note_data['note'].display())  # Call the display() method!
        
            
        
    def search_note (self):
        pass
        

    
# Create a notes manager
my_notes = NoteManager()

# Add a text note
my_notes.add_note("text", "Review Python OOP concepts")

# Add a reminder note
my_notes.add_note("reminder", "Project deadline", "2025-03-10 10:00 AM")

# Show all notes
my_notes.show_notes()

# Search for a note
my_notes.search_notes("deadline")

# Delete a note
my_notes.delete_note(1)