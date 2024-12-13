project = float(input("Enter project score: "))
internal = float(input("Enter internal score: "))
external = float(input("Enter external score: "))
if project >= 50 and internal >=50 and external >= 50:
    total=(project*0.70)+(internal*0.10)+(external*0.20)
    print(total)
    if(total>90):
        print("A grade")
    elif(80> total <=90):
        print("B grade")
    else:
        print("C grade")

if(project<50):
    print(f"failed in project {project}")
if(internal<50):
    print(f"failed in internal {internal}")
if(external<50):
    print(f"failed in external {external}")


