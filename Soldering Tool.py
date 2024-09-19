import math

def soldering_tool():
    print("Soldering Tool Method")

    # awg to diameter mapping (mm)
    awg_to_diameter = {
        0000: 11.684,  # 4/0 AWG
        000: 10.405,   # 3/0 AWG
        00: 9.266,     # 2/0 AWG
        0: 8.252,      # 1/0 AWG
        1: 7.348,
        2: 6.544,
        3: 5.827,
        4: 5.189,
        5: 4.621,
        6: 4.115,
        7: 3.665,
        8: 3.264,
        9: 2.906,
        10: 2.588,
        11: 2.305,
        12: 2.053,
        13: 1.828,
        14: 1.628,
        15: 1.450,
        16: 1.291,
        17: 1.150,
        18: 1.024,
        19: 0.912,
        20: 0.8128,
        21: 0.7239,
        22: 0.644,
        23: 0.5733,
        24: 0.5106,
        25: 0.4547,
        26: 0.4039,
        27: 0.3606,
        28: 0.3211,
        29: 0.2860,
        30: 0.2546,
        31: 0.2268,
        32: 0.2019,
        33: 0.1798,
        34: 0.1601,
        35: 0.1426,
        36: 0.1270,
        37: 0.1131,
        38: 0.1007,
        39: 0.0897,
        40: 0.0799
    }


    # inputs
    awg = int(input("Enter the wire gauge (AWG): "))
    if awg not in awg_to_diameter:
        print("Error: Invalid AWG. Please enter an AWG between 0000 and 40.")
        return

    diameter = awg_to_diameter[awg]
    print(f"\nDiameter for AWG {awg}: {diameter} mm")

    # clamp force
    k = 100  # arbitrary constant for clamp force calculation?? idk got from google
    clamp_force = k * diameter

    print(f"Calculated clamp force: {clamp_force:.2f} units")

    # solder volume
    cross_sectional_area = math.pi * (diameter / 2) ** 2
    solder_volume = cross_sectional_area * 0.1  # 0.1 mm length for solder

    print(f"Calculated solder volume needed: {solder_volume:.6f} mm³")

    print("\nSimulating soldering process:")
    print(f"Clamping wires with force {clamp_force:.2f} units")
    print(f"Ejecting {solder_volume:.6f} mm³ of superheated solder into the joint")

if __name__ == "__main__":
    soldering_tool()
'''
wire gauge: 18
'''