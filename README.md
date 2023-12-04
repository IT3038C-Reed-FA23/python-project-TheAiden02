# Python Project

## Checklist

```md
- [x] This task is complete.
```

- [x] Described script purpose.
- [x] Filled out the self-evaluation.
- [x] Filled out the self-reflection.

## Script Purpose

This script is a password manager. It has two modes, store and retrieve. When it is run, it checks to see if the file 'securepass.cvs' exists. If it does then it reads it into a dataframe. If not, it creates a new dataframe. The securepass database contains two columns, labled 'key' and 'password'. The key column functions as a primary key, and each key must be unique. In store mode, the user provides a key and a password as arguments. If the key is not already in use, the script will check to make sure that the password meets some basic requirements, and if it does a new row will be added to the databass containing the supplied arguments. In retrieve mode, the script will first authenticate to make sure that the user is not a hacker. Then it will look through the databass and print the password that matches the provided key. Note that the user must be in the directory that the csv file is saved in, or securepass will create a new csv file in their current location which will not contain the user's previously saved passwords. As a final disclaimer, securepass is not a secure password manager and should not be used to store sensitive information.

## Self-Evaluation

How many points out of 85 do you deserve on this assignment: `0-85`

I think I deserve full points because my project meets all of the requirements and works.

## Self-Reflection
<!-- What did you learn that you found interesting -->

My two greatest takaways from the lab are increased familiarity with the argsparse and pandas modules. I feel much more comfortable using argparse to create switches using the modules different options to do things like specify multiple arguments following a switch and print helpful usage information when the user uses the -h flag. I also got much better at using pandas to read from and write to csv files, and manipulate dataframe objects inside the script. This script can create a dataframe, lookup specific rows using a primary key, and add new rows while maintaining databass integrity. 
### How long it took you to finish this?

In total this project took about 5 hours.
