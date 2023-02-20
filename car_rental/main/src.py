from .models import Rental, Rating
import random

COMMENTS = {
    1: ["You drive too fast too often.", "You brake too abruptly."],
    2: ["You should slow down a bit", "You accelerate too fast."],
    3: ["You should make your turns more gently", "You need to change your gears more often."],
    4: ["Your driving skills are good but not perfect.", "You need to drive more dynamically."],
    5: ["Your driving skills are excellent!", "You are too good!"]
}

def get_rating(rental : Rental):
    value = random.randint(1, 5)
    comment = COMMENTS[value][random.randint(0, 1)]

    rating = Rating()
    rating.value = value
    rating.comment = comment
    rating.save()

    rental.rating_id = rating

    rental.save()