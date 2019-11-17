# CertPipe
A CertStream monitoring tool. Monitor and alert on Certificate Transparency logs by looking for keyword matches. 

This is a customizable domain discovery, recon, and security tool based on Certificate Transparency log monitoring.

## Usage

### Run with Python

1. Install python dependencies with `pip install -r requirements`.
2. Edit the `config.py` to setup the application.
3. Run the application using `python certpipe.py`

### Run in Docker

Easily create and run a CertPipe Docker image:

1. Edit the `config.py` to setup the application.
2. Build the image using `docker build -t certpipe-docker .` within the CertPipe directory.
3. Start the Docker container in headless mode with `docker run -d certpipe-docker`

### Output

Results can be viewed a few ways:

- Slack alerting. Useful for receiving alerts on mobile device.
- CSV output file found in application directory (certpipe_matches.csv)
- Text output in terminal window

## TODO:

- [x] List of keywords to alert on
- [x] List of keywords to always ignore
- [x] Use text similarity matching algorithms / Text Fuzzing
- [x] Text output
- [x] Basic Logging / Debug
- [x] Slack alerting
- [ ] Syslog output
- [x] CSV file output
- [x] Output type: matched domains
- [ ] Output type: full detailed JSON
- [x] Create a configuration file
- [x] Load configuration from configuration file
- [ ] Scan the domains that match the keywords (urlscan.io?)
- [ ] Save HTTP screenshots of domains that match keywords
- [ ] Improve exception handling
- [x] Add Docker deployment option