idx = 0
idx_v = 0

def tprint(s):
    return
    global idx

    if 'If state' in s:
        print(s)

    if 'cannot transition' in s:
        print('# TRACE {}: {}'.format(idx, s))
        idx += 1

def vprint(s):
    global idx_v
    idx_v += 1
    print('# TRACE {}: {}'.format(idx_v, s))

