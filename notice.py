import json
import os
import datetime

def load_notes():
    if not os.path.exists("notes.json"):
        return []
    with open("notes.json", "r") as f:
        return json.load(f)

def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def add_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    created_at = datetime.datetime.now().isoformat()
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": created_at
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата создания: {note['created_at']}")
        print(f"Дата последнего изменения: {note['updated_at']}")
        print()

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note["title"] = title
            note["body"] = body
            note["updated_at"] = datetime.datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

def filter_notes_by_date():
    notes = load_notes()
    date_str = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    filtered_notes = [note for note in notes if note["created_at"].startswith(date_str)]
    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата создания: {note['created_at']}")
        print(f"Дата последнего изменения: {note['updated_at']}")
        print()

def main():
    while True:
        print("Введите команду:")
        print("1. Добавить заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Фильтровать заметки по дате")
        print("6. Выйти")
        choice = input("Ваш выбор: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            filter_notes_by_date()
        elif choice == "6":
            break
        else:
            print("Неверная команда")

if __name__ == "__main__":
    main() 