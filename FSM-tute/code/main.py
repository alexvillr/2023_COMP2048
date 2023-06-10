import FSM

# Q2 FSM
q2_transition_table = {
        (1, '0'): 1,
        (1, '1'): 2,
        (2, '0'): 3,
        (2, '1'): 2,
        (3, '0'): 2,
        (3, '1'): 2
    }
q2_fsm = FSM.FSM(transition_table=q2_transition_table, accepting_states={2})

# Q3 FSM
q3_transition_table = {
        (1, '0'): 4,
        (1, '1'): 2,
        (2, '0'): 3,
        (2, '1'): 2,
        (3, '0'): 3,
        (3, '1'): 2,
        (4, '0'): 4,
        (4, '1'): 5,
        (5, '0'): 4,
        (5, '1'): 5
    }
q3_fsm = FSM.FSM(transition_table=q3_transition_table, accepting_states={2,4})

# Q4 FSMs
q4a_transition_table = {
        (1, '0'): 2,
        (1, '1'): 1,
        (2, '0'): 1,
        (2, '1'): 2
        }
q4a_fsm = FSM.FSM(transition_table=q4a_transition_table, accepting_states={1})

q4b_transition_table = {
        (1, '0'): 1,
        (1, '1'): 2,
        (2, '0'): 2,
        (2, '1'): 1
        }
q4b_fsm = FSM.FSM(transition_table=q4b_transition_table, accepting_states={2})

q4c_transition_table = {
        (1, '0'): 3,
        (1, '1'): 2,
        (2, '0'): 4,
        (2, '1'): 1,
        (3, '0'): 1,
        (3, '1'): 4,
        (4, '0'): 4,
        (4, '1'): 3
        }
q4c_fsm = FSM.FSM(transition_table=q4c_transition_table, accepting_states={1, 2, 4})

if __name__ == "__main__":
    what_question = input("Please enter which question to see? ")
    pattern = input("What would you like to parse to this FSM: ")

    match what_question:
        case '2':
            accepted, states = q2_fsm.run(pattern)
        case '3':
            accepted, states = q3_fsm.run(pattern)
        case '4a':
            accepted, states = q4a_fsm.run(pattern)
        case '4b':
            accepted, states = q4b_fsm.run(pattern)
        case '4c':
            accepted, states = q4c_fsm.run(pattern)
        case _:
            print("ERROR: you did not enter a valid question number")
    
    print(f"For Question {what_question}: FSM accepts is {accepted}")
    print(f"And state history was {states}")
