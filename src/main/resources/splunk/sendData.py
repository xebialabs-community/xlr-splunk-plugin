#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from splunk.SplunkClient import SplunkClient

if splunkServer is None:
    print "No server provided."
    sys.exit(1)

host = splunkServer['host']
port = splunkServer['port']
username = splunkServer['username']
password = splunkServer['password']
https_enabled = splunkServer['httpsEnabled']

# Set up the example logger
# Arguments are your access token and the project ID
if https_enabled:
    log = SplunkClient(host, port, username, password, index, "https")
else:
    log = SplunkClient(host, port, username, password, index, "http")

# Send a log; will pick up the default value for ``source``.
log.send(data,sourcetype='syslog')
