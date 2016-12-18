
# Set up default metadata

RE.md['beamline_id'] = 'HYSPEC'
RE.md['proposal_id'] = None
RE.md['scan_id'] = bs_run_number.value

# Add a callback that prints scan IDs at the start of each scan.

def print_scan_ids(name, start_doc):
    print("Transient Scan ID: {0}".format(start_doc['scan_id']))
    print("Persistent Unique Scan ID: '{0}'".format(start_doc['uid']))

gs.RE.subscribe('start', print_scan_ids)
