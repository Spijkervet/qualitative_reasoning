
idx = 0
def tprint(s):
    global idx
    print('# TRACE {}: {}'.format(idx, s))

    if not 'If state' in s:
        idx += 1
