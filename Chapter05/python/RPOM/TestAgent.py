'''
    Example code - not meant to run
'''
from ChatPage import ChatPage
# imports (such as pages import) purposedly omitted

class TestAgent(): 
    def __init__(self):
        self.chat_page = ChatPage()
        self.timeout = 60
        # init routine, including remote login 

    def login(self, user_to):
        return user_to
        #logs in the chat - code omitted

    def test_chat_init(self, user_from, user_to):
        self.login(user_from)
        self.chat_page.wait_for_user_online(user_to, self.timeout) 
        if (not self.chat_page.user_online(user_to)):
            return 1
        self.chat_page.send_chat_to_user(user_to, "Hi from " + user_from)
        self.chat_page.wait_for_chat("Hi from " + user_to, self.timeout)
        if (not self.chat_page.chat_exists("Hi from " + user_to)):
            return 2
        return 0 

    def test_chat_receipt(self, user_from, user_to):
        self.login(user_to)
        self.chat_page.wait_for_chat("Hi from " + user_from, self.timeout)
        if (not self.chat_page.chat_exists("Hi from " + user_from)): 
            return 2 # we associate non existing chat with 2 
        self.chat_page.send_chat_to_user(user_from, "Hi from " + user_to)
        self.chat_page.wait_for_chat("Hi from " + user_from, self.timeout)
        if (not self.chat_page.chat_exists("Hi from " + user_from)):
            return 2
        return 0