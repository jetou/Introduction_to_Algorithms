"""
@jetou
@date : 2017/12/15
@algorithms: automaton_matcher
"""

from collections import defaultdict

class match:
    def __init__(self, all_word, train_string, test_string):
        self.all_word = all_word
        self.test_string = test_string
        self.train_string = train_string
        self.delta = defaultdict(dict)
        self.word_len = len(train_string)-1

    def finite_automaton_matcher(self):
        n = len(self.test_string)
        q = 0
        for i in range(0, n):
            try:
                q = self.delta[q][self.test_string[i]]
            except KeyError:
                continue
            if q == self.word_len:
                print "Pattern occurs with shift", i - self.word_len + 1

    def compute_transition_function(self):
        m = len(self.train_string)
        for q in range(0, m+1):
            for i in self.all_word:
                k = min(m + 1, q + 2)
                while True:   # do something while
                    k = k - 1
                    if self.matching_prefix(k, i): #fail condition
                        break
                self.delta[q][i] = k

    def matching_prefix(self,k, a):
        if k == 0:
            return True
        return self.train_string[k-1]==a

    def strat_match(self):
        self.compute_transition_function()
        self.finite_automaton_matcher()



ss = "abcdefghijklmnopqrstuvwxyz" #all test word
input_string = "ababaca"
test_string  = "cababaca"
c = match(ss, input_string, test_string)
c.strat_match()
