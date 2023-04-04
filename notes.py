import argparse
import json
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="path to notes file", default="notes.json")
args = parser.parse_args()

NOTES_FILE = args.file

def read_notes():
    if not os.path.exists(NOTES_FILE):
        return[]
    
    with open(NOTES_FILE) as f:
        try:
            notes = json.load(f)
        except json.decoder.JSONDecodeError:
            notes = []

    return notes

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)
 
def add_note():
    notes = read_notes()

    title = input("Заголовок:")
    content = input("Содержание:")
    timestamp = int(time.time())

    notes.append({"id": len(notes), "title": title, "content": content, "timestamp": timestamp})

    save_notes(notes)

def edit_note():
    notes = read_notes()

    note_id = int(input("Идентификатор заметки:"))

    for note in notes:
        if note["id"] == note_id:
            note["title"] = input(f"New title({note['title']}):") or note["title"]
            note["content"] = input(f"New content({note['content']}):") or note["content"]
            note["timestamp"] = int(time.time())
            break
    else:
        print(f"Заметка с идентификатором {note_id} не найдена")
        return
        
    save_notes(notes)

def delete_note():
    notes = read_notes()

    note_id = int(input("Идентификатор заметки:"))

    for i, note in enumerate(notes):
        if note["id"] == note_id:
            del notes[i]
            break
        else:
            print(f"Заметка с идентификатором {note_id} не найдена")
            return
        
    save_notes(notes)

def list_notes():
    notes = read_notes()

    if notes:
        for note in notes:
            print(f"[{note['id']}]{note['title']}({time.ctime(note['timestamp'])})")
    else:
        print("Нет заметок")

    print()

while True:
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print('3. Удалить заметку')
    print("4. Список заметок")
    print("0. Выход")

    choice = input(">")

    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        list_notes()
    elif choice == "0":
        break
    else:
        print("Неверный выбор")
