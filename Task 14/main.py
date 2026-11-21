
import re
import time

contacts = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Ravi Kumar",
        "phone": "9840012345",
        "email": "ravi.kumar@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "+91 98765 43210",
        "email": "priya@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9876543211",
        "email": ""
    },
    {
        "name": "Priya",
        "phone": "9876543210",
        "email": "priya@gmail.com"
    }
]

def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone)

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    return digits

def merge_contacts(contacts):
    merged = {}

    for contact in contacts:
        phone = normalize_phone(contact.get("phone", ""))

        if not phone:
            continue

        if phone not in merged:
            merged[phone] = {
                "name": contact.get("name", "Unknown"),
                "numbers": set(),
                "emails": set()
            }

        if contact.get("name"):
            merged[phone]["name"] = contact["name"]

        merged[phone]["numbers"].add(contact["phone"])

        if contact.get("email"):
            merged[phone]["emails"].add(contact["email"])

    return merged

start = time.time()

result = merge_contacts(contacts)

end = time.time()

print("Merged Contacts:")

for phone, details in result.items():
    print("\nName:", details["name"])
    print("Phone numbers:", sorted(details["numbers"]))
    print("Emails:", sorted(details["emails"]))

print("\nExecution time:", end - start, "seconds")
