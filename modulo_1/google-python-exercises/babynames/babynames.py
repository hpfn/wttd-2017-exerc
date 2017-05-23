#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'r') as babynames:
        html_file = babynames.read() # .split('\n')

    pop_year = re.search(
        r".*(Popularity in (\d{4})).*",
        html_file)
    year_rank_list = pop_year.group(2)

    person_rank_lst = []
    html_file = html_file.split('\n')
    for a in html_file:
        full_name = re.search(
            r"<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",
            a)
        if full_name:
            rank = full_name.group(1)
            male_name = full_name.group(2)
            female_name = full_name.group(3)
            person_rank_lst.append("%s %s" % (male_name, rank))
            person_rank_lst.append("%s %s" % (female_name, rank))

    person_rank_lst.sort()
    person_rank_lst.insert(0, year_rank_list)

    return person_rank_lst


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
        # each year has his own file
        for file in args:
            year_name_rank_lst = extract_names(file)
            year = year_name_rank_lst[0]
            year_file =open(year, 'w')
            print('\n'.join(year_name_rank_lst), file=year_file)


if __name__ == '__main__':
    main()
