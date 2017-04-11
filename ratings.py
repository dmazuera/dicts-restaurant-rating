"""Restaurant rating lister."""


# put your code here

def get_rating(filename):
    """Gets restaurant ratings"""

    ratings_dict = {}

    for line in open(filename):
        list_of_rests = line.rstrip().split(":")

        # creates a dictionary with restaurant [0], and rating [1]
        ratings_dict[list_of_rests[0]] = list_of_rests[1]

    # creates a sorted list of tuples
    new_tuple_list = ratings_dict.items()
    new_sorted_list = sorted(new_tuple_list)

    #prints restaurant, rating in alphabetical order
    for pair in new_sorted_list:
        print "{} is rated at {}".format(pair[0], pair[1])


get_rating("scores.txt")
