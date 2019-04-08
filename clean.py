from variables import MagnitudeValues, DerivativeValues
from utils import tprint

def validity_check(state):
    for s in state.quantities:

        if not state.quantities['Volume'].is_equal(state.quantities['Outflow']):
            # tprint("VOLUME != OUTFLOW")
            return False

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

    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.ZERO:
        if state.quantities['Volume'].derivative.val == DerivativeValues.MAX:
            tprint('{}({}, {}) and {}({},{}) is an invalid state'.format('Inflow', magnitude, '?', 'Volume', '?', state.quantities['Volume'].derivative.val))
            return False

    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.ZERO:
        if state.quantities['Volume'].magnitude.val == MagnitudeValues.MAX and state.quantities['Volume'].derivative.val == DerivativeValues.ZERO:
            tprint('{}({}, {}) and {}({},{}) is an invalid state'.format('Inflow', state.quantities['Inflow'].magnitude.val, '?', 'Volume', state.quantities['Volume'].magnitude.val, state.quantities['Volume'].derivative.val))
            return False

    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.ZERO:
        if state.quantities['Volume'].magnitude.val == MagnitudeValues.MAX:
            tprint('{}({},{}) and {}({},{}) is an invalid state'.format('Inflow', state.quantities['Inflow'].magnitude.val, '?', 'Volume', state.quantities['Volume'].magnitude.val, '?'))
            return False

    if state.quantities['Inflow'].magnitude.val == MagnitudeValues.PLUS:
        if state.quantities['Volume'].magnitude.val == MagnitudeValues.ZERO and state.quantities['Volume'].derivative.val != DerivativeValues.MAX:
            tprint('{}({},{}) and {}({},{}) is an invalid state'.format('Inflow', state.quantities['Inflow'].magnitude.val, '?', 'Volume', state.quantities['Volume'].magnitude.val, '?'))
            return False
    return True




def clean_states(states):
    new_states = []
    for state in states:
        if validity_check(state):
            new_states.append(state)
    return new_states

# POINT VALUES: MAX / MIN, ZERO, PLUS
def transition_validity_check(s1, s2):
    if s1.quantities == s2.quantities:
        return False

    for q in ['Volume', 'Inflow']:
        if s1.quantities[q].derivative.val == DerivativeValues.ZERO:
            if s1.quantities[q].magnitude.val != s2.quantities[q].magnitude.val:
                tprint('If state 1: {}({},{}):'.format(q, '?', s1.quantities[q].derivative.val))
                tprint('{}({},{}) cannot transition to {}({},{})'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val, q, s2.quantities[q].magnitude.val, s2.quantities[q].derivative.val))
                return False

        if s1.quantities[q].derivative.val == DerivativeValues.MAX:
            if not s2.quantities[q].magnitude.is_gequal(s1.quantities[q].magnitude):
                tprint('If state 1: {}({},{}):'.format(q, '?', s1.quantities[q].derivative.val))
                tprint('{}({},{}) cannot transition to {}({},{})'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val, q, s2.quantities[q].magnitude.val, s2.quantities[q].derivative.val))
                return False

        if s1.quantities[q].derivative.val == DerivativeValues.MIN:
            if not s1.quantities[q].magnitude.is_gequal(s2.quantities[q].magnitude):
                tprint('If state 1: {}({},{}):'.format(q, '?', s1.quantities[q].derivative.val))
                tprint('{}({},{}) cannot transition to {}({},{})'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val, q, s2.quantities[q].magnitude.val, s2.quantities[q].derivative.val))
                return False

        if s1.quantities[q].derivative.val == DerivativeValues.MAX:
            if s2.quantities[q].derivative.val == DerivativeValues.MIN:
                tprint('If state 1: {}({},{}):'.format(q, '?', s1.quantities[q].derivative.val))
                tprint('{}({},{}) cannot transition to {}({},{})'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val, q, s2.quantities[q].magnitude.val, s2.quantities[q].derivative.val))
                return False

        if s1.quantities[q].derivative.val == DerivativeValues.MIN:
            if s2.quantities[q].derivative.val == DerivativeValues.MAX:
                tprint('If state 1: {}({},{}):'.format(q, '?', s1.quantities[q].derivative.val))
                tprint('{}({},{}) cannot transition to {}({},{})'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val, q, s2.quantities[q].magnitude.val, s2.quantities[q].derivative.val))
                return False

        if s1.quantities[q].magnitude.val == MagnitudeValues.MAX:
            if s1.quantities[q].derivative.val == DerivativeValues.MIN:
                if not s2.quantities[q].magnitude.val == MagnitudeValues.PLUS:
                    tprint('If state 1: {}({},{}):'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val))
                    tprint('{}({},{}) cannot transition to {}({},{})'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val, q, s2.quantities[q].magnitude.val, s2.quantities[q].derivative.val))
                    return False

        if s1.quantities[q].magnitude.val == MagnitudeValues.ZERO:
            if s1.quantities[q].derivative.val == DerivativeValues.MAX:
                if not s2.quantities[q].magnitude.val == MagnitudeValues.PLUS:
                    tprint('If state 1: {}({},{}):'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val))
                    tprint('{}({},{}) cannot transition to {}({},{})'.format(q, s1.quantities[q].magnitude.val, s1.quantities[q].derivative.val, q, s2.quantities[q].magnitude.val, s2.quantities[q].derivative.val))
                    return False

    if s1.quantities['Inflow'].magnitude.val == MagnitudeValues.MAX:
        if not s2.quantities['Volume'].derivative.val == DerivativeValues.MAX:
            tprint('If state 1: {}({},{}):'.format('Inflow', s1.quantities['Inflow'].magnitude.val, s1.quantities['Inflow'].derivative.val))
            tprint('{}({},{}) cannot transition to {}({},{})'.format('Inflow', s1.quantities['Inflow'].magnitude.val, s1.quantities['Inflow'].derivative.val, 'Volume', s2.quantities['Volume'].magnitude.val, s2.quantities['Volume'].derivative.val))
            return False

    return True

def clean_transitions(transitions):
    new_transitions = []
    for (s1, s2) in transitions:
        if transition_validity_check(s1, s2):
            s1.transitions.append(s2)
            new_transitions.append((s1, s2))
    return new_transitions
