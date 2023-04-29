#!/usr/bin/python3
"""
Displays the X-request-Id header variable of a HTTP request to a given URL, by the user
"""
import sys
import request


if __name__ =="__main__":
    url = sys.argv[1]

    r = request.get(url)
    print(r.headers.get("X-Request-Id"0)
