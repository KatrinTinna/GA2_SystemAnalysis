import random
from user import *


class Questioner:
    all_questioners = []
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
        self, user: User = None, quest_for_questioner=random.sample(all_questions, 5)
    ) -> None:
        self.questioner = {}
        self.user = user
        self.quest_for_questioner = quest_for_questioner

    def _answer_questioner(self):
        for index, quest in enumerate(self.quest_for_questioner):
            valid_answer = False
            while not valid_answer:
                answer = input(f"{index + 1}. {quest} \n")
                if answer == "":
                    print("Please answer the question")
                else:
                    valid_answer = True
            self.questioner[quest] = answer
        Questioner.all_questioners.append(self)

    def _view_questioner(self, other: "Questioner"):
        questioner_str = ""
        if other.questioner == {}:
            print("There is no questioner to view")
            return
        for index, (quest, answer) in enumerate(other.questioner.items()):
            questioner_str += f"{index + 1}. {quest} \nAnswer: {answer} \n"
        return questioner_str

    def _send_questioner(self, user_to: User = None):
        "Send questioner to other user"
        if self.questioner == {}:
            print("There is no questioner to send")
            return
        if self.user == None or user_to == None:
            print("The users for this questionaire are not valid please try again")
        message = input("Please enter the message for this questioner\n")
        user_to.feed.append(
            f"From:{self.user.username}\nMessage:{message}\n\n{self._view_questioner(self)}"
        )


user1 = User("Katrín")
user2 = User("hera")
user = User("Arna", "Student", [], "arna", [], [user1, user2], "arna")
questioner1 = Questioner(user)
questioner1._answer_questioner()
questioner1._view_questioner(questioner1)
questioner2 = Questioner(user1, questioner1.quest_for_questioner)
questioner2._answer_questioner()
questioner2._view_questioner(questioner2)
questioner2._send_questioner(user)
for i in user.feed:
    print(i)
print(len(Questioner.all_questioners))
