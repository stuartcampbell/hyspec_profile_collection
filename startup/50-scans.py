from bluesky.plans import abs_set, trigger, read

@bluesky.run_decorator(plan_name='waitfor_proton_charge')
def waitfor_proton_charge(threshold):
    """Set, trigger, read until the current reaches threshold"""
    i = 0
    while True:
        print("Waiting for Proton Charge (> %f) LOOP %d" % (threshold, i))
        yield from trigger(bs_pcharge, wait=True)
        current_pcharge = yield from read(bs_pcharge)
        if current_pcharge['bs_pcharge']['value'] >= threshold:
            print('DONE')
            break
        i += 1
