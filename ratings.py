"""Restaurant rating lister."""


# put your code here

def get_rating(filename):

    ratings_dict = {}

    for line in open(filename):
        list_of_rests = line.rstrip().split(":")

        # creating a dictionary with restaurnt [0], and rating [1]
        ratings_dict[list_of_rests[0]] = list_of_rests[1]

        #print "{} is rated at {}".format(list_of_rests[0], list_of_rests[1])

        new_tuple_list = ratings_dict.items()
        new_sorted_list = sorted(new_tuple_list)

    for pair in new_sorted_list:
        print "{} is rated at {}".format(pair[0], pair[1])

    return ratings_dict


ratings = get_rating("scores.txt")
