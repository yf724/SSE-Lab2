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
            "Which of the following numbers is the largest: 29, 41,22") == 41


def test_add_up_numbers():
    assert process_query(
            "What is 55 plus 90") == 145
