import pytest
import unittest
from unittest.mock import patch
from SmartNoteManager import Note, TextNote, ReminderNote, NoteManager
from datetime import datetime

def test_note_init():
    with patch('datetime.datetime') as mock_datetime:
        mocked_now = datetime(2025, 3, 9, 12, 0, 0) #capture the mocked datetime.
        mock_datetime.now.return_value = mocked_now #set the return value.
        note = Note("Text content", mocked_now) #pass the mocked value.
        assert note.content == "Text content"
        assert note.created_at == mocked_now #assert against the mocked value.

#TEST FOR VALID REMINDERNOTE       
def test_add_valid_text_note(capsys):
    note_manager = NoteManager()
    note_manager.add_note("text", "Test text note")
    assert len(note_manager.notes) == 1
    note = note_manager.notes[0]["note"]
    assert isinstance(note, TextNote)
    assert note.content == "Test text note"
    assert note.created_at is not None
    assert note_manager.notes[0]["id"] == 1
    

#TEST FOR VALID REMINDERNOTE    
def test_add_valid_reminder_note(capsys):  
    note_manager = NoteManager()
    reminder_time_str = "2025-03-09 12:00 AM"
    reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %I:%M %p")
    note_manager.add_note("reminder", "Test reminder note", reminder_time_str)
    assert len(note_manager.notes) == 1
    note = note_manager.notes[0]["note"]
    assert isinstance(note, ReminderNote)
    assert note.content == "Test reminder note"
    assert note.reminder_time == reminder_time
    assert note.created_at is not None

#TEST FOR INVALIDNOTE TYPE  
def test_add_invalid_note_type(capsys):
    note_manager = NoteManager()
    note_manager.add_note("invalid_type", "Test invalid type")
    captured = capsys.readouterr()
    assert "INVALID NOTE TYPE"  in captured.out
    assert len(note_manager.notes) == 0


#TEST FOR INVALID REMINDER TIME FORMAT
def test_add_invalid_reminder_time_format(capsys):
    note_manager = NoteManager()
    note_manager.add_note("reminder", "Test reminder invalid time", "invalid")
    captured = capsys.readouterr()
    assert "Invalid reminder time format. Please use䣨-MM-DD HH:MM AM/PM" in captured.out
    assert len(note_manager.notes) == 0
        
    
#TEST FOR DELETING_NOTE BY ID
def test_deleting_note(capsys):
    note_manager = NoteManager()
    note_manager.add_note("text", "Note to delete")  # Add a note
    note_id = note_manager.notes[0]["id"]  # Get the ID of the added note
    note_manager.delete_note(note_id)
    captured = capsys.readouterr()
    assert "Note deleted"  in captured.out
    assert len(note_manager.notes) == 0
    
    
#TEST FOR DELETING NONE EXISTING_NOTE BY ID
def test_for_deleting_non_existing_note_id(capsys):
    note_manager = NoteManager()
    note_manager.add_note("text", "Note to delete")  # Add a note
    note_manager.delete_note(99)
    captured = capsys.readouterr()
    assert "Note ID doesn't exist"  in captured.out
    assert len(note_manager.notes) == 1
    
    
#TEST FOR SHOW_ALL_NOTES
def test_to_show_all_note(capsys):
    note_manager = NoteManager()
    note_manager.add_note("text", "Note to display")  # Add a note
    note_manager.show_notes() 
    captured = capsys.readouterr()
    assert "Note to display" in captured.out
    assert "ID: 1" in captured.out #verify the ID is printed.
    

#TEST FOR SHOW EMPTY_NOTE LIST
def test_to_show_empty_note_list(capsys):
    note_manager = NoteManager()
    note_manager.show_notes() 
    captured = capsys.readouterr()
    assert "No notes to display: Note list is empty" in captured.out
       
    
#TEST FOR  SEARCHING KEYWORD__NOTE
def test_search_keyword_note(capsys):
    note_manager = NoteManager()
    note_manager.add_note("text", "This is a test note.")  # Add a note
    note_manager.search_note("test")  # Search for the keyword "test"
    captured = capsys.readouterr()
    assert "This is a test note." in captured.out
    
    note_manager.search_note("nonexistent") #search for a non existant note
    captured2 = capsys.readouterr()
    assert "No matching notes found." in captured2.out
