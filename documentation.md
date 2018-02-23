# Documentation
This is the documentation of for the usage of MaliciousDomainFetch.

## Class Definitions and Methods

```python
# initialize multiple domain list
mdl = MultipleDomainList() 
# add a domain list to the mdl instance
mdl.add_domain_list("https:// ....") 
# print the name of all domain lists
mdl.print_all_domain_lists() 
# print all urls contained in the data structure
mdl.print_list_contents()

```

## Commands Line Interface
Use the command below to execute the functions described

* Prints all urls stored in the data structure

```
python main.py -print-contained-domains true

```

* Print the names of all domain lists 

```
python main.py -print-domain-lists true

```

* Search for a domain

```
python main.py -search domain_name

```
### Thanks for viewing! :+1::+1::+1::+1::+1: