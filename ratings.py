"""Restaurant rating lister."""


# put your code here
def format_restaurant_data(file_name):

    log_file = open(file_name)

    formatted_list_of_file = []

    for line in log_file:
        line = line.rstrip()
        line = line.split(":")
        formatted_list_of_file.append(line)

    return formatted_list_of_file

def create_restaurant_dict(file_name):

    formatted_list_of_file = format_restaurant_data(file_name)

    restaurant_dict = {}

    for line in formatted_list_of_file:
        restaurant_dict[line[0]] = line[1]

    return restaurant_dict

# print(create_restaurant_dict("scores.txt"))

def print_alpha_dict(file_name):

    restaurant_dict = create_restaurant_dict(file_name)

    for restaurant in sorted(restaurant_dict.keys()):
        print(f'{restaurant} is rated at {restaurant_dict[restaurant]}.')

print_alpha_dict('scores.txt')