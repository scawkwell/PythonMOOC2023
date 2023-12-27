# Write your solution here
def is_it_valid(pic : str):
    from datetime import datetime
    control_characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    cent_marker = pic[6]
    personal_identifier = pic[7:10]
    control = pic[-1]
    

    # Check the century marker is valid
    if cent_marker != "-" and cent_marker != "+" and cent_marker != "A":
        print("cent")
        return False

    try:
        if cent_marker == "-":
            year += 1800
        elif cent_marker == "+":
            year



    # Check DOB is valid
    try:
        dob = datetime(year, month, day)
        print("dob")
    except:
        print("dob bad")
        return False



    
    # Check the control character is valid
    control_input = int(pic[:6] + pic[7:10])
    print("contr")
    return control_characters[control_input % 31] == control

if __name__ == "__main__":


    print(is_it_valid("290200A1239"))