from ophyd import (EpicsScaler, EpicsSignal, EpicsSignalRO,
                   Device, DeviceStatus)
from ophyd import Component as Cpt

from bluesky.examples import NullStatus

class NeutronDetector(Device):
    start_cmd = Cpt(EpicsSignal, ':Start')
    pause_cmd = Cpt(EpicsSignal, ':Pause')
    stop_cmd = Cpt(EpicsSignal, ':Stop')

    def stage(self):
        self._full_path = "UNKNOWN"
        return super().stage()

    def unstage(self):
        return super().unstage()


    def kickoff(self):
        print('kickoff', self.name)
        # Callback will not work with simulation run control
        self.start_cmd.put(1)
        #self.start_cmd.put(1,wait=True)
        status = DeviceStatus(self)
        #status = NullStatus()
        return status

    def complete(self):
        print('complete', self.name)
        # Callback will not work with simulation run control
        self.stop_cmd.put(1)
        #self.stop_cmd.put(1,wait=True)
        status = DeviceStatus(self)
        #status = NullStatus()
        return status

    def pause(self):
        # Callback will not work with simulation run control
        self.pause_cmd.put(1)
        #self.pause_cmd.put(1,wait=True)

    def resume(self):
        # Callback will not work with simulation run control
        self.pause_cmd.put(0)
        #self.pause_cmd.put(0,wait=True)

    def stop(self):
        # Callback will not work with simulation run control
        self.stop_cmd.put(1)
        #self.stop_cmd.put(1,wait=True)

detector = NeutronDetector('BL99:CS:RunControl', name='detector')

# integrated proton charge for the run
bs_pcharge = EpicsSignalRO('BL14B:Det:N1:PChargeIntegrated_RBV', name='bs_pcharge')

# Detector Counts
bs_neutrons = EpicsSignalRO('BL14B:Det:Neutrons', name='bs_neutrons')
bs_neutrons_roi = EpicsSignalRO('BL14B:Det:Neutrons:ROI1', name='bs_neutrons_roi')

# Beam Monitor Counts
bs_bm2 = EpicsSignalRO('BL14B:Det:BM2', name='bs_bm2')
