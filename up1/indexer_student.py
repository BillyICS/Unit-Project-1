# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 11:38:58 2014

@author: zzhang
"""
import pickle
import re

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0
        
    def get_total_words(self):
        return self.total_words
        
    def get_msg_size(self):
        return self.total_msgs
        
    def get_msg(self, n):
        return self.msgs[n]
        
    # implement
    def add_msg(self, m):
        self.total_msgs += 1
        self.msgs.append(m)
        return
        
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        words = m.split()
        for s in words:
            if s not in self.index.keys():
                self.index[s] = list()
            self.index[s].append(l)
        return

    # implement: query interface
    '''
    return a list of tupple. if index the first sonnet (p1.txt), then
    call this function with term 'thy' will return the following:
    [(7, " Feed'st thy light's flame with self-substantial fuel,"),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (12, ' Within thine own bud buriest thy content,')]          
    '''                      
    def search(self, term):
        msgs = []
        words = term.strip().split()
        if len(words) == 1:
            try:
                for idx in self.index[words[0]]:
                    msgs.append((idx, self.msgs[idx]))
            except KeyError:
                return []
            return msgs
        else:
            for word in words:
                try:
                    for idx in self.index[word]:
                        msgs.append((idx, self.msgs[idx]))
                except KeyError:
                    return []
            clean_msgs = list()
            for m in msgs:
                if msgs.count(m) == len(words):
                    clean_msgs.append(m)
            final_messages = list()
            for m in clean_msgs:
                if term.strip() in m[1]:
                    final_messages.append(m)
            return final_messages

class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()

    def indexing(self, m, l):
        words = m.split()
        if len(words) == 1 and words[0] != '':
            self.index[words[0]] = list()
            self.index[words[0]].append(l)
        else:
            for s in words:
                temp_s = re.sub(r'\W', '', s)
                if temp_s not in self.index.keys():
                    self.index[temp_s] = list()
                if l not in self.index[temp_s]:
                    self.index[temp_s].append(l)
        
        # implement: 1) open the file for read, then call
        # the base class's add_msg_and_index
    def load_poems(self):
        sonnets_file = open("AllSonnets.txt", 'r')
        sonnets_content = sonnets_file.read()
        sonnets_file.close()
        sonnets_list = sonnets_content.split('\n')
        for s in sonnets_list:
            if s != 'All Sonnets' and s != '':
                self.add_msg_and_index(s)
        return
    
        # implement: p is an integer, get_poem(1) returns a list,
        # each item is one line of the 1st sonnet
    def get_poem(self, p):
        poem = []
        roman_chapter = self.int2roman[p] + '.'
        chapter_index = self.index[roman_chapter][0]
        poem.append(self.msgs[chapter_index])
        chapter_index += 1
        while True:
            if self.msgs[chapter_index].strip('.') in self.int2roman.values():
                break
            else:
                poem.append(self.msgs[chapter_index])
                chapter_index += 1
        return poem

if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    # the next two lines are just for testing
    p = sonnets.get_poem(3)
    #print(p)
    s = sonnets.search("can see")
    print(s)