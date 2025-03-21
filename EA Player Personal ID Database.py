def main():
    # Dictionary mapping user inputs to their respective responses
    responses1 = {
        "NQZ21": "1008326962781",
        "GT800M": "1007371140128",
        "ID_M_IDK_4": "1007626131024",
        "min_mozj_ez": "1004225464721",
        "Qiu_Bai_SKDF": "1004699201316",
        "DSkD-PopCap-GT3": "1006138250717",
        "July8280v0": "1005238363609",
        "ID_H_LIGHTHOUSE": "1003798306823",
        "jidcues": "1006617763064",
        "CREENSON": "1005788522509",
        "xuanyu_hello": "1003953342633",
        "ID_M_GOAT": "1004675093888",
        "MinecraftLionxX": "1935839972",
        "Z-Phragmites": "1814002591",
        "shoushou1106": "1004656909349",
        "Fei_bo_qwq": "1006010053619",
        "138BBQ": "1010231687099",
        "jlklzn": "1003914877790",
        "COTears": "1005463164735",
        "Chomper_chichi": "1010323670470",
        "Kemou_OWO": "1005938123313",
        "partycloud": "1005789032825",
        "_Nemsch___U": "1005938273904",
        "Im_Sam_SAMA": "1898196972",
        "Prof_Edgar": "1006416304844",
        "CHN-Snowy": "1005671158262",
        "Pepper_MD_Rumia": "1006311927925",
        "PingsQAQ": "1006719667001",
        "ExoticArrowww2": "1004037833985",
        "jigglyjoe15": "1004037833985",
        "shoushou1107": "1007264158402",
        "EyjaAlcremieCake": "1006692340632"
    }

    responses2 = {
    "NQZ21": "ID number: 210106201002240336 Name: Zhou Yuze",
    "MinecraftLionxX": "Real name: Liu Ruoyu Mobile phone number: 13836053660 Company name: Harbin World Department Store Shufang Knitting Children's Wear Boutique"
    }

    while True:
        # Prompt the user for input
        user_input = input("Please enter player ID (type 'exit' to quit): ")

        # Exit condition
        if user_input.lower() == 'exit':
            print("Program exited.")
            break

        # Check if input exists in responses1 dictionary
        if user_input in responses1:
            print(f"Personal ID: {responses1[user_input]}")

        # Check if input exists in responses2 dictionary
        if user_input in responses2:
            print(f"More information: {responses2[user_input]}")

        # Special case for specific users
        elif user_input == "shoushou1106" or user_input == "shoushou1107":
            print("He is a pedophile supporter https://youtu.be/DKL4-pM9mNM")

        # If the player is not found
        else:
            print(f"The player does not exist: {user_input}")

if __name__ == "__main__":
    main()
