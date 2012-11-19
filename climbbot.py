import gradeconvert
import re
from ircutils import bot

class ClimbBot(bot.SimpleBot):

    def on_private_message(self, event):
        print "Just received private message from " + event.source + " with message " + event.message
        self.handle_message(event.message, event.source)

    def on_channel_message(self, event):
        msg = str(event.message)
        msg_text = None
        if msg.startswith("~") or msg.startswith("!"):
            msg_text = msg[1:].strip()
        else:
            nickname_match = self.nickname_regex.match(msg)
            if nickname_match:
                msg_text = nickname_match.group(1) 

        if msg_text:
            self.handle_message(msg_text, event.target)

    def handle_message(self, msg_text, reply_target):
        try:
            print "Received: " + msg_text
            if gradeconvert.contains_grade(msg_text):
                self.reply(reply_target, gradeconvert.convert(msg_text))
            else:
                self.reply(reply_target, "I don't understand: " + msg_text)
        except StandardError as e:
            print "Error processing message: " + msg_text, e
            self.reply(reply_target, "I don't understand: " + msg_text)

    def reply(self, reply_target, reply):
        print "Reply: " + reply
        self.send_message(reply_target, reply)

    def __init__(self, nickname):
        super(ClimbBot, self).__init__(nickname)
        self.nickname_regex = re.compile(nickname + '[^0-9a-zA-Z]*(.*)')


if __name__ == "__main__":
    # Create an instance of the bot
    # We set the bot's nickname here
    climbbot = ClimbBot("climbbot")
    climbbot.real_name = "climbbot"

    # Let's connect to the host
    climbbot.connect("irc.snoonet.com", channel="#climbing")

    # Start running the bot
    climbbot.start()
