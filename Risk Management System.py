risk_logs = {}
mitigation_strategies = {}


def create_risk_log(project_name, risk_description):
    risk_id = len(risk_logs) + 1
    risk_logs[risk_id] = {
        "project_name": project_name,
        "risk_description": risk_description,
        "mitigation_id": None
    }
    return risk_id

def read_risk_log(risk_id):
    return risk_logs.get(risk_id)

def update_risk_log(risk_id, project_name=None, risk_description=None):
    if risk_id in risk_logs:
        if project_name:
            risk_logs[risk_id]["project_name"] = project_name
        if risk_description:
            risk_logs[risk_id]["risk_description"] = risk_description
        print(f"Risk log {risk_id} updated.")
    else:
        print(f"Risk log {risk_id} not found.")

def delete_risk_log(risk_id):
    if risk_id in risk_logs:
        del risk_logs[risk_id]
        print(f"Risk log {risk_id} deleted.")
    else:
        print(f"Risk log {risk_id} not found.")


def identify_project_risks():
    project_name = input("Enter project name: ")
    risk_description = input("Enter risk description: ")
    risk_id = create_risk_log(project_name, risk_description)
    print(f"Risk '{risk_description}' identified in project '{project_name}' with risk ID {risk_id}")


def implement_risk_mitigation():
    risk_id = int(input("Enter risk ID for mitigation: "))
    if risk_id not in risk_logs:
        print(f"Risk ID {risk_id} not found.")
        return
    mitigation_id = len(mitigation_strategies) + 1
    mitigation_description = input("Enter mitigation description: ")
    mitigation_strategies[mitigation_id] = {
        "risk_id": risk_id,
        "mitigation_description": mitigation_description
    }
    risk_logs[risk_id]["mitigation_id"] = mitigation_id
    print(f"Mitigation '{mitigation_description}' implemented for risk ID {risk_id}")


def display_risk_logs():
    if not risk_logs:
        print("No risk logs available.")
    else:
        for risk_id, details in risk_logs.items():
            print(f"ID: {risk_id}, Project: {details['project_name']}, Risk: {details['risk_description']}, Mitigation ID: {details['mitigation_id']}")


def menu():
    while True:
        print("\nRisk Management System Menu")
        print("1. Identify Project Risk")
        print("2. Implement Risk Mitigation")
        print("3. Display Risk Logs")
        print("4. Update Risk Log")
        print("5. Delete Risk Log")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            identify_project_risks()
        elif choice == '2':
            implement_risk_mitigation()
        elif choice == '3':
            display_risk_logs()
        elif choice == '4':
            risk_id = int(input("Enter risk ID to update: "))
            project_name = input("Enter new project name (leave blank to keep current): ")
            risk_description = input("Enter new risk description (leave blank to keep current): ")
            update_risk_log(risk_id, project_name or None, risk_description or None)
        elif choice == '5':
            risk_id = int(input("Enter risk ID to delete: "))
            delete_risk_log(risk_id)
        elif choice == '6':
            print("Exiting the Risk Management System.")
            break
        else:
            print("Invalid choice, please try again.")

menu()
