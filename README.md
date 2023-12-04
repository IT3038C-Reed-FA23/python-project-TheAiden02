# Python Project

## Checklist

```md
- [x] This task is complete.
```

- [x] Described script purpose.
- [x] Filled out the self-evaluation.
- [x] Filled out the self-reflection.

## Script Purpose

This script is a password manager. It has two modes, store and retrieve. When it is run, it checks to see if the file 'securepass.cvs' exists. If it does then it reads it into a dataframe. If not, it creates a new dataframe. The securepass database contains two columns, labled 'key' and 'password'. The key column functions as a primary key, and each key must be unique. In store mode, the user provides a key and a password as arguments. If the key is not already in use, a new row will be added to the databass containing the supplied arguments. In retrieve mode, the script will first authenticate to make sure that the user is not a hacker. THen it will look through the databass and print the password that matches the provided key. Note that the user must be in the directory that the database is saved in, or securepass will create a new databass file in their current location which will not contain the user's previously saved passwords. As a final disclaimer, securepass is not a secure password manager and should not be used to store actual sensitive information.

## Self-Evaluation

How many points out of 85 do you deserve on this assignment: `0-85`

I think I deserve full points because my project meets all of the requirements and works.

## Self-Reflection
<!-- What did you learn that you found interesting -->

My two greatest takaways from the lab are increased familiarity with the argsparse and pandas modules. I feel much more comfortable creating switches with different numbers of arguments and providing useful usage information with the -h flag.
### How long it took you to finish this?

In total this project took about 5 hours.
