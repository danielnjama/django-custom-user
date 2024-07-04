import random
def get_activation_code():
    number_range = list(range(100000,999999))
    code = random.sample(number_range,1)[0]
    return code