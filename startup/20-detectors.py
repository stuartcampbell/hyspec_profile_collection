from ophyd import (EpicsScaler, EpicsSignal, EpicsSignalRO, Device, StatsPlugin)
from ophyd import Component as Cpt


# integrated proton charge for the run
bs_pcharge = EpicsSignalRO('BL14B:Det:N1:PChargeIntegrated_RBV', name='bs_pcharge')

# Detector Counts
bs_neutrons = EpicsSignalRO('BL14B:Det:Neutrons', name='bs_neutrons')
bs_neutrons_roi = EpicsSignalRO('BL14B:Det:Neutrons:ROI1', name='bs_neutrons_roi')

# Beam Monitor Counts
bs_bm2 = EpicsSignalRO('BL14B:Det:BM2', name='bs_bm2')
