# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as read_file, open("correct_numbers.csv", "w") as write_file:
        for line in read_file:
            parts = line.strip().split(";")
            week = parts[0].split(" ")[1]
            numbers = parts[1].split(",")
            
            try:
                filtered_numbers = []
                for number in numbers:
                    number = int(number)
                    if 0 < number and number < 40 and number not in filtered_numbers:
                        filtered_numbers.append(number)           

                if len(filtered_numbers) != 7:
                    raise ValueError

                number_output = ""
                for numberr in filtered_numbers:
                    number_output += f"{numberr},"
                number_output = number_output[:-1]
                write_file.write(f"week {int(week)};{number_output}\n")
                
            except:
                pass



if __name__ == "__main__":
    filter_incorrect()
