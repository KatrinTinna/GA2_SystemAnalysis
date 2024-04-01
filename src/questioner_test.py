import unittest
from user import User
from questioner import Questioner
import coverage


class TestQuestioner(unittest.TestCase):
    """This class will test if the Questioner feature is working correctly."""

    def test_answering_questioner(self):
        """Tests if answering questioner was succesfull."""
        questioner1 = Questioner(
            quest_for_questioner=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questioner1._answer_questioner(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ],
        )
        self.assertIn(questioner1, Questioner.all_questioners)

    def test_view_questioner(self):
        """Tests viewing a questioner."""
        questioner = Questioner(
            quest_for_questioner=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questioner._answer_questioner(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        expected_result = "1. What is your DJ name?\nAnswer: DJ Anns\n2. What was your last Netflix binge?\nAnswer: Gossip Girl\n3. Would you rather always be two hours early or 20 minutes late?\nAnswer: 20 minutes late\n4. What three items would you bring with you on a deserted island?\nAnswer: Water bottle, fishing pole, campus\n5. What is your go-to karaoke song?\nAnswer: Dancing Queen\n"
        result = questioner._view_questioner(questioner)
        self.maxDiff = None
        self.assertEqual(expected_result, result)

    def test_view_no_questioner(self):
        """Tests viewing a questioner which is not an instance of the Questioner class."""
        questioner = Questioner()
        result = questioner._view_questioner()
        self.assertFalse(result)

    def test_view_empty_questioner(self):
        """Tests viewing a empty questioner."""
        questioner = Questioner()
        result = questioner._view_questioner(questioner)
        self.assertFalse(result)

    def test_send_questioner(self):
        """Tests sending a questioner."""
        user = User("Anna")
        user_to = User("Halla")
        questioner = Questioner(
            user,
            [
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questioner._answer_questioner(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        result = questioner._send_questioner(user_to, message)
        self.assertTrue(result)

    def test_send_questioner_feed(self):
        """Tests when sending a questioner if it appears on the user's feed"""
        user = User("Anna")
        user_to = User("Halla")
        questioner = Questioner(
            user,
            [
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questioner._answer_questioner(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        questioner._send_questioner(user_to, message)
        result = f"From:{user.username}\nMessage:{message}\n\n{questioner._view_questioner(questioner)}"
        self.assertIn(result, user.feed)

    def test_send_questioner_no_to_user(self):
        """Tests sending a questioner with no user to send to."""
        user = User("Anna")
        questioner = Questioner(
            user,
            [
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questioner._answer_questioner(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        result = questioner._send_questioner(None, message)
        self.assertFalse(result)

    def test_send_questioner_no_user(self):
        """Tests sending a questioner from no user."""
        user_to = User("Hanna")
        questioner = Questioner(
            quest_for_questioner=[
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questioner._answer_questioner(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        result = questioner._send_questioner(user_to, message)
        self.assertFalse(result)

    def test_send_empty_questioner(self):
        """Tests sending a empty questioner."""
        user = User("Anna")
        user_to = User("Halla")
        questioner = Questioner(user)
        message = "Hi"
        result = questioner._send_questioner(user_to, message)
        self.assertFalse(result)

    def test_send_questioner_unsuccessful(self):
        """Tests if when sending a questioner was unsuccessful if it still appears on the users feed"""
        user = User("Anna")
        user_to = User("Halla")
        questioner = Questioner(
            user,
            [
                "What is your DJ name?",
                "What was your last Netflix binge?",
                "Would you rather always be two hours early or 20 minutes late?",
                "What three items would you bring with you on a deserted island?",
                "What is your go-to karaoke song?",
            ],
        )
        questioner._answer_questioner(
            [
                "DJ Anns",
                "Gossip Girl",
                "20 minutes late",
                "Water bottle, fishing pole, campus",
                "Dancing Queen",
            ]
        )
        message = "Hi"
        questioner._send_questioner(message=message)
        result = f"From:{user.username}\nMessage:{message}\n\n{questioner._view_questioner(questioner)}"
        print(f"user feed: {user_to.feed}")
        print(result in user_to.feed)
        result1 = "Fokk off"
        self.assertNotIn(result, user_to.feed)


if __name__ == "__main__":
    test = TestQuestioner()
    test.test_send_questioner_unsuccessful()
    cov = coverage.Coverage()
    cov.start()

    unittest.main()

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")
