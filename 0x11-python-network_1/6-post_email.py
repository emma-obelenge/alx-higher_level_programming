#!/usr/bin/python3
"""Check status"""
import requests
import sys


def post():
    """status"""
    data = {"email": sys.argv[2]}
    result = requests.post(sys.argv[1], data)
    print(result.text)


if __name__ == "__main__":
    post()
