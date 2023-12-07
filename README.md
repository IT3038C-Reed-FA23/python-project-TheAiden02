# Python Project

## Checklist

```md
- [x] This task is complete.
```

- [x] Described script purpose.
- [x] Filled out the self-evaluation.
- [x] Filled out the self-reflection.

## Script Purpose

This script is a password manager, used to store and retrieve passwords. It has three options: store, retrieve, and view. In store mode, the script takes two arguments, a key and a password. The script adds a row to a csv database using the inputted arguments. Keys must be unique, and passwords must meet some minimum requirements (this is checked with a regular expression). In retrieve mode, the user specifies a key and the script searches through the database until it finds the password associated with that key and prints it to the console. In view mode, the script prints the entire csv file to the console. These options can be combined in any order, and output messages clarify which option they pertain to. 

## Self-Evaluation

How many points out of 85 do you deserve on this assignment: `0-85`

I think I deserve full points because my project meets all of the requirements and works.

## Self-Reflection
<!-- What did you learn that you found interesting -->

My two greatest takaways from the lab are increased familiarity with the argsparse and pandas modules. I feel much more comfortable using argparse to create switches using the module's different options to do things like specify multiple arguments following a switch and print helpful usage information when the user uses the -h flag. I also learned how to use pandas to read from and write to csv files, and manipulate dataframe objects inside the script. This script can create a dataframe, lookup specific rows using a primary key, and add new rows while maintaining databass integrity. 
### How long it took you to finish this?

In total this project took about 7 hours.
