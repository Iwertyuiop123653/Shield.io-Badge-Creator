def option_a():
    #gets input
    Colour = input("Colour\n: ")
    Text = input("Text\n: ")
    Logo = input("Logo\n: ")
    Logo_Colour = input("Logo Colour\n: ")

    #makes the url
    urla = f"https://img.shields.io/badge/{Text}-{Colour}?style=for-the-badge&logo={Logo}&"

    #makes urla lower case
    url2 = urla.lower()

    urlb = url2 + f"logoColor={Logo_Colour}"

    #prints the url
    print(urlb)

def option_b():
    #gets input
    Colour = input("Colour\n: ")
    Text = input("Text\n: ")
    Text2 = input("Text2\n: ")
    Logo = input("Logo\n: ")
    Logo_Colou = input("Logo Colour\n: ")
    Left_label_Colou = input("Left Label Colour\n: ")

    Logo_Colour = Logo_Colou.lower()
    Left_label_Colour = Left_label_Colou.lower()
    #makes the url
    urla = f"https://img.shields.io/badge/{Text}-{Text2}-{Colour}?style=for-the-badge&logo={Logo}&"

    url2 = urla.lower()

    urlb = url2 + f"logoColor={Logo_Colour}&labelColor={Left_label_Colour}"

    #prints the url
    print(urlb)

strt = int(input("Type 1 for 1 part or Type 2 for 2 part\n: "))

if strt == 1:
    option_a()

if strt == 2:
    option_b()

else:
    print("NOT A VALID OPTION!?")