sal = float(input("Total salary: "))
bill1 = float(input("first bill: "))
bill2 = float(input("sec bill: "))
bill3 = float(input("third bill: "))
total = bill1 + bill2 + bill3
percentage = (total/sal)*100
print(f"Total {total}")
print(f"percent {percentage:.2f}%")
