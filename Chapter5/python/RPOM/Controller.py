'''
    Example code - not meant to run
'''
# other imports omitted 
import unittest 
import subprocess

class Controller(unittest.TestCase):
    def test_chat(self):
        agent1 = {}
        agent1.user = # ... 
        agent1.host = # ... 
        agent2 = {}
        agent2.user = # ... 
        agent2.host = # ... 
        self.run_command("login()", agent1.user, agent1.host)  
        # could add check no error here,  
        # see next example to understand this method 
        self.run_command("login()", agent2.user, agent2.host) 
        self.chat_init_response= self.run_command("test_chat_init(\"user1\",\"user2\")", agent1.user, agent1.host) 
        self.assertEquals(self.chat_init_response, 0) #handle the other errors so they are clear on the failure 
        self.chat_receipt_response = self.run_command("test_chat_receipt((\"user1\",\"user2\")", agent2.user, agent2.host) 
        self.assertEquals(self.chat_receipt_response,0) 

    def run_command(self, method, user, host):
        command = "ssh " + user + "@" + host+ "\"path/to/myenv/bin/python\" -c 'from testAgent import *; "+method+"'" 
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE) 
        return result.communicate()
    
    def chat_receipt_response(self):
        return
    # code ommitted