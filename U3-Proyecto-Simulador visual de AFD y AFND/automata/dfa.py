class DFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = set(final_states)

    def simulate_steps(self, input_str):
        steps = []
        current_state = self.start_state

        for i, symbol in enumerate(input_str):
            if symbol not in self.alphabet:
                return {
                    "accepted": False,
                    "error": f"Símbolo '{symbol}' no pertenece al alfabeto.",
                    "steps": steps,
                    "final_state": current_state,
                }

            key = (current_state, symbol)
            if key not in self.transitions:
                return {
                    "accepted": False,
                    "error": f"No hay transición desde '{current_state}' con símbolo '{symbol}'.",
                    "steps": steps,
                    "final_state": current_state,
                }

            next_state = self.transitions[key]
            steps.append({
                "step": i + 1,
                "symbol": symbol,
                "from": current_state,
                "to": next_state,
            })

            current_state = next_state

        accepted = current_state in self.final_states
        return {
            "accepted": accepted,
            "error": None,
            "steps": steps,
            "final_state": current_state,
        }
