
from datetime import datetime

def add_returned_book(book_id):
    try:
        with open("book_log.txt", "a", encoding="utf-8") as file:
            date = datetime.now().strftime("%Y-%m-%d")
            file.write(f"{date},{book_id}\n")

        print("Book return recorded successfully.")

    except (OSError, PermissionError) as error:
        try:
            with open("error_log.txt", "a", encoding="utf-8") as log:
                log.write(
                    f"{datetime.now()}: {type(error).__name__}: {error}\n"
                )
        except OSError:
            print("Unable to save the error log.")

        print("Error:", error)


while True:
    book_id = input("Enter book ID (0 to exit): ")

    if book_id == "0":
        break

    add_returned_book(book_id)
