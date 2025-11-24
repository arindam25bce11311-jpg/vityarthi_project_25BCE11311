import csv
import os
from datetime import datetime

holdname = 'crops_sched.csv'

def load_sched():
    if not os.path.exists(holdname):
        return []
    with open(holdname, 'r') as f:
        return list(csv.DictReader(f))

def save_sched(schedule1):
    with open(holdname, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['crop_namez', 'plant_datez', 'harvest_datez', 'quantity'])
        writer.writeheader()
        writer.writerows(schedule1)

def add_crop(schedule1):
    print("\nAdd Crop")
    crpame = input("crop name: ")
    plntdate = input("plant date (dd/mm/yyyy): ")
    hrvstdate = input("harvest date (dd/mm/yyyy): ")
    quantity = input("quantity: ")
    
    schedule1.append({
        'crop_namez': crpame,
        'plant_datez': plntdate,
        'harvest_datez': hrvstdate,
        'quantity': quantity
    })
    save_sched(schedule1)
    print("Crop has been added")

def view_sched(schedule1):
    if not schedule1:
        print("\nNo crops are in schedule.")
        return
      
    print("\nharvest schedule")
    for i, crop in enumerate(schedule1, 1):
        print(f"\n{i}. {crop['crop_namez']} - Quantity: {crop['quantity']}")
        print(f"   Plant: {crop['plant_datez']} | Harvest: {crop['harvest_datez']}")

def delcrop(schedule1):
    if not schedule1:
        print("\nno crops to delete.")
        return
    
    view_sched(schedule1)
    try:
        index = int(input("\nenter crop no. to delete: ")) - 1
        if 0 <= index < len(schedule1):
            removed = schedule1.pop(index)
            save_sched(schedule1)
            print(f"Deleted: {removed['crop_namez']}")
        else:
            print("wrong no.")
    except ValueError:
        print("wrong input.")

def main():
    sched = load_sched()
    
    while True:
        print("\nharvest planner")
        print("1. Add crop")
        print("2. View schedule")
        print("3. Delete crop")
        print("4. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            add_crop(sched)
        elif choice == '2':
            view_sched(sched)
        elif choice == '3':
            delcrop(sched)
        elif choice == '4':
            print("byebye mate")
            break
        else:
            print("invalid choice.")

if __name__ == "__main__":
    main()