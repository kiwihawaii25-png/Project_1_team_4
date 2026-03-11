def clear_terminal() :
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def header() :
    print("\033[36m")
    print("*" * 50)
    print("          WING DEFLECTION CALCULATOR\n")
    print("            On a Wing and a Prayer\n\n")
    print("               Brought to you by\n")
    print("       Alessandra, Aeryn, Kyra, Jacob, Jay")
    print("*" * 50)
    print("\033[0m")

def calculate_air_density(h):
 
    L = 0.0065          #  Change in air temp at altitude
    g = 9.81            #  Gravity
    R = 287             #  Gas Constant for air
    rho0 = 1.225        #  Air density at sea level
    T0 = 288.15         #  Temp in K
 
    rho = rho0 + (1 - (L * h) / T0) ** ((g / (R * L)) - 1)  #  Claculate air density at elevation
 
    return rho

def get_flight_conditions():
    air_speed = float(input("\nEnter Air Speed (kts): "))
    altitude = float(input("Enter Altitude (meters): "))
 
    v = air_speed * 0.51444
 
    return v, altitude

def display_results(plane, material, lift, deflection, L_wing):
 
    print("\n" + "*" * 40)
    print(f"AIRCRAFT: {plane}")
    print(f"MATERIAL: {material}")
    print(f"TOTAL LIFT: {lift:,.3f} N")
    print(f"Estimated Wingtip Deflection: {deflection * 100:.3f} cm")
 
    if deflection > (L_wing * 0.2):
        print("Warning: Structural limits likely exceeded!")
 
    if "Concrete" in material:
        print("A plane with concrete wings isn't going to get off the ground.")