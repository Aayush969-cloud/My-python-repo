# Dice rolling game 

import random 


print("Welcome to Game")
print("y for yes /n n for no")

choice = input("can i roll the dice?? /n y/n:  ").lower()
die1 = random.randint(1,6)
die2 = random.randint(1,6)

while True:
 if(choice == "n"):
     print("Thanks for playing")
     break
 elif(choice == "y"):
     print(f"({die1} , {die2})")
 else:
     print("Invalid Input")



# QR code generator

import qrcode

data = input("Enter your URL: ").strip()
filename = ("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size = 10 , border = 4)
qr.add_data(data)

image = qr.make_image(fill_color = "black" , back_color = "white")
image.save(filename)

print("f QR code is saved as {filename}")


