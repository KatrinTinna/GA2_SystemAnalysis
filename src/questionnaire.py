#!/bin/python3.11
import random
from user import *


class Questionnaire:
    all_questionnaires = []
    all_questions = [
        "What is your DJ name?",
        "If your life was captured in the “expectation vs. reality” meme, what would the two pictures be?",
        "Which two companies would you like to be sponsored by?",
        "What was your last Netflix binge?",
        "If you could be a character in any movie, what character and what movie would it be?",
        "If you invented an ice cream flavor, what ingredients would it have, and what would it be called?",
        "If you could make an office rule that everyone had to follow for a day, what would it be?",
        "What is the best concert/ festival you have ever been to?",
        "A genie grants you one wish; what do you wish for?",
        "What three items would you bring with you on a deserted island?",
        "Would you rather always be two hours early or 20 minutes late?",
        "Would you rather have every traffic light turn green or always have the best parking spot?",
        "What is the most underrated city you have ever visited?",
        "If you could live in a different country for a year, which country would you choose?",
        "What is your go-to karaoke song?",
    ]

    def __init__(
        self, user: User = None, quest_for_questionnaire=random.sample(all_questions, 5)
    ) -> None:
        self.questionnaire = {}
        self.user = user
        self.quest_for_questionnaire = quest_for_questionnaire

    def _answer_questionnaire(self, answers=[]):
        """Adds a questionnaire with answers to list of all questionnaires.

        Args:
            answers (list): A list consisting of all the answers to the questionnaire. Defaults to an empty list.

        Returns:
            bool: Returns True if the questionnaire was successfully added, else returns False.
        """
        if len(answers) < len(self.quest_for_questionnaire) and len(answers) != 0:
            print("Please answer all the questions provided")
            return False
        elif len(answers) > len(self.quest_for_questionnaire):
            print("Questions answered were too many")
            return False

        for index, quest in enumerate(self.quest_for_questionnaire):
            if len(answers) == len(self.quest_for_questionnaire):
                answer = answers[index]
            else:
                valid_answer = False
                while not valid_answer:
                    answer = input(f"{index + 1}. {quest} \n")
                    if answer == "":
                        print("Please answer the question or enter q to quit")
                    elif answer == "q":
                        return False
                    else:
                        valid_answer = True
            self.questionnaire[quest] = answer
        Questionnaire.all_questionnaires.append(self)
        print("The questionnaire has been successfully answered")
        return True

    def _view_questionnaire(self, other: "Questionnaire" = None):
        """Makes a list with questionnaire and answers to print.

        Args:
            other (Questionnaire): Instance of Questionnaire representing the questionnaire to view. Defaults to None

        Returns:
            str or bool: Returns str of questionnaire and answers to print if the questionnaire was successfully viewed, else returns False.
        """
        questionnaire_str = ""
        if other is None or other.questionnaire == {}:
            print("There is no questionnaire to view")
            return False
        for index, (quest, answer) in enumerate(other.questionnaire.items()):
            questionnaire_str += f"{index + 1}. {quest}\nAnswer: {answer}\n"
        return questionnaire_str

    def _send_questionnaire(self, user_to: User = None, message=""):
        """Sends questionnaire to other user.

        Args:
            user_to (User): Instance of User representing the user to send to. Defaults to None
            message (str): A string representing the message to include with the questionnaire

        Returns:
            bool: Returns True if the questionnaire was successfully sent, else returns False.
        """
        if self.questionnaire == {}:
            print("There is no questionnaire to send")
            return False
        if not isinstance(self.user, User) or not isinstance(user_to, User):
            print("The users for this questionnaire are not valid please try again")
            return False
        if message == "":
            message = input("Please enter the message for this questionnaire\n")
        user_to.feed.append(
            f"From:{self.user.username}\nMessage:{message}\n\n{self._view_questionnaire(self)}"
        )
        print(f"The questionnaire has been successfully sent to {user_to.username}")
        return True
