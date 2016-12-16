from ophyd import (EpicsScaler, EpicsSignal, EpicsSignalRO,
                   Device, DeviceStatus)
from ophyd import Component as Cpt

import time

class NeutronDetector(Device):
    runcontrol_start = Cpt(EpicsSignal, ':CS:RunControl:Start')
    runcontrol_pause = Cpt(EpicsSignal, ':CS:RunControl:Pause')
    runcontrol_stop = Cpt(EpicsSignal, ':CS:RunControl:Stop')
    #runcontrol_message = Cpt(EpicsSignal, ':CS:RunControl:Message')
    #runcontrol_state = Cpt(EpicsSignal, ':CS:RunControl:State')
    runcontrol_stateenum = Cpt(EpicsSignal, ':CS:RunControl:StateEnum')

    def stage(self):
        self._full_path = "UNKNOWN"
        return super().stage()

    def unstage(self):
        return super().unstage()


    def kickoff(self):
        print('kickoff', self.name)
        status = DeviceStatus(self)

        enums = self.runcontrol_stateenum.enum_strs
        def inner_cb(value, old_value, **kwargs):
            old_value, value = enums[int(old_value)], enums[int(value)]
            print('kickoff:', old_value, value, time.time())
            if value == "Run":
                status._finished(success=True)
                self.runcontrol_stateenum.clear_sub(inner_cb)

        self.runcontrol_stateenum.subscribe(inner_cb)

        # Callback will not work with simulation run control
        self.runcontrol_start.put(1)
        #self.start_cmd.put(1,wait=True)

        return status

    def complete(self):
        print('complete', self.name)
        # Callback will not work with simulation run control
        self.runcontrol_stop.put(1)
        #self.stop_cmd.put(1,wait=True)
        status = DeviceStatus(self)
        enums = self.runcontrol_stateenum.enum_strs
        def inner_cb(value, old_value, **kwargs):
            old_value, value = enums[int(old_value)], enums[int(value)]
            print('complete:', kwargs['timestamp'], old_value, value, value == 'Idle')
            if value == "Idle":
                status._finished(success=True)
                self.runcontrol_stateenum.clear_sub(inner_cb)

        self.runcontrol_stateenum.subscribe(inner_cb)

        # Callback will not work with simulation run control
        self.runcontrol_stop.put(1)
        #self.start_cmd.put(1,wait=True)

        return status

    def pause(self):
        # Callback will not work with simulation run control
        self.runcontrol_pause.put(1)
        #self.pause_cmd.put(1,wait=True)

    def resume(self):
        # Callback will not work with simulation run control
        self.runcontrol_pause.put(0)
        #self.pause_cmd.put(0,wait=True)

    def stop(self):
        # Callback will not work with simulation run control
        self.runcontrol_stop.put(1)
        #self.stop_cmd.put(1,wait=True)

detector = NeutronDetector('BL99', name='detector')

# integrated proton charge for the run
bs_pcharge = EpicsSignalRO('BL14B:Det:N1:PChargeIntegrated_RBV', name='bs_pcharge')

# Detector Counts
bs_neutrons = EpicsSignalRO('BL14B:Det:Neutrons', name='bs_neutrons')
bs_neutrons_roi = EpicsSignalRO('BL14B:Det:Neutrons:ROI1', name='bs_neutrons_roi')

# Beam Monitor Counts
bs_bm2 = EpicsSignalRO('BL14B:Det:BM2', name='bs_bm2')
