from variables import MagnitudeValues, DerivativeValues

def validity_check(state):
    for s in state:

        if not state['Volume'].is_equal(state['Outflow']):
            return False

        # for quantity in state[s]:
        magnitude = state[s].magnitude.val
        derivative = state[s].derivative.val

        # ASSUMPTION: Inflow cannot be zero AND become more negative
        if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
            return False
        # ASSUMPTION: Inflow cannot be maximum AND become more positive
        if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
            return False

        # ASSUMPTION: Volume cannot be MAX AND become more positive
        if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
            return False
        # ASSUMPTION: Volume cannot be ZERO AND become more negative
        if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
            return False

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
    if s1 == s2:
        return False

    # if s1['Bathtub']['Volume'].is_equal(s2['Drain']['Outflow']) or s1['Drain']['Outflow'].is_equal(s2['Bathtub']['Volume']):
        # return True
    return True

def clean_transitions(transitions):
    new_transitions = []
    for (s1, s2) in transitions:
        if transition_validity_check(s1, s2):
            # print("VALID")
            new_transitions.append((s1, s2))
    return new_transitions
