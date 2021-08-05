#!/usr/bin/env python3
""" Main 0
"""
import sys


if __name__ == '__main__':
    sys.path.append('..')
    from api.v1.auth.auth import Auth

    a = Auth()

    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.authorization_header())
    print(a.current_user())