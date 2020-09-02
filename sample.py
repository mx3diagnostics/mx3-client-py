#!/usr/bin/env python

from pprint import pprint
from mx3client import MX3Client

TOKEN = "<your_key_here>"


def main():
    client = MX3Client(TOKEN)

    # get users
    all_users = client.get_users()
    pprint(all_users)

    # get measurements
    measurements = client.get_measurements()
    pprint(measurements)

    # get a user from this organisation
    user = client.get_user('<existing-user-id>')
    pprint(user)

    # add or update users
    users = [
      {   # update existing user
        'user_id': '<existing-user-id>',
        'name_first': 'Updated',
        'name_last': 'Name',
        'tags': ['my-group']
      },
      {   # add new user
        'name_first': 'New',
        'name_last': 'User',
      },
    ]
    client.update_users(users)

    # delete user
    client.delete_user('<existing-user-id>')


if __name__ == "__main__":
    main()

