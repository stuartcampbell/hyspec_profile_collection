from bluesky.plans import abs_set, trigger, read

def waitfor_proton_charge(threshold):
    """Set, trigger, read until the current reaches threshold"""
    i = 0
    while True:
        print("LOOP %d" % i)
        yield from trigger(bs_pcharge, wait=True)
        current_pcharge = yield from read(bs_pcharge)
        if reading['bs_pcharge']['value'] < threshold:
            print('DONE')
            break
        i += 1