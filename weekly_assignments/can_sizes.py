import math

def main():
    name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    for i in range(len(name)):
        name = name[i]

    for i in radius(len(radius)):
        radius = radius[i]

    for i in height(len(height)):
        height = height[i]

    for i in cost(len(cost)):
        cost = cost[i]

print(name, radius, height, cost)
    
def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_serface_area(radius, height):
    serface_area = math.pi * radius * (radius + height)
    return serface_area

main()