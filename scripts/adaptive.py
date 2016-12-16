from bluesky.plans import adaptive_scan
from bluesky.callbacks import LivePlot
from bluesky.examples import motor, det

# Adaptive Rocking curve scan using just the neutron counts
# (either total or ROI).  This will not trigger the ADARA
# system - therefore no NeXus file will be created.

## TODO : Update with realistic values for the steps, etc....

RE(adaptive_scan([bs_neutrons_roi], 'bs_neutrons_roi', bs_axis1,
                 start=-15,
                 stop=10,
                 min_step=0.01,
                 max_step=5,
                 target_delta=.05,
                 backstep=True),
   LivePlot('bs_neutrons_roi', 'bs_axis1', markersize=5, marker='o'))
