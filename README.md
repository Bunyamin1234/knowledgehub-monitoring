# Knowledge Hub Monitoring

An initial Python script for collecting monitoring settings.

## Requirements

- Python 3.12 or newer

## Run the script

```bash
python monitor.py
```

On Linux, use `python3 monitor.py`.

Enter a hostname, IP address, and comma-separated metric names.
The script removes surrounding spaces and ignores empty metric entries,
then displays the settings.

## Current scope

Settings are stored in memory only. The script does not connect to
servers, collect live measurements, or validate hostnames and IP addresses.

## Tests completed

- Normal input displays the hostname, IP address, and metric list.
- Extra spaces and consecutive commas produce no empty metric entries.