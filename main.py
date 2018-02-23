import urllib.request
import argparse

"""
A class that represents a domain list.
"""
class DomainList:
    def __init__(self, url):
        """ execute a http fetch with the given link and store in to data structure
        :param url: The url used to initialize and populate the domain list
        """
        self.dataStr = []
        self.url_identifier = url

        url_object = urllib.request.urlopen(url)
        data = url_object.read()
        parsed_data = str(data, 'utf-8').split("\n")
        for item in parsed_data:
            if len(item) == 0 or item[0] == "#":
                continue
            self.dataStr.append(item)

    def print(self):
        """ print the all the urls contained in the data structure
        :return: functions is void
        """
        print("\n")
        print(self.url_identifier + ":")
        for item in self.dataStr:
            print(" " + item)

    def __contains__(self, url):
        """
        Determines if the url is contained in the list.
        :param url: the url to be tested
        :return: true iff. the data structure array contains the url
        """
        if url in self.dataStr:
            return True
        return False

"""
A class that represents a collection of domain lists.
"""
class MultipleDomainList:
    def __init__(self):
        """
        Initialize the object with an empty list of DomainList objects.
        """
        self.domainCollection = []

    def add_domain_list(self, url):
        """
        :param url: Initialize a domainList object with the url, then add to domainCollection
        :return: void
        """
        self.domainCollection.append(DomainList(url))

    def print_all_domain_lists(self):
        """
        Print the names of all domain lists
        :return: void
        """
        for list in self.domainCollection:
            print(list.url_identifier)

    def print_list_contents(self):
        """
        Prints all urls stored in the data structure
        :return: void
        """
        for list in self.domainCollection:
            list.print()

    def search(self, url):
        """
        Check if url can be found in the data structure: If true, print the domain list it exists in.
        Otherwise, inform the user the url cannot be found
        :param url: the url to be searched
        :return: void
        """
        is_found = False
        for item in self.domainCollection:
            if url.strip() in item:
                print("URL {} exists in domain {}".format(url,item.url_identifier))
                is_found = True
        if not is_found:
            print("URL {} cannot be found in any domain list.".format(url))


if __name__ == '__main__':
    mdl = MultipleDomainList()
    mdl.add_domain_list("https://zeustracker.abuse.ch/blocklist.php?download=baddomains")
    mdl.add_domain_list("http://mirror1.malwaredomains.com/files/justdomains")

    parser = argparse.ArgumentParser(description='Malicious Domain Parser')
    parser.add_argument("-print-contained-domains", "--pcd", type=bool, nargs=1,
                        metavar="contained-domains", default=None,
                        help="Prints all urls stored in the data structure")
    parser.add_argument("-print-domain-lists", "--pdl", type=bool, nargs=1,
                        metavar="domain-list", default=None,
                        help="Print the names of all domain lists")
    parser.add_argument("-search", "--search", type=str, nargs=1,
                        metavar="search-item", default=None,
                        help="Search for a domain")

    args = parser.parse_args()

    if args.pcd != None:
        mdl.print_list_contents()
    elif args.pdl != None:
        mdl.print_all_domain_lists()
    elif args.search != None:
        mdl.search(args.search[0])

