from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == (
            "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_your_name_returns_yiran_and_wenqing():
    assert process_query("What is your name") == "yfwt"


def test_largest_number():
    assert process_query(
            "Which of the following numbers is the largest: 29, 41,22") == "41"


def test_add_up_numbers():
    assert process_query(
            "What is 55 plus 90") == "145"


def test_multiply_numbers():
    assert process_query(
            "What is 31 multiplied by 21") == "651"


def test_square_and_cube_numbers():
    assert process_query(
            """Which of the following numbers is both
            a square and a cube: 64, 8, 2, 3, 4, 5, 6""") == ["64"]


def test_prime_number():
    assert process_query(
           """ Which of the following numbers are primes:
           92, 6, 85, 23, 42?""") == "23"

def test_prime_number():
    assert process_query(
            """Which of the following numbers are primes:
              37, 8, 73, 47, 25?""") == ["37", "73", "47"]
    

def test_minus_numbers():
    assert process_query(
            """What is 66 minus 97?""") == "-31"


def test_minus_numbers2():
    assert process_query(
            """What is 81 minus 86?""") == "-5"


def test_power_numbers():
    assert process_query(
            """What is 5 to the power of 8?""") == "390625"
