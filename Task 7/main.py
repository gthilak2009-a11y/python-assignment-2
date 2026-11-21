import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


def original_solution(parts):
    text = ""

    for item in parts:
        text += item + ";"

    return text


def redesigned_solution(parts):
    return "".join(item + ";" for item in parts)


start = time.perf_counter()
original = original_solution(items)
original_time = time.perf_counter() - start


start = time.perf_counter()
redesigned = redesigned_solution(items)
redesigned_time = time.perf_counter() - start


print("Original length:", len(original))
print("Redesigned length:", len(redesigned))

print("Same output:", original == redesigned)

print(f"Original time: {original_time:.4f} seconds")
print(f"Redesigned time: {redesigned_time:.4f} seconds")

if redesigned_time < original_time:
    print("Redesigned solution is faster.")
else:
    print("Original solution is faster on this run.")
