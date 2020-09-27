# **Python-Mini-Projects**

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/PhilRoli/Python-Mini-Projects/pulls) [![GitHub last commit](https://img.shields.io/github/last-commit/philroli/Python-Mini-Projects)](https://github.com/PhilRoli/Python-Mini-Projects/pulls) ![GitHub repo size](https://img.shields.io/github/repo-size/philroli/Python-Mini-Projects)

Just some Scripts I made that help me in stuff I have to do often and dont want to do by hand all the time.
Below you will find a list with explination to nearly all files in this repo.

Dont know if anyone will find this usefull, but I thought I would make it my first public repo.
Also please ignore my mixture of English and German in certain files.

---

## Files

---

- **[cpu_information.py](/cpu_information.py)**: Displays information about your CPU (Cores, Usage, Frequenzy) (Works in VSC, but not when started seperatly, checked PATH).

- **[get_google.py](/get_google.py)**: Checks if Google.com is availibe, then gives back result if internet is availible or not.

- **[getssid.py](/getssid.py)**: SSID part failed, now returns the IP Address

- **[ip_address.py](/ip_address.py)**: Returns the Users Host-Name and Ip-Address in a more beautiful form.

- **[network_details.py](/network_details.py)**: Returns the Users Interface, Ip-Address, Host-Name, ~~Broadcast-IP~~ (Not possible if acces to Wifi Router is not possible).

- **[network_speed.py](/network_speed.py)**: Gets the Users Down and Upload speed with the Speedtest Module, then returns the resault in a table.

- **[network_speed_ProgressBar.py](/network_speed_ProgressBar.py)**: Combines the [network_speed.](/network_speed.py), [network_details](/network_details.py) and [get_google](/get_google.py) files to check internet availability, then return the internet details. If no Internet is availibly return that.

- **[network_time.py](/network_time.py)**: Made as a test file to run the network speed file multiple times, to test the time the test takes. But not working as intend.

- **[online_information.py](/online_information.py)**: [network_speed_ProgressBar](/network_speed_ProgressBar.py) without the Progress bar and internet check.

- **[outside_ip.py](/outside_ip.py)**: Uses a ``get('').text`` request to ``https://api.ipify.org`` to get the oustide ip of the local machine and outputs it to the terminal.

- **[url_shortener.py](/url_shortener.py)**: Shortens any given url with the pyshorteners module.

<!-- ---

## Folders

---

-->
