import panel as pn

pn.config.theme = "dark"

#header of the page

buttonStyles = {
    "height" : "10%",
    "font-family" : "Comic Sans MS"
}
pn.extension(raw_css=['.fade-in { opacity: 0; animation: fadeIn ease-in 1; animation-fill-mode: forwards; animation-duration: 1s;} @keyframes fadeIn { 0% { opacity: 0; } 100% { opacity: 1; } }'])

img = pn.pane.GIF("header.gif" , sizing_mode = "scale_width" , css_classes = ["fade-in"])
img.servable()
registerButton = pn.widgets.Button(name = "Sign in / Sign up" , button_type = "primary" , sizing_mode = "scale_width" , styles = buttonStyles , css_classes = ["fade-in"])
registerButton.servable()

#sections

pn.pane.GIF("shape.gif" , sizing_mode = "scale_width" , css_classes = ["fade-in"]).servable()
pn.pane.GIF("equipments.gif" , sizing_mode = "scale_width" , css_classes = ["fade-in"]).servable()
pn.pane.GIF("arm.gif" , sizing_mode = "scale_width" , css_classes = ["fade-in"]).servable()
pn.pane.GIF("abs.gif" , sizing_mode = "scale_width" , css_classes = ["fade-in"]).servable()
pn.pane.PNG("chest.png" , sizing_mode = "scale_width" , css_classes = ["fade-in"]).servable()
pn.pane.PNG("leg.png" , sizing_mode = "scale_width" , css_classes = ["fade-in"]).servable()

#footer
footerStyles = {
    "font-family" : "Comic Sans MS",
    "font-size" : "large",
    "width" : "50%"
}

footerButton = pn.widgets.Button(name = "Sign in / Sign up" , button_type = "success" , sizing_mode = "scale_width" , styles = buttonStyles , css_classes = ["fade-in"])
pn.Row(pn.widgets.StaticText(value = "Practice makes perfect. Sign up now for free." , styles = footerStyles) , footerButton).servable()
for i in range(10):
    pn.Row("\n").servable()


def register(events):
    pn.serve("register.py")

registerButton.on_click(register)
footerButton.on_click(register)