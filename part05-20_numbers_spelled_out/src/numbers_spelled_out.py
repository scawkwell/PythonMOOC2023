# Write your solution here
def dict_of_numbers():
    
    first_ten = {0 : 'zero', 
                 1 : 'one', 
                 2 : 'two', 
                 3 : 'three', 
                 4 : 'four', 
                 5 : 'five', 
                 6 : 'six', 
                 7 : 'seven', 
                 8 : 'eight', 
                 9 : 'nine'}

    multiples_ten = {   10 : 'ten',
                        20 : 'twenty',
                        30 : 'thirty',
                        40 : 'forty',
                        50 : 'fifty',
                        60 : 'sixty',
                        70 : 'seventy',
                        80 : 'eighty',
                        90 : 'ninety',}
    
    dictionary_of_numbers = {}

    for number in range(10):
        dictionary_of_numbers[number] = first_ten[number]

    dictionary_of_numbers.update({  10 : 'ten',
                                    11 : 'eleven',
                                    12 : 'twelve',
                                    13 : 'thirteen',
                                    14 : 'fourteen',
                                    15 : 'fifteen',
                                    16 : 'sixteen',
                                    17 : 'seventeen',
                                    18 : 'eighteen',
                                    19 : 'nineteen',
                                    20 : 'twenty' })

    dictionary_of_numbers.update(multiples_ten)


    for number in range(20, 100):
        if number > 20 and number % 10 != 0:
            tens = (number // 10) * 10
            units = number - tens
            dictionary_of_numbers[number] = multiples_ten[tens] + "-" + first_ten[units]

    return dictionary_of_numbers
