#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:28:29 2023

@author: psztxa
"""

class DFA : 

    def __init__(self,Q,Sigma,delta,q0,F) :
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function as a dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states 
            
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"
    
    def run (self,w) :
        q = self.q0
        while w!="" :
            q = self.delta[(q,w[0])]
            w = w[1:]
        return q in self.F    
    
    
D1 = DFA({0,1,2,3},{"0","1"},
         {(0,"0"):1,(0,"1"):2,
          (1,"0"):1,(1,"1"):2,
          (2,"0"):3,(2,"1"):1,
          (3,"0"):2,(3,"1"):3},
          0,
          {1})

x=str(input())
if not x or x=="" or x==" ":
    print("it cant be empty")
else:
    print(D1.run(x))



