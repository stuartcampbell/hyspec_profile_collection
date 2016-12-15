import bluesky.plans as bp
from bluesky.plans import abs_set, trigger, read, run_decorator

@run_decorator()
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

@run_decorator()
def time_plan(collection_time):
    yield from bp.kickoff(adara_detector, wait=True)
    yield from bp.sleep(collection_time)
    yield from bp.complete(adara_detector, wait=True)
    # yield from bp.collect(adara_detector)  # they don't actually do this step, but you should

@run_decorator()
def pcharge_plan(pcharge):
    yield from bp.kickoff(adara_detector, wait=True)
    yield from waitfor_proton_charge(pcharge)
    yield from bp.complete(adara_detector, wait=True)
    # yield from bp.collect(adara_detector)  # they don't actually do this step, but you should
