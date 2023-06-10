# -*- coding: utf-8 -*-
"""
Test script for running a turing machine to accept the language C where
    C = {a^i b^j c^k | i * j = k && i, j, k >= 1}

Created on Mon 20 Mar 29:59:32 2023

@author: alexvillr
"""
from turing_machine import TuringMachine

# Create the turing machine
q4_machine = TuringMachine(
    {
        ("q0", "a"): ("q1", "x", "R"),
        ("q1", "a"): ("q1", "a", "R"),
        ("q1", "b"): ("q2", "y", "R"),
        ("q1", "z"): ("q4", "z", "L"),
        ("q2", "b"): ("q2", "b", "R"),
        ("q2", "c"): ("q3", "z", "L"),
        ("q2", "z"): ("q2", "z", "R"),
        ("q3", "b"): ("q3", "b", "L"),
        ("q3", "y"): ("q1", "y", "R"),
        ("q3", "z"): ("q3", "z", "L"),
        ("q4", "a"): ("q5", "a", "L"),
        ("q4", "x"): ("q6", "x", "R"),
        ("q4", "y"): ("q4", "b", "L"),
        ("q5", "a"): ("q5", "a", "L"),
        ("q5", "x"): ("q0", "x", "R"),
        ("q6", "b"): ("q6", "b", "R"),
        ("q6", "z"): ("q6", "z", "R"),
        ("q6", "_"): ("qa", "_", "L"),
    },
    blank_symbol="_",
    wait_mode=False,
)

statement = input(
    "Please enter your string to see if it is accepted by "
    "language C = {a^i b^j c^k | i * j = k && i, j, k >= 1}: "
)

q4_machine.debug(statement, step_limit=2000, colored=True)
