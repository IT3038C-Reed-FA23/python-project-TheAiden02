# Python password manager
# Purpose: Allow user to store passwords and associated service in a csv, and retrieve them.
# Options: -h: use information, -s: store new password, -r: retrieve password

import pandas as pd
import argparse as ap
import re
import os.path

# Parse switches and arguments
parser = ap.ArgumentParser() # Create argument parser

parser.add_argument('-s', nargs=2)
parser.add_argument('-r')

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
  try:
    newPassKey = args.s[0]
    newPass = args.s[1]
  except:
    print("An error ocurred. Make sure that two arguments are provided following the -s flag.")
  # Password requirements: At least ten characters, one uppercase, one lowercase, and one number
  validPass = re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{10,}$', newPass)
  if validPass:
    # Add the new password as a row to the dataframe
    df.loc[len(df)] = [newPassKey, newPass]
  else:
    print("Your password does not meet the requirements. Passwords must have at least one uppercase letter, one lowercase letter, and one number. They must contain at least ten characters.")
    exit()

print(df)


# if -r:
  # Check to see if the password exists

  # Find the password with the matching service and print it

# if -h:
  # Print usage information