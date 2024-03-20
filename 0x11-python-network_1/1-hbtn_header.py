#!/usr/bin/python3
""" sends a request to the URL and displays the 
value of the X-Request-Id variable 
found in the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
