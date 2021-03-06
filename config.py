#!/bin/python

###########################################################################
#
# Copyright 2019 Devin Calado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###########################################################################

# Set to True to enable verbose logging. Set to False to only output the matched keywords and domains.
enable_logging = True

# These keywords will be fuzzed so that look-alike domain matches are identified. 
keywords = ['google', 'amazon', 'facebook']

# These keywords will NOT be fuzzed. Useful for searching for domains that contains specific words (i.e., 'prod', 'database', 'bucket', etc...). 
no_fuzz_keywords = ['userdata', 'admin', 'database']

# These keywords will be ingored.  If a domain contains any of these keywords, then it will not be included in the results.
ignore_keywords = []

# Save all matched domains to a csv file.  CSV file has three columns (timestamp, matched_keyword, domain).
enable_csv_output = True
output_csv_file = "certpipe_matches.csv"

# Alert bulk sending.  Groups alert messages together into single alert every n seconds.
alert_send_frequency = 30

# Slack alerting configuration.
enable_slack = False
slack_token = "<INSERT SLACK API TOKEN>"
slack_channel = "<INSERT SLACK CHANNEL>"

# Mattermost alerting configuration. Requires an Incoming Webhook to be created and added to a channel.
enable_mattermost = False
mattermost_webhook_url = "https://<INSERT MATTERMOST SITE>/hooks/<INSERT GENERATED KEY>"

# Submit matched domains to URLScan.io and output links to the scan results in output / alerts. 
enable_urlscanio = False
urlscanio_api_key = "<INSERT URLSCAN.IO API KEY>"

# Syslog configuration TODO
#enable_syslog = False
#syslog_server = "10.10.11.18"
#syslog_port = 514
