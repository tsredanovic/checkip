# CheckIP

Resolves public (WAN) IP from supported providers.

## Providers

| Code           | URL                                          |
| -------------- | -------------------------------------------- |
| cloudflare     | https://cloudflare.com/cdn-cgi/trace         |
| dyndns         | http://checkip.dyndns.org/                   |
| freedns        | https://freedns.afraid.org/dynamic/check.php |
| googledomains  | https://domains.google.com/checkip           |
| he             | http://checkip.dns.he.net/                   |
| httpbin        | https://httpbin.org/ip                       |
| ip4only        | http://ip4only.me/api/                       |
| ipfy           | https://api.ipify.org/                       |
| loopia         | http://dns.loopia.se/checkip/checkip.php     |
| myip           | https://api.myip.com                         |
| myonlineportal | https://myonlineportal.net/checkip           |
| noip           | http://ip1.dynupdate.no-ip.com/              |
| nsupdate       | http://ipv4.nsupdate.info/myip               |
| zoneedit       | http://dynamic.zoneedit.com/checkip.html     |

## Installation

```bash
pip install checkip
```

## Usage

## Get IP
Use provider's code to fetch your public (WAN) IP from that provider.

```python
from checkip.ip import get_ip

print(get_ip('cloudflare'))
```

# License

**CheckIP** is a free software under terms of the `MIT License`.

Copyright (C) 2021 by [Toni Sredanović](https://tsredanovic.github.io/), toni.sredanovic@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
