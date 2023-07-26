import panel as pn
from panel.theme import Material
import pandas as pd
import os

pn.config.theme = "dark"
pn.config.design = Material

def app():

    #training tab
    arm = pn.pane.JPG("arm.jpg" , sizing_mode = "scale_width")
    abs = pn.pane.JPG("abs.jpg" , sizing_mode = "scale_width")
    chest = pn.pane.JPG("chest.jpg" , sizing_mode = "scale_width")
    legs = pn.pane.JPG("legs.jpg" , sizing_mode = "scale_width")
    shoulder = pn.pane.JPG("back.jpg" , sizing_mode = "scale_width")
    armButton = pn.widgets.Button(name = "Arm Workout" , sizing_mode = "scale_width")
    absButton = pn.widgets.Button(name = "Abs Workout" , sizing_mode = "scale_width")
    chestButton = pn.widgets.Button(name = "Chest Workout" , sizing_mode = "scale_width")
    legsButton = pn.widgets.Button(name = "Lower Body Workout" , sizing_mode = "scale_width")
    shoulderButton = pn.widgets.Button(name = "Back & Shoulder Workout" , sizing_mode = "scale_width")
    
    userfile = open("username.txt")
    for i in userfile:
        pass

    df = pd.read_csv(f"{i}.csv")

    #report tab
    if df["height"][0] == "empty" and df["weight"][0] == "empty" and df["BMI"][0] == "empty":
        height = pn.widgets.TextInput(placeholder = "Enter your height(m)" , sizing_mode = "scale_width")
        weight = pn.widgets.TextInput(placeholder = "Enter your weight(kg)" , sizing_mode = "scale_width")
        BMIvalue = pn.widgets.StaticText(sizing_mode = "scale_width")
        healthCondition = pn.widgets.StaticText(sizing_mode = "scale_width")
    else: 
        height = pn.widgets.TextInput(value = f"{df['height'][0]}" , placeholder = "Enter your height(m)" , sizing_mode = "scale_width")
        weight = pn.widgets.TextInput(value = f"{df['weight'][0]}" , placeholder = "Enter your weight(kg)" , sizing_mode = "scale_width")
        BMIvalue = pn.widgets.StaticText(value = f"{df['BMI'][0]}" , sizing_mode = "scale_width")
        healthCondition = pn.widgets.StaticText(value = f"{df['health condition'][0]}" , sizing_mode = "scale_width")
    
    BMI = pn.widgets.StaticText(value = "Your BMI is : " , sizing_mode = "scale_width")
    BMIbutton = pn.widgets.Button(name = "Calculate BMI" , sizing_mode = "scale_width")
    
    #chat & profile tab
    if df["profile photo"][0] == "empty":
        userPhoto = pn.pane.PNG("profile.png" , sizing_mode = "scale_width")
        chatBox = pn.widgets.ChatBox(message_icons = {"You" :"profile.png"})
    else:
        userPhoto = pn.pane.PNG(f"{df['profile photo'][0]}" , sizing_mode = "scale_width")
        chatBox = pn.widgets.ChatBox(message_icons = {"You" : f"{i}.png"})

    userPhotoUpload = pn.widgets.FileInput(accept = ".png , .jpg , .jpeg" , sizing_mode = "scale_width")
    passChange = pn.widgets.TextInput(placeholder = "Enter your new password" , sizing_mode = "scale_width")
    update = pn.widgets.Button(name = "Update profile" , sizing_mode = "scale_width")
    delete = pn.widgets.Button(name = "Remove photo" , sizing_mode = "scale_width")
    updateResult = pn.widgets.StaticText()
    logoutButton = pn.widgets.Button(name = "Log out" , sizing_mode = "scale_width")
    deleteAccountbutton = pn.widgets.Button(name = "Delete your account" , sizing_mode = "scale_width" , button_type = "danger")

    pn.Tabs(("Training" , pn.Column(arm , armButton , abs , absButton , chest , chestButton , legs , legsButton , shoulder , shoulderButton)) ,
            ("Chat" , chatBox) , ("Report" , pn.Column(height , weight , BMIbutton , pn.Row(BMI , BMIvalue) , healthCondition)) ,
            ("Profile" , pn.Column(pn.widgets.StaticText(value = f"Username: {i}") , "Choose your profile photo" , userPhoto , userPhotoUpload ,
                            pn.widgets.StaticText(value = "Change your password: ") , passChange , pn.Row(update , delete) , updateResult , logoutButton , deleteAccountbutton))).servable()
    
    def updateProfile(event):
        if userPhotoUpload.value is not None:
            userPhotoUpload.save(f"{i}.png")
            df["profile photo"][0] = f"{i}.png"
            df.to_csv(f"{i}.csv")
            updateResult.value = "Profile updated successfully. Refresh the page to see the changes."
        
        if passChange.value_input is not None:
            df["password"][0] = passChange.value_input
            df.to_csv(f"{i}.csv")
            with open("users.txt" , "r") as file:
                inputFilelines = file.readlines()
                with open("users.txt" , "w") as file:
                    for line in inputFilelines:
                        if line.strip().split(" ")[0] != i:
                            file.write(line)
            
            file.close()
            file = open("users.txt" , "a+")
            file.write(f"{i} {passChange.value_input}")
            file.close()
            updateResult.value = "Profile updated successfully. Refresh the page to see the changes."
        
        else:
            updateResult.value = "There are no changes to update."
            

    def removePhoto(event):
        df["profile photo"][0] = "empty"
        os.remove(f"{i}.png")
        df.to_csv(f"{i}.csv")
        updateResult.value = "Profile photo was removed. Refresh the page to see the changes."
    
    def logout(event):
        loginStatus = open("loginStatus.txt" , "w")
        loginStatus.write("0")

    def deleteAccount(event):
        if df["profile photo"][0] != "empty":
            os.remove(f"{i}.png")
        os.remove(f"{i}.csv")
        loginStatus = open("loginStatus.txt" , "w")
        loginStatus.write("0")
        with open("users.txt" , "r") as file:
            inputFilelines = file.readlines()
            with open("users.txt" , "w") as file:
                for line in inputFilelines:
                    if line.strip().split(" ")[0] != i:
                        file.write(line)
            
        file.close()

    def BMIcalculator(event):
        df["BMI"][0] = float(weight.value_input )/ (float(height.value_input)**2)
        df["height"][0] = height.value_input
        df["weight"][0] = weight.value_input
        BMIvalue.value = f"{df['BMI'][0]}"
        if float(df["BMI"][0]) < 18.5:
            df["health condition"][0] = "You're underweight"
        elif float(df["BMI"][0]) >= 18.5 and float(df["BMI"][0])<= 24.9:
            df["health condition"][0] = "Your BMI falls within the healthy weight range"
        elif float(df["BMI"][0]) > 24.9 and float(df["BMI"][0])<= 29.9:
            df["health condition"][0] = "You're overweight"
        elif float(df["BMI"][0]) > 29.9:
            df["health condition"][0] = "Your BMI falls within the obese range"
        healthCondition.value = df["health condition"][0]
        df.to_csv(f"{i}.csv")

    def armFunc(event):
        pn.serve("arm.py")

    update.on_click(updateProfile)
    delete.on_click(removePhoto)
    logoutButton.on_click(logout)
    deleteAccountbutton.on_click(deleteAccount)
    BMIbutton.on_click(BMIcalculator)
    armButton.on_click(armFunc)


loginStatus = open("loginStatus.txt")
for i in loginStatus:
    pass

if i == "0":
    pn.Column("You don't have access to this page. You should login first").servable()

else:
    app()
