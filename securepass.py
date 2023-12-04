# Python password manager
# Purpose: Allow user to store passwords and associated key in a csv, and retrieve them.
# Options: -h: usage information, -s: store new password, -r: retrieve password

import pandas as pd
import argparse as ap
import re
import os.path

def authenticate(): # Bulletproof authentication
  hacker = input('Are you a hacker? You have to tell the truth (y/n): ')

  if hacker == 'y' or hacker == 'Y':
    print("Please refrain from hacking this user's passwords. They don't have anything interesting or valuable anyway. Thank you!")
    exit()
  elif hacker == 'n' or hacker == 'N':
    print("Oh, that's good!")
  else:
    print("Hmmmm. Not a y or n. Well, lucky for you, we here at securepass (tm) prefer to give our users the benefit of the doubt!")

# Parse switches and arguments
parser = ap.ArgumentParser(description='A password manager which can write to and read from a csv file, using unique keys to reference stored passwords.') # Create argument parser

parser.add_argument('-s', '--store', nargs=2, help='Store a new entry in the password manager. Note that passwords must contain at least one uppercase letter, one lowercase letter, and one number, and be at least ten characters long.', metavar=('KEY', 'PASSWORD'))
parser.add_argument('-r', '--retrieve', help='Retrieve a password from the password manager', metavar='KEY')
parser.add_argument('-v', '--view', action='store_true', help='View entire database')

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



if args.store: # Store mode: add a new line to df, and write df to securepass.csv
  newPassKey = args.store[0]
  newPass = args.store[1]

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
    # Write the updated dataframe to our csv
    df.to_csv('securepass.csv', index=False)
  else:
    print("Your password does not meet the requirements. Passwords must have at least one uppercase letter, one lowercase letter, and one number. They must contain at least ten characters.")



if args.retrieve: # Retrieve mode: find the password with the matching key
  authenticate()
  passKey = args.retrieve
  found = False

  # Find the password with the matching key
  for i in df.index:
    if df.key[i] == passKey:
      output = df.password[i]
      found = True

  if found:
    print("Your password is: " + output)
  else:
    print("No match was found for the provided key. ")


if args.view:
  authenticate()
  print(df)