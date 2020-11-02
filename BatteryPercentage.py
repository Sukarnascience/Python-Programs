#https://www.facebook.com/sukarna.jana.9/posts/861280437944655
#Subscribed by Sukarna Jana

import psutil

#Use Only in Laptop for seeing Battery % 
battery=psutil.sensors_battery()
percent=str(battery.percent)

print("Your Battery Status:-",percent,"%")
