# Import the standard math module so that
# math.pi can be used in this program
import math

def main():
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    for i in range(len(names)):       
        volume = compute_volume(radiuses[i], heights[i])
        surface = compute_surface_area(radiuses[i], heights[i])
        storage_efficiency = volume / surface
        print(f"{names[i]} {storage_efficiency:.2f}")

def compute_volume(radius, height):
    """Compute and return the volume of a cylinder
    
    parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    return: the volume of the cylinder

    """
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder

    parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    return: the surface area of the cylinger
    
    """
    surface_area = 2 * math.pi *radius * (radius + height)
    return surface_area

# Starat this program by
# calling the main function
main()