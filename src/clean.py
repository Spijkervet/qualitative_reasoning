from variables import MagnitudeValues, DerivativeValues
from utils import tprint, vprint

def validity_check(state):
    if not state.quantities['Volume'].is_equal(state.quantities['Outflow']):
        return False

    if not intra_edge_cases(state):
        return False

    for s in state.quantities:
        # for quantity in state[s]:
        magnitude = state.quantities[s].magnitude.val
        derivative = state.quantities[s].derivative.val

        # ASSUMPTION: Inflow cannot be zero AND become more negative
        if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
            tprint('{}({}, {}) is an invalid state'.format(s, magnitude, derivative))
            return False

        # ASSUMPTION: Inflow cannot be maximum AND become more positive
        if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
            tprint('{}({}, {}) is an invalid state'.format(s, magnitude, derivative))
            return False

        # ASSUMPTION: Volume cannot be MAX AND become more positive
        if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
            tprint('{}({}, {}) is an invalid state'.format(s, magnitude, derivative))
            return False

        # ASSUMPTION: Volume cannot be ZERO AND become more negative
        if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
            tprint('{}({}, {}) is an invalid state'.format(s, magnitude, derivative))
            return False


        # ASSUMPTION: Outflow cannot be MAX AND become more positive
        if magnitude == MagnitudeValues.MAX and derivative == DerivativeValues.MAX:
            tprint('{}({}, {}) is an invalid state'.format(s, magnitude, derivative))
            return False


        # ASSUMPTION: Outflow cannot be ZERO AND become more negative
        if magnitude == MagnitudeValues.ZERO and derivative == DerivativeValues.MIN:
            tprint('{}({}, {}) is an invalid state'.format(s, magnitude, derivative))
            return False
    tmp = 'STATE {} - '.format(state.id)
    for s in state.quantities:
        magnitude = state.quantities[s].magnitude.val
        derivative = state.quantities[s].derivative.val
        tmp += '{}({}, {}), '.format(s, magnitude, derivative)
    vprint('{} is a valid state'.format(tmp))
    return True


def clean_states(states, model):
    print("\n\n #### INTRA-STATE TRACE #### \n\n")
    new_states = []
    for state in states:
        if validity_check(state):
            new_states.append(state)
    return new_states

def clean_transitions(transitions):
    print("\n\n #### TRANSITION TRACE #### \n\n")
    new_transitions = []
    for (s1, s2) in transitions:
        if transition_validity_check(s1, s2):
            s1.transitions.append(s2)
            new_transitions.append((s1, s2))
    return new_transitions


def transition_validity_check(s1, s2):
    if s1.quantities == s2.quantities:
        return False

    if not edge_cases(s1, s2):
        return False

    for q in s1.quantities:

        # ASSUMPTION: The derivative of state 1 cannot be zero if the magnitude value of state 1 is not equal to state 2
        if s1.quantities[q].derivative.val == DerivativeValues.ZERO:
            if s1.quantities[q].magnitude.val != s2.quantities[q].magnitude.val:
                return False

        if s1.quantities[q].derivative.val == DerivativeValues.MAX:
            # ASSUMPTION: The derivative of state 1 cannot be maximum if the magnitude value of state 2 is smaller than state 1
            if not s2.quantities[q].magnitude.is_gequal(s1.quantities[q].magnitude):
                return False

            # ASSUMPTION: The derivative of state 1 cannot be maximum if the magnitude value of state 1 is zero and the magnitude value of state 2 is not positive.
            if s1.quantities[q].magnitude.val == MagnitudeValues.ZERO:
                if not s2.quantities[q].magnitude.val == MagnitudeValues.PLUS:
                    return False

            # ASSUMPTION: The derivative of state 2 cannot be negative if the derivative of state 1 is maximum
            if s2.quantities[q].derivative.val == DerivativeValues.MIN:
                return False

        if s1.quantities[q].derivative.val == DerivativeValues.MIN:
            # ASSUMPTION: The magnitude of state 2 cannot be greater or equal to state 1 if the derivative of state 1 is negative.
            if not s1.quantities[q].magnitude.is_gequal(s2.quantities[q].magnitude):
                return False

            # ASSUMPTION: The magnitude value of state 2 cannot be positive if the derivative of state 1 is negative and the magnitude value is positive.
            if s1.quantities[q].magnitude.val == MagnitudeValues.MAX:
                if not s2.quantities[q].magnitude.val == MagnitudeValues.PLUS:
                    return False

            # ASSUMPTION: The derivative of state 2 cannot be maximum if the derivative of state 1 is negative
            if s2.quantities[q].derivative.val == DerivativeValues.MAX:
                return False

    tmp = 'STATE {} - '.format(s1.id)
    tmp_2 = 'STATE {} - '.format(s2.id)
    for q in s1.quantities:
        magnitude = s1.quantities[q].magnitude.val
        derivative = s1.quantities[q].derivative.val
        tmp += '{}({}, {}), '.format(q, magnitude, derivative)

    for q in s2.quantities:
        magnitude = s2.quantities[q].magnitude.val
        derivative = s2.quantities[q].derivative.val
        tmp_2 += '{}({}, {}), '.format(q, magnitude, derivative)


    vp = '{} can transition to {}'.format(tmp, tmp_2)
    s1.tooltip = vp
    vprint(vp)

    return True



def edge_cases(s1, s2):
    # ASSUMPTION: The Volume derivative of state 2 cannot be maximum if the Inflow magnitude of state 1 is maximum
    if s1.quantities['Inflow'].magnitude.val == MagnitudeValues.MAX:
        if not s2.quantities['Volume'].derivative.val == DerivativeValues.MAX:
            return False

    # ASSUMPTION: The Volume derivative of state 1 cannot be zero and Volume derivative of state 2 cannot be maximum
    # if the Inflow magnitude of state 1 is maximum and the Inflow derivative of state 1 is negative
    if s1.quantities['Inflow'].magnitude.val == MagnitudeValues.MAX and s1.quantities['Inflow'].derivative.val == DerivativeValues.MIN:
        if s1.quantities['Volume'].derivative.val == DerivativeValues.ZERO and s2.quantities['Volume'].derivative.val == DerivativeValues.MAX:
            return False

    # ASSUMPTION: The Volume derivative of state 2 cannot be maximum if the Inflow derivative of state 1 is negative
    if s1.quantities['Inflow'].derivative.val == DerivativeValues.MIN:
        if s2.quantities['Volume'].derivative.val == DerivativeValues.MAX:
            return False

    return True

def intra_edge_cases(state):
    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.PLUS:
        if state.quantities['Volume'].magnitude.val == MagnitudeValues.MAX:
            return True

    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.ZERO:
        if state.quantities['Volume'].magnitude.val == MagnitudeValues.PLUS and not state.quantities['Volume'].derivative.val == DerivativeValues.MIN:
            return False

        # ASSUMPTION: Inflow cannot be zero, and Volume magnitude cannot be maximum if the volume derivative is zero
        if state.quantities['Volume'].magnitude.val == MagnitudeValues.MAX and state.quantities['Volume'].derivative.val == DerivativeValues.ZERO:
            return False

    # ASSUMPTION: Inflow magnitude cannot be plus while the Volume magnitude is zero and the Volume derivative value is not equal to the maximum
    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.PLUS:
        if state.quantities['Volume'].magnitude.val == MagnitudeValues.ZERO and state.quantities['Volume'].derivative.val != DerivativeValues.MAX:
            return False

    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.ZERO:
        if state.quantities['Volume'].derivative.val == DerivativeValues.MAX:
            return False

    return True

