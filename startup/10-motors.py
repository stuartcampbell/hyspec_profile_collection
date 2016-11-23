from ophyd import (PVPositioner, EpicsMotor, EpicsSignal, EpicsSignalRO,
                   PVPositionerPC, Device)
from ophyd import Component as Cpt


# Aperture 1 left/top/right/bottom
bs_a1l = EpicsMotor('BL14B:Mot:a1l', name='bs_a1l')
bs_a1t = EpicsMotor('BL14B:Mot:a1t', name='bs_a1t')
bs_a1r = EpicsMotor('BL14B:Mot:a1r', name='bs_a1r')
bs_a1b = EpicsMotor('BL14B:Mot:a1b', name='bs_a1b')

# Aperture 2 left/top/right/bottom
bs_a2l = EpicsMotor('BL14B:Mot:a2l', name='bs_a2l')
bs_a2t = EpicsMotor('BL14B:Mot:a2t', name='bs_a2t')
bs_a2r = EpicsMotor('BL14B:Mot:a2r', name='bs_a2r')
bs_a2b = EpicsMotor('BL14B:Mot:a2b', name='bs_a2b')

# Sample (table) Z rotation
bs_s1 = EpicsMotor('BL14B:Mot:s1', name='bs_s1')

# Sample translation upper (y), lower (x)
bs_stu = EpicsMotor('BL14B:Mot:stu', name='bs_stu)
bs_stl = EpicsMotor('BL14B:Mot:stl', name='bs_stl)

# Sample goniometer upper (y), lower (x) tilt
bs_sgu = EpicsMotor('BL14B:Mot:sgu', name='bs_sgu)
bs_sgl = EpicsMotor('BL14B:Mot:sgl', name='bs_sgl)

# Sample Axes (stick on sample environment, etc)
bs_axis1 = EpicsMotor('BL14B:Mot:Axis1', name='bs_Axis1)
bs_axis2 = EpicsMotor('BL14B:Mot:Axis2', name='bs_Axis2)                      
 
