def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


print(add_item_buggy("Tea"), add_item_buggy("Vada"))

print(add_item("Tea"), add_item("Vada"))


def calculate_bill(amount, gst=5):
    tax = amount * gst / 100
    total = amount + tax
    return total, tax


total, tax = calculate_bill(1000)

print("Total Amount:", total)
print("GST:", tax)


# Local and global scope
x = 10


def display():
    global x
    x = 20
    print("Inside function:", x)


display()
print("Outside function:", x)


# Nonlocal scope
def outer():
    value = 10

    def inner():
        nonlocal value
        value = 30

    inner()
    print("Nonlocal value:", value)


outer()
