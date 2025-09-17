import streamlit as st

ROWS = 5
COLS = 5
PARKING_LOT = [[0 for _ in range(COLS)] for _ in range(ROWS)]
PARKED_CARS = {}

def find_nearest_spot():
    for r in range(ROWS):
        for c in range(COLS):
            if PARKING_LOT[r][c] == 0:
                return (r, c)
    return None

def park_car(license_plate):
    spot = find_nearest_spot()
    if spot:
        row, col = spot
        PARKING_LOT[row][col] = 1
        PARKED_CARS[license_plate] = (row, col)
        return f"Car with license plate {license_plate} parked at spot ({row}, {col})."
    else:
        return "Sorry, the parking lot is full."

def exit_parking_lot(license_plate):
    if license_plate in PARKED_CARS:
        row, col = PARKED_CARS[license_plate]
        PARKING_LOT[row][col] = 0
        del PARKED_CARS[license_plate]
        return f"Car with license plate {license_plate} exited from spot ({row}, {col})."
    else:
        return f"Car with license plate {license_plate} not found."

def display_parking_lot():
    st.write("Parking Lot Status (0 = Vacant, 1 = Occupied):")
    for row in PARKING_LOT:
        st.write(" ".join(map(str, row)))

st.title("Smart Parking Lot System")

action = st.selectbox("What would you like to do?", ["Park a Car", "Exit a Car", "View Parking Lot Status"])

if action != "View Parking Lot Status":
    license_plate = st.text_input("Enter the car's license plate:")

if st.button("Submit"):
    if action == "Park a Car":
        st.success(park_car(license_plate))
    elif action == "Exit a Car":
        st.success(exit_parking_lot(license_plate))
    elif action == "View Parking Lot Status":
        pass

display_parking_lot()
