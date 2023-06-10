# -*- coding: utf-8 -*-
"""
Test script for running a turing machine to accept the language A where
    A = {w#w | w in {0, 1}*}

Created on Wed 22 Mar 16:01:11 2023

@author alexvillr
"""

from turing_machine import TuringMachine

# Create the turing machine
q2_machine = TuringMachine(
    {
        ("q1", "0"): ("q2", "X", "R"),
        ("q1", "1"): ("q3", "X", "R"),
        ("q1", "#"): ("q8", "#", "R"),
        ("q2", "0"): ("q2", "0", "R"),
        ("q2", "1"): ("q2", "1", "R"),
        ("q2", "#"): ("q4", "#", "R"),
        ("q3", "0"): ("q3", "0", "R"),
        ("q3", "1"): ("q3", "1", "R"),
        ("q3", "#"): ("q5", "#", "R"),
        ("q4", "0"): ("q6", "X", "L"),
        ("q4", "X"): ("q4", "X", "R"),
        ("q5", "1"): ("q6", "X", "L"),
        ("q5", "X"): ("q5", "X", "R"),
        ("q6", "0"): ("q6", "0", "L"),
        ("q6", "1"): ("q6", "1", "L"),
        ("q6", "#"): ("q7", "#", "L"),
        ("q6", "X"): ("q6", "X", "L"),
        ("q7", "0"): ("q7", "0", "L"),
        ("q7", "1"): ("q7", "1", "L"),
        ("q7", "X"): ("q1", "X", "R"),
        ("q8", "0"): ("qa", "0", "R"),
        ("q8", "1"): ("qa", "1", "R"),
        ("q8", "#"): ("qa", "#", "R"),
        ("q8", "_"): ("qa", "_", "R"),
        ("q8", "X"): ("q8", "X", "R"),
    },
    blank_symbol="_",
    start_state="q1",
    wait_mode=False,
)

statement = input(
    "Please enter input to see if it fits the language "
    "A = {w#w | w in {0, 1}*}: \n"
)

q2_machine.debug(statement, step_limit=2000, colored=True)
