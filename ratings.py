"""Restaurant rating lister."""


# put your code here

def get_rating(filename):

    ratings_dict = {}

    for line in open(filename):
        list_of_rests = line.rstrip().split(":")

        for restaurant in list_of_rests:
            ratings_dict[restaurant] = ratings_dict.get(restaurant, 0)


        for restaurant in list_of_rests:
            score = list_of_rests[restaurant]

        print "{} is rated at {}".format(restaurant, score)


get_rating("scores.txt")
