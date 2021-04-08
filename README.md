# Log to Remove Syslog Server

[![Type](https://img.shields.io/badge/Type-Custom_Component-orange.svg)](https://github.com/TheByteStuff/RemoteSyslog_Service)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Send log messages to a Syslog Server using UDP or TCP protocol.  

Messages are delivered in in BSD (legacy Syslog) format.  User may select Facility, Log Level, program.  


## What?

This repository contains multiple files, here is a overview:

File | Purpose
-- | --
`.github/ISSUE_TEMPLATE/feature_request.md` | Template for Feature Requests
`.github/ISSUE_TEMPLATE/issue.md` | Template for issues
`custom_components/remote_syslog/__init__.py` | The component file for the integration.
`custom_components/remote_syslog/manifest.json` | A [manifest file](https://developers.home-assistant.io/docs/en/creating_integration_manifest.html) for Home Assistant.
`custom_components/remote_syslog/services.yaml` | Service definitions.
`custom_components/remote_syslog/syslogger_tcp.py` | A file to hold the class for the TCP logging.
`custom_components/remote_syslog/syslogger_udp.py` | A file to hold the class for the UDP logging.
`custom_components/remote_syslog/sysloggercommon.py` | A file to hold shared classes for the entire integration.
`tests/__init__.py` | Makes the `tests` folder a module.
`tests/test_common.py` | Tests for `custom_components/remote_syslog/sysloggercommon.py`.
`tests/test_syslogger_tcp.py` | Tests for `custom_components/remote_syslog/syslogger_tcp.py`.
`tests/test_syslogger_udp.py` | Tests for `custom_components/remote_syslog/syslogger_udp.py`.
`CONTRIBUTING.md` | Guidelines on how to contribute.
`AutomationsExample.png` | Screenshot from Automations 'Call Service'.
`info.md` | An example on a info file (used by [hacs][hacs]).
`LICENSE` | The license file for the project.
`README.md` | The file you are reading now.
`requirements.txt` | Python packages used by this integration.
`requirements_dev.txt` | Python packages used to provide [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense)/code hints during development of this integration, typically includes packages in `requirements.txt` but may include additional packages


## Installation


1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `remote_syslog`.
4. Download _all_ the files from the `custom_components/remote_syslog/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Add "remote_syslog:" to configuration.yaml.
7. Restart Home Assistant
8. In the HA UI go to "Configuration" -> "Automations", create a mew automation and review service options for Actions.


Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/remote_syslog/__init__.py
custom_components/remote_syslog/manifest.json
custom_components/remote_syslog/services.yaml
custom_components/remote_syslog/syslogger_tcp.py
custom_components/remote_syslog/syslogger_udp.py
custom_components/remote_syslog/sysloggercommon.py
```


## Usage


## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)