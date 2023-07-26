import panel as pn
from panel.theme import Bootstrap
import pandas as pd

pn.config.design = Bootstrap

tabStyle = {
    "width" : "50%",
    "margin-left" : "25%"
}

for i in range(10):
    pn.Column("\n").servable()


logUser = pn.widgets.TextInput(placeholder = "Enter username or Email" , sizing_mode = "scale_width" , required = True)
logPass = pn.widgets.PasswordInput(placeholder = "Enter password" , sizing_mode = "scale_width" , required = True)
logButton = pn.widgets.Button(name = "Log in" , button_type = "primary" , sizing_mode = "scale_width")

regUser = pn.widgets.TextInput(placeholder = "Enter username or Email" , sizing_mode = "scale_width" , required = True)
regPass = pn.widgets.PasswordInput(placeholder = "Enter password" , sizing_mode = "scale_width" , input_type = "password" , required = True)
regButton = pn.widgets.Button(name = "Sign up" , button_type = "success" , sizing_mode = "scale_width")

pn.Tabs(("Log in" , pn.Column(logUser , logPass , logButton)) , ("Sign up" , pn.Column(regUser , regPass , regButton)) , styles = tabStyle).servable()
label = pn.widgets.StaticText(styles = tabStyle)

def register(event):
    file = open("users.txt" , "r+")
    t = 0
    for line in file:
        line = line.strip().split(" ")
        if regUser.value_input == line[0]:
            t += 1
    if t == 0:
        file.write(f"{regUser.value_input} {regPass.value_input}" + "\n")
        label.value = "Done! You can now log in to your account."
        newUser = open(f"{regUser.value_input}.csv" , "a")
        newUser.close()
        userData = {"username" : [regUser.value_input] , 
                    "password" : [regPass.value_input] ,
                    "height" : ["empty"] ,
                    "weight" : ["empty"] ,
                    "BMI" : ["empty"] ,
                    "health condition" : ["empty"] ,
                    "age" : ["empty"] ,
                    "calories" : [0] ,
                    "profile photo" : ["empty"] ,
                    "progression photos" : ["empty"]
                    }
        pd.DataFrame(userData).to_csv(f"{regUser.value_input}.csv")
    else:
        label.value = "Username already taken. Try another username."
          
    file.close()


def login(event):
    file = open("users.txt")
    t = 0
    for line in file:
        line = line.strip().split(" ")
        if logUser.value_input == line[0]:
            t += 1
            if logPass.value_input == line[1]:
                label.value = "You're logged in."
                loginStatus = open("loginStatus.txt" , "w")
                loginStatus.write("1")
                loginStatus.close()
                userfile = open("username.txt" , "w")
                userfile.write(logUser.value_input)
                userfile.close()
                #pn.serve("main.py")
            else:
                label.value = "Wrong password."


    if t == 0:
        label.value = "You don't have an account. Try to sign up first."

    file.close()


regButton.on_click(register)
logButton.on_click(login)
label.servable()