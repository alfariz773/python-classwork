try:
    title = input("Enter the book title: ")
    if not title.replace(" ", "").isalpha():
        raise TypeError("Error: Book title should contain only alphabets and spaces")

    year = input("Enter the publication year: ")
    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise TypeError("Error: Year must be a 4-digit number starting with 19 or 20")

    print(f"\nBook Recorded: '{title}' ({year})")

except Exception as e:
    print(e)
    
finally:
    print("\nProgram finished (with or without error).")
