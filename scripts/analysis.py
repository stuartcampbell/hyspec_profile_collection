# I've setup Metadatastore config in ~/.config/metadatastore/connection.yml
# I've setup Filestore config in ~/.config/filestore/connection.yml

from databroker import db

# Find run number 154338
db(scan_id=154338)

# All started on sunday
db(start_time='2016-12-18')

# All started/stopped on sunday
db(start_time='2016-12-18', stop_time='2015-12-18')

# Get the 'db_neutrons' data into a pandas dataframe
h = db(scan_id=154338)
t = db.get_table(h,fields=['bs_neutrons'])

