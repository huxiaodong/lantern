#!/usr/bin/env python

import sys
import boto
from boto.s3.key import Key

key = str(sys.argv[1])

if key.endswith('dmg'):
    latest = 'latest.dmg'
elif key.endswith('exe'):
    latest = 'latest.exe'
elif key.endswith('32-bit.deb'):
    latest = 'latest-32.deb'
elif key.endswith('64-bit.deb'):
    latest = 'latest-64.deb'
else:
    print 'File name with full version required. .deb files should end in 32-bit.deb or 64-bit.deb'
    sys.exit(1)   

conn = boto.connect_s3()
b = conn.get_bucket('lantern')

k = Key(b)
k.key = key
k.copy('lantern', latest, preserve_acl=True)

# Since we've just updated the fixed name 'lantest.x' file in our bucket,
# we need to make sure to invalidate it on cloudfront in case anyone's
# using it.
#print 'Invalidating latest installers on CloudFront...'
#c = boto.connect_cloudfront()
#paths = [latest] 
#inval_req = c.create_invalidation_request(u'E1D7VOTZEUYRZT', paths)
#status = c.invalidation_request_status(u'E1D7VOTZEUYRZT', inval_req.id)
