from variables import MagnitudeValues, DerivativeValues

def validity_check(state):
    for s in state:
        for quantity in state[s]:
            magnitude = state[s][quantity].magnitude.val
            derivative = state[s][quantity].derivative.val

            if quantity == "Inflow":
                # ASSUMPTION: Inflow cannot be zero AND become more negative
                if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
                    return False
                # ASSUMPTION: Inflow cannot be maximum AND become more positive
                if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
                    return False

            elif quantity == "Volume":
                # ASSUMPTION: Volume cannot be MAX AND become more positive
                if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
                    return False
                # ASSUMPTION: Volume cannot be ZERO AND become more negative
                if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
                    return False
            elif quantity == "Outflow":
                # ASSUMPTION: Outflow cannot be MAX AND become more positive
                if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
                    return False
                # ASSUMPTION: Outflow cannot be ZERO AND become more negative
                if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
                    return False
    return True




def clean_states(states):
    new_states = []
    for state in states:
        if validity_check(state):
            new_states.append(state)
    return new_states


def transition_validity_check(s1, s2):
    print(s1)
    print(s2)
    return True

def clean_transitions(transitions):
    new_transitions = []
    for (s1, s2) in transitions:
        if transition_validity_check(s1, s2):
            new_transitions.append((s1, s2))
        break
    return new_transitions
