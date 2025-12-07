class NFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states, epsilon_symbol="ε"):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = set(final_states)
        self.epsilon_symbol = epsilon_symbol

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            key = (state, self.epsilon_symbol)
            if key in self.transitions:
                for nxt in self.transitions[key]:
                    if nxt not in closure:
                        closure.add(nxt)
                        stack.append(nxt)
        return closure

    def simulate_steps(self, input_str):
        log = []
        current_states = self.epsilon_closure({self.start_state})

        log.append({
            "type": "init",
            "states": sorted(current_states)
        })

        for i, symbol in enumerate(input_str):
            if symbol not in self.alphabet:
                return {
                    "accepted": False,
                    "error": f"Símbolo '{symbol}' no pertenece al alfabeto.",
                    "steps": log,
                    "current_states": sorted(current_states),
                    "accepted_states": [],
                }

            next_states = set()
            moves = []

            for state in current_states:
                key = (state, symbol)
                if key in self.transitions:
                    for dst in self.transitions[key]:
                        next_states.add(dst)
                        moves.append((state, symbol, dst))

            if not next_states:
                return {
                    "accepted": False,
                    "error": f"No hay transición con '{symbol}' desde {sorted(current_states)}",
                    "steps": log,
                    "current_states": sorted(current_states),
                    "accepted_states": [],
                }

            closure = self.epsilon_closure(next_states)

            log.append({
                "type": "step",
                "step": i + 1,
                "symbol": symbol,
                "from_states": sorted(current_states),
                "moves": moves,
                "after_epsilon": sorted(closure),
            })

            current_states = closure

        accepted_states = sorted(current_states & self.final_states)

        return {
            "accepted": bool(accepted_states),
            "error": None,
            "steps": log,
            "current_states": sorted(current_states),
            "accepted_states": accepted_states,
        }
