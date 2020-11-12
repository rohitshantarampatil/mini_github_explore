# mini_github_explore

This program provides a minimal set of services to explore github repositories.


### Input
  Program takes input in following format:
     <organization> <n> <m>
     e.g : google 10 4

  Here, first input is the organization on github, e.g. Google, microsoft etc.
    Second input(n) is the number of most popular repositories based on total forks.
    Third input(m) is the number of top committes.
  To exit the program write 0 and press enter.
### Output
  The program prints n popular repositories( only if n are available in the first place) with respective fork count.
  Then for each repository it prints the username of top m committees with their commit count.
  
### how to run.

#### Required Libraries: requests | sys | json | termcolor

download main.py script
This script uses github API.
Generate a access token on your github with containing feature of access to public repositories.
write your access token in line 9
```
TOKEN = "<your token here>"

```

Run main.py to use the program.
