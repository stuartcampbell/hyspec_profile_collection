
# Simple sit and count for a period of time_plan
RE(time_plan(60))
RE(time_plan(10), sample_id='A', purpose='calibration', user='Stuart')

# Simple sit and count for a given proton charge
RE(pcharge_plan(0.01))

# Step scan (separate file for each step)
# args are (mymotor, min, max, step, collection_time)
RE(step_scan(mymotor, 30.0, 40.0, 0.1, 10))

# 'Continuous Step Scan' (One file for whole scan)
# args are (mymotor, min, max, step, collection_time)
RE(continuous_step_scan(mymotor, 30.0, 40.0, 0.1, 10))
