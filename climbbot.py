import gradeconvert
from ircutils import bot

class ClimbBot(bot.SimpleBot):

    def on_private_message(self, event):
        self.send_message(event.target, "Just received this private message: " + event.message)

    def on_channel_message(self, event):
        msg = str(event.message)
        if msg.startswith("~") or msg.startswith("!"):
            msg_text = msg[1:]
            self.send_message(event.target, gradeconvert.convert_grade(msg_text))


if __name__ == "__main__":
    # Create an instance of the bot
    # We set the bot's nickname here
    climbbot = ClimbBot("climbbot")

    # Let's connect to the host
    climbbot.connect("irc.snoonet.com", channel="#bottest")

    # Start running the bot
    climbbot.start()
