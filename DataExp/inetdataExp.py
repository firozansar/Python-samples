#!/usr/bin/env python3
# 
# Example file for retrieving data from the internet
#
import urllib3

http = urllib3.PoolManager()
url = 'https://firozansari.info'

resp = http.request('GET', url)
print(resp.status)
print(resp.data.decode('utf-8'))
print(resp.headers['Server'])
print(resp.headers['Date'])
print(resp.headers['Content-Type'])
print(resp.headers['Last-Modified'])