import unittest
from user import User
from questionnaire import Questionnaire


class Testquestionnaire(unittest.TestCase):
    """This class will test if the questionnaire feature is working correctly."""

    def test_answering_questionnaire(self):
        """Tests if answering questionnaire was succesfull."""
        questionnaire1 = Questionnaire(
            quest_for_questionnaire=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questionnaire1._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ],
        )
        self.assertIn(questionnaire1, questionnaire1.all_questionnaires)

    def test_answering_questionnaire_to_many_answer(self):
        questionnaire1 = Questionnaire(
            quest_for_questionnaire=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        result = questionnaire1._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
                "Soccer",
            ],
        )
        self.assertFalse(result)

    def test_answering_questionnaire_not_enough_answers(self):
        questionnaire1 = Questionnaire(
            quest_for_questionnaire=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        result = questionnaire1._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
            ],
        )
        self.assertFalse(result)

    def test_view_questionnaire(self):
        """Tests viewing a questionnaire."""
        questionnaire = Questionnaire(
            quest_for_questionnaire=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questionnaire._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        expected_result = "1. What is your DJ name?\nAnswer: DJ Anns\n2. What was your last Netflix binge?\nAnswer: Gossip Girl\n3. Would you rather always be two hours early or 20 minutes late?\nAnswer: 20 minutes late\n4. What three items would you bring with you on a deserted island?\nAnswer: Water bottle, fishing pole, campus\n5. What is your go-to karaoke song?\nAnswer: Dancing Queen\n"
        result = questionnaire._view_questionnaire(questionnaire)
        self.maxDiff = None
        self.assertEqual(expected_result, result)

    def test_view_no_questionnaire(self):
        """Tests viewing a questionnaire which is not an instance of the questionnaire class."""
        questionnaire = Questionnaire()
        result = questionnaire._view_questionnaire()
        self.assertFalse(result)

    def test_view_empty_questionnaire(self):
        """Tests viewing a empty questionnaire."""
        questionnaire = Questionnaire()
        result = questionnaire._view_questionnaire(questionnaire)
        self.assertFalse(result)

    def test_send_questionnaire(self):
        """Tests sending a questionnaire."""
        user = User("Anna")
        user_to = User("Halla")
        questionnaire = Questionnaire(
            user,
            [
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questionnaire._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        result = questionnaire._send_questionnaire(user_to, message)
        self.assertTrue(result)

    def test_send_questionnaire_feed(self):
        """Tests when sending a questionnaire if it appears on the user's feed"""
        user = User("Anna")
        user_to = User("Halla")
        questionnaire = Questionnaire(
            user,
            [
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questionnaire._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        questionnaire._send_questionnaire(user_to, message)
        result = f"From:{user.username}\nMessage:{message}\n\n{questionnaire._view_questionnaire(questionnaire)}"
        self.assertIn(result, user.feed)

    def test_send_questionnaire_no_to_user(self):
        """Tests sending a questionnaire with no user to send to."""
        user = User("Anna")
        questionnaire = Questionnaire(
            user,
            [
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questionnaire._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        result = questionnaire._send_questionnaire(message=message)
        self.assertFalse(result)

    def test_send_questionnaire_no_user(self):
        """Tests sending a questionnaire from no user."""
        user_to = User("Hanna")
        questionnaire = Questionnaire(
            quest_for_questionnaire=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questionnaire._answer_questionnaire(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        result = questionnaire._send_questionnaire(user_to, message)
        self.assertFalse(result)

    def test_send_empty_questionnaire(self):
        """Tests sending a empty questionnaire."""
        user = User("Anna")
        user_to = User("Halla")
        questionnaire = Questionnaire(user)
        message = "Hi"
        result = questionnaire._send_questionnaire(user_to, message)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
