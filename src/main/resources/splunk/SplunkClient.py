#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import splunklib.client as client


class SplunkClient(object):

    def __init__(self, host, port, username, password, index, http_config):
        # Create a Service instance and log in
        self.service = client.connect(host=host, port=port, username=username, password=password, scheme=http_config)
        self.index_name = index

    def send(self, event_text, sourcetype='syslog', host=None):
        # Retrieve the index for the data
        index = self.service.indexes[self.index_name]
        # Submit an event over HTTP
        index.submit(event_text, sourcetype=sourcetype, host=host)
