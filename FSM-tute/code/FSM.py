class FSM:
    def __init__(self, transition_table, initial_state=1, accepting_states):
        self.transition_table = transition_table
        self.current_state = initial_state
        self.accepting_states = accepting_states
        self.state_history = [initial_state]

    def run(self, input_string):
        for symbol in input_string:
            if (self.current_state, symbol) not in self.transition_table:
                return False, self.state_history
            self.current_state = self.transition_table[(self.current_state, symbol)]
            self.state_history.append(self.current_state)

        return self.current_state in self.accepting_states, self.state_history
