repair_categories = ["Electronics", "Furniture", "Appliances", "Vehicles"]

# List of equipment with the following information: an id, a description, a repair cost, and a Category.
equipment_list = [
    {"id": 1, "description": "Laptop", "repair_cost": 150.0, "category": "Electronics"},
    {"id": 2, "description": "Sofa", "repair_cost": 200.0, "category": "Furniture"},
    {"id": 3, "description": "Washing Machine", "repair_cost": 300.0, "category": "Appliances"},
    {"id": 4, "description": "Car", "repair_cost": 500.0, "category": "Vehicles"},
    {"id": 5, "description": "Smartphone", "repair_cost": 100.0, "category": "Electronics"},
    {"id": 6, "description": "Dining Table", "repair_cost": 250.0, "category": "Furniture"},
    {"id": 7, "description": "Refrigerator", "repair_cost": 400.0, "category": "Appliances"},
    {"id": 8, "description": "Motorcycle", "repair_cost": 350.0, "category": "Vehicles"},
]

# Function to add an equipment item to the list of equipment.
def add_equipment(equipment_list, equip_id, description, repair_cost, category):
    if any(item["id"] == equip_id for item in equipment_list):
        raise ValueError(f"Equipment ID '{equip_id}' already exists.")
    
    if category not in repair_categories:
        raise ValueError(f"Category '{category}' is not valid. Choose from {repair_categories}.")
    
    new_equipment = {
        "id": equip_id,
        "description": description,
        "repair_cost": repair_cost,
        "category": category
    }
    equipment_list.append(new_equipment)


# Function to remove an equipment item from the list of equipment.
def remove_equipment(equipment_list, equip_id):
    before = len(equipment_list)
    equipment_list[:] = [item for item in equipment_list if item["id"] != equip_id]
    return len(equipment_list) < before


# Function to display details of an equipment item.
def display_equipment(equipment):
    print(f"ID: {equipment['id']}")
    print(f"Description: {equipment['description']}")
    print(f"Repair Cost: ${equipment['repair_cost']:.2f}")
    print(f"Category: {equipment['category']}")

# Function to show the full list of equipment.
def show_all_equipment(equipment_list):
    for equipment in equipment_list:
        display_equipment(equipment)
        print("\n" + "-" * 20)



# Function to search by equipment description, returning the equipment if found.
def search_equipment_by_description(equipment_list, description):
    for equipment in equipment_list:
        if equipment["description"].lower() == description.lower():
            return equipment
    return None

# Function to search by a substring of the description, returning matching equipment if found.
def search_equipment_by_substring(equipment_list, substring):
    matching_equipment = []
    for equipment in equipment_list:
        if substring.lower() in equipment["description"].lower():
            matching_equipment.append(equipment)
    return matching_equipment

# List of repair requests with the following information: an id, a date, and a list of equipment.
repair_requests = [
    {"id": 1, "date": "2024-01-15", "equipment": [equipment_list[0].copy(), equipment_list[2].copy()]},
    {"id": 2, "date": "2024-02-20", "equipment": [equipment_list[1].copy(), equipment_list[3].copy()]},
    {"id": 3, "date": "2024-03-10", "equipment": [equipment_list[4].copy(), equipment_list[5].copy()]},
]

# Function to add an equipment item to a repair request with a quantity (qty).
def add_equipment_to_repair_request(repair_request, equipment, qty):
    for i in range(qty):
        repair_request["equipment"].append(equipment.copy())

# Function to remove an equipment item from a repair request.
def remove_equipment_from_repair_request(repair_request, equipment_id):
    repair_request["equipment"] = [item for item in repair_request["equipment"] if item["id"] != equipment_id]

# Function to display the details of a repair request.
def display_repair_request(repair_request):
    print(f"Repair Request ID: {repair_request['id']}")
    print(f"Date: {repair_request['date']}")
    print("Equipment to be repaired:")
    for equipment in repair_request["equipment"]:
        display_equipment(equipment)
        print("\n" + "-" * 20)

# Function that returns the total repair cost of a request.
def total_repair_cost(repair_request):
    total_cost = sum(equipment["repair_cost"] for equipment in repair_request["equipment"])
    return total_cost

# Function to add a repair request to the list of repair requests.
def add_repair_request(repair_requests, req_id, date, equipment):
    if any(request["id"] == req_id for request in repair_requests):
        raise ValueError(f"Repair Request ID '{req_id}' already exists. Please enter another ID.")
    
    new_request = {
        "id": req_id,
        "date": date,
        "equipment": equipment
    }
    repair_requests.append(new_request)


# Function to remove a repair request from the list of requests.
def remove_repair_request(repair_requests, req_id):
    repair_requests[:] = [request for request in repair_requests if request["id"] != req_id]

# Function to display all repair requests.
def display_all_repair_requests(repair_requests):
    for request in repair_requests:
        display_repair_request(request)
        print("\n" + "-" * 20)


# Function that returns the total global cost of all repair requests.
def total_global_repair_cost(repair_requests):
    total_cost = sum(total_repair_cost(request) for request in repair_requests)
    return total_cost

# Menu
def menu():
    while True:
        print("\n" + "=" * 30 + "\n" )
        print("Repair Management System")
        print("1. Show all equipment")
        print("2. Add equipment")
        print("3. Remove equipment")
        print("4. Search equipment by description")
        print("5. Search equipment by substring")
        print("6. Show all repair requests")
        print("7. Add repair request")
        print("8. Remove repair request")
        print("9. Total global repair cost")
        print("0. Exit")
        print("\n" + "=" * 30 + "\n" )


        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_equipment(equipment_list)

        elif choice == '2':
            while True:
                try:
                    equip_id = int(input("Enter equipment ID: "))
                    if equip_id == 0:
                        break
                    description = input("Enter equipment description: ")
                    if description == 0:
                        break
                    repair_cost = float(input("Enter repair cost: "))
                    if repair_cost == 0:
                        break
                    category = input(f"Enter category ({', '.join(repair_categories)}): ")
                    if category == 0:
                        break

                    add_equipment(equipment_list, equip_id, description, repair_cost, category)
                    print("Equipment added successfully.")
                    break 

                except ValueError as e:
                    print("Error:", e)
                    print("Please enter a different ID/category.\n")



        elif choice == '3':
            try:
                equip_id = int(input("Enter equipment ID to remove: "))
                if equip_id == 0:
                    continue
                removed = remove_equipment(equipment_list, equip_id)
                if removed:
                    print("Equipment removed successfully.")
                else:
                    print("Equipment ID not found.")
            except ValueError:
                print("Invalid ID.")



        elif choice == '4':
            description = input("Enter equipment description to search: ")
            if description =="0":
                continue
            equipment = search_equipment_by_description(equipment_list, description)
            if equipment:
                display_equipment(equipment)
            else:
                print("Equipment not found.")

        elif choice == '5':
            substring = input("Enter substring to search in descriptions: ")
            if substring =="0":
                continue
            matching_equipment = search_equipment_by_substring(equipment_list, substring)
            if matching_equipment:
                for equipment in matching_equipment:
                    display_equipment(equipment)
                    print("-" * 20)
            else:
                print("No matching equipment found.")

        elif choice == '6':
            display_all_repair_requests(repair_requests)

        elif choice == '7':
            while True:
                try:
                    req_id = int(input("Enter repair request ID: "))
                    if req_id == 0:
                        break
                    date = input("Enter date (YYYY-MM-DD): ")
                    if date =="0":
                        break
                    equipment_ids = input("Enter equipment IDs to add (comma separated, or leave empty): ").strip()
                    if equipment_ids =="0":
                        break
                    equipment_to_add = []

                    if equipment_ids:
                        for eid_str in equipment_ids.split(','):
                            try:
                                eid = int(eid_str.strip())
                            except ValueError:
                                print(f"Skipping invalid ID '{eid_str.strip()}'")
                                continue

                            equipment = next((item for item in equipment_list if item["id"] == eid), None)
                            if equipment:
                                equipment_to_add.append(equipment.copy())
                            else:
                                print(f"Equipment with ID {eid} not found; skipping.")

                    add_repair_request(repair_requests, req_id, date, equipment_to_add)
                    print("Repair request added successfully.")
                    break  # exits  only when request ID is valid
                except ValueError as e:
                    print("Error:", e)
        elif choice == '8':
            try:
                req_id = int(input("Enter repair request ID to remove: "))
                if req_id =="0":
                        continue
                remove_repair_request(repair_requests, req_id)
                print("Repair request removed successfully.")
            except ValueError:
                print("Invalid ID.")

        elif choice == '9':
            total = total_global_repair_cost(repair_requests)
            print(f"Total global repair cost: ${total:.2f}")

        elif choice == '0':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()