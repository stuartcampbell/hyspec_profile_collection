# Make ophyd listen to pyepics.
from ophyd import setup_ophyd
setup_ophyd()

# Define some environment variables (for now)
import os
os.environ['MDS_HOST'] = 'localhost'
os.environ['MDS_PORT'] = '27017'
os.environ['MDS_DATABASE'] = 'metadatastore-production-v1'
os.environ['MDS_TIMEZONE'] = 'US/Eastern'
os.environ['FS_HOST'] = 'localhost'
os.environ['FS_PORT'] = '27017'
os.environ['FS_DATABASE'] = 'filestore-production-v1'

# Connect to metadatastore and filestore.
from metadatastore.mds import MDS, MDSRO
from filestore.fs import FileStoreRO
from databroker import Broker
mds_config = {'host': 'localhost',
              'port': 27017,
              'database': 'metadatastore-production-v1',
              'timezone': 'US/Eastern'}
fs_config = {'host': 'localhost',
             'port': 27017,
             'database': 'filestore-production-v1'}
mds = MDS(mds_config)
#mds_readonly = MDSRO(mds_config)
# As we aren't writing any files at the moment, use
# the readonly version
fs_readonly = FileStoreRO(fs_config)

db = Broker(mds, fs_readonly)


# Subscribe metadatastore to documents.
# If this is removed, data is not saved to metadatastore.
from bluesky.global_state import gs
gs.RE.subscribe('all', mds.insert)

# Import matplotlib and put it in interactive mode.
import matplotlib.pyplot as plt
plt.ion()

# Make plots update live while scans run.
from bluesky.utils import install_qt_kicker
install_qt_kicker()

# Optional: set any metadata that rarely changes.

# convenience imports
from ophyd.commands import *
from bluesky.callbacks import *
from bluesky.spec_api import *
from bluesky.global_state import gs, abort, stop, resume
from bluesky.plan_tools import print_summary
from time import sleep
import numpy as np

RE = gs.RE  # convenience alias
