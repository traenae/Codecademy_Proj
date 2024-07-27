import colors_r_fun
from colors_r_fun import *
#myColors()

name = input("What is your name? " )
weight = float(input("How much does your package weigh in pounds? "))

if weight <= 2:
    ground_shipping = (1.50 * weight) + 20
elif (weight > 2) and (weight <= 6):
    ground_shipping = (3.00 * weight) + 20
elif (weight > 6) and (weight <= 10):
    ground_shipping = (4.00 * weight) + 20
elif weight > 10:
    ground_shipping = (4.75 * weight) + 20
else:
    print("Error!")
    
if weight <= 2:
    drone_shipping = 4.50 * weight
elif (weight > 2) and (weight <= 6):
    drone_shipping = 9.00 * weight
elif (weight > 6) and (weight <= 10):
    drone_shipping = 12.00 * weight
elif weight > 10:
    drone_shipping = 14.25 * weight
else:
    print("Error!")

premium_shipping = 125.00

if (ground_shipping < drone_shipping) and (ground_shipping < 125.00):
    shipping_cost = ground_shipping
    method = "Ground"
elif (drone_shipping <= ground_shipping) and (drone_shipping <= premium_shipping):
    shipping_cost = drone_shipping
    method = "Drone"
elif (premium_shipping < ground_shipping) and (premium_shipping < drone_shipping):
    shipping_cost = premium_shipping
    method = "Premium Ground"
else:
    print("Error!")
    
format(ground_shipping, ".2f")
format(drone_shipping, ".2f")
format(premium_shipping, ".2f")
format(shipping_cost, ".2f")

print("{}Ground Shipping costs:{}".format(myColors.b_green, myColors.c_reset), ground_shipping, " for ", weight, " pounds.\n")
print("{}Premium Ground Shipping{}".format(myColors.b_green, myColors.c_reset), "costs a flat fee of 125.00\n")
print("{}Drone Shipping costs: {}".format(myColors.b_green, myColors.c_reset), drone_shipping, " for ", weight, " pounds.\n")
print("\nYour total shipping costs will be: ", "{}".format(myColors.b_blue), shipping_cost, "{}".format(myColors.c_reset), " and will be shipped via ", "{}".format(myColors.bl_green), method, "{}".format(myColors.c_reset), ".\n")
    