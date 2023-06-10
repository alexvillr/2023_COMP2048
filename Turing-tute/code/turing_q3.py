# -*- coding: utf-8 -*-
"""
Test script for running a turing machine to accept a string of '0's of
length 2 ^ n | n >= 0

Created on Mon 20 Mar 14:27:32 2023

@author: alexvillr
"""
from turing_machine import TuringMachine

# Create the turing machine
q3Machine = TuringMachine(
    {
        ("q0", "0"): ("q1", "_", "R"),
        ("q0", "_"): ("qr", "_", "R"),
        ("q0", "X"): ("qr", "X", "R"),
        ("q1", "0"): ("q2", "X", "R"),
        ("q1", "_"): ("qa", "_", "R"),
        ("q1", "X"): ("q1", "X", "R"),
        ("q2", "0"): ("q3", "0", "R"),
        ("q2", "_"): ("q4", "_", "L"),
        ("q2", "X"): ("q2", "X", "R"),
        ("q3", "0"): ("q2", "X", "R"),
        ("q3", "_"): ("qr", "_", "R"),
        ("q3", "X"): ("q3", "X", "R"),
        ("q4", "0"): ("q4", "0", "L"),
        ("q4", "_"): ("q1", "_", "R"),
        ("q4", "X"): ("q4", "X", "L"),
    },
    blank_symbol="_",
    wait_mode=False,
)

statement = input("Please enter the number of 0s to see if machine accepts: ")
asZeros = int(statement) * "0"

q3Machine.debug(asZeros, step_limit=2000, colored=True)
