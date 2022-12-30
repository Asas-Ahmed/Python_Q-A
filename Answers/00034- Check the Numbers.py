n = int(20)
list = list(map(int, input(
    "Enter 20 integers (Space-Seperated): ").strip().split()))

po_count, ne_count, ze_count = 0, 0, 0

for num in list:
    if num > 0:
        po_count += 1
    elif num == 0:
        ze_count += 1
    else:
        ne_count += 1
    
print("\nPostive numbers in the list: ",po_count)
print("Negative numbers in the list: ",ne_count)
print("Zeros in the list: ",ze_count)
