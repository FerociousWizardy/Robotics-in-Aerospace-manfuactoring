import math

def epoxy_application():
    print("Epoxy Application Method")

    # get parameters
    ID = float(input("Enter the Inner Diameter (ID) of the shell in mm: "))
    tolerance = float(input("Enter the tolerance (gap between insulator and shell) in mm: "))
    length = float(input("Enter the length over which epoxy is applied in mm: "))

    r_outer = ID / 2
    r_inner = r_outer - tolerance

    if r_inner <= 0:
        print("Error: Tolerance is too large, resulting in negative or zero inner radius.")
        return

    cross_sectional_area = math.pi * (r_outer**2 - r_inner**2)
    volume_of_epoxy = cross_sectional_area * length

    print(f"\nCross-sectional area of gap: {cross_sectional_area:.4f} mm²")
    print(f"Volume of epoxy needed: {volume_of_epoxy:.4f} mm³")

    # motor movement in circular motion
    steps = 36  # 10 degrees per step
    angle_increment = 360 / steps

    print("\nSimulating motor movement:")
    for step in range(steps):
        angle = step * angle_increment
        x = r_outer * math.cos(math.radians(angle))
        y = r_outer * math.sin(math.radians(angle))
        print(f"At angle {angle:.1f}°, position: x = {x:.2f} mm, y = {y:.2f} mm")

if __name__ == "__main__":
    epoxy_application()

'''
sample input
id: 50
tolerance 1
length 100
'''