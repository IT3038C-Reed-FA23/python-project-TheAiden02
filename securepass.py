# Python password manager
# Purpose: Allow user to store passwords and associated service in a csv, and retrieve them.
# Options: -h: use information, -s: store new password, -r: retrieve password

import pandas as pd
import argparse as ap
import re
import os.path

# Parse switches and arguments
parser = ap.ArgumentParser(description='A password manager which can write to and read from a csv file, using unique keys to reference stored passwords.') # Create argument parser

parser.add_argument('-s', '--store', nargs=2, help='Store a new entry in the password manager.', metavar=('KEY', 'PASSWORD'))
parser.add_argument('-r', '--retrieve', help='Retrieve a password from the password manager', metavar='KEY')

args = parser.parse_args()

# Read in password csv, or create a new dataframe if it does not yet exist
if os.path.isfile('securepass.csv'):
  df = pd.read_csv('securepass.csv')
else:
  data = {
    "key": [],
    "password": []
  }

  df = pd.DataFrame(data)



if args.s:
  newPassKey = args.s[0]
  newPass = args.s[1]

  # Make sure the key does not already exist
  for ind in df.index:
    if newPassKey == df["key"][ind]:
      print("Key already exists. Every password must have a unique key.")
      exit()

  # Password requirements: At least ten characters, one uppercase, one lowercase, and one number
  validPass = re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{10,}$', newPass)


  if validPass:
    # Add the new password as a row to the dataframe
    df.loc[len(df)] = [newPassKey, newPass]
  else:
    print("Your password does not meet the requirements. Passwords must have at least one uppercase letter, one lowercase letter, and one number. They must contain at least ten characters.")
    exit()

  # Write the updated dataframe to our csv
  df.to_csv('securepass.csv', index=False)


if args.r:

  # Bulletproof authentication
  hacker = input('Are you a hacker? You have to tell the truth (y/n): ')

  if hacker == 'y' or hacker == 'Y':
    print("Please refrain from hacking this user's passwords. They don't have anything interesting or valuable anyway. Thank you!")
    exit()
  elif hacker == 'n' or hacker == 'N':
    print("Oh, that's good!")
  else:
    print("Hmmmm. Not a y or n. Well, lucky for you, we here at securepass (tm) prefer to give our users the benefit of the doubt!")

  passKey = args.r

  # Find the password with the matching key and print it
  for i in df.index:
    if df.key[i] == passKey:
      print("Your password is: " + df.password[i])
      exit()

  # If no password matches the key:
  print("No match was found for the provided key. ")


# if -h:
  # Print usage information