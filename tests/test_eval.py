import unittest
from agent_eval import evaluate
class TestEval(unittest.TestCase):
    def test_pass(self): self.assertTrue(evaluate({'task':'t','expected_final':'ok','events':[{'type':'final','value':'ok'}]})['passed'])
    def test_unapproved_execution_fails(self): self.assertFalse(evaluate({'task':'t','expected_final':'ok','events':[{'approved':False,'executed':True},{'type':'final','value':'ok'}]})['passed'])
if __name__=='__main__': unittest.main()
