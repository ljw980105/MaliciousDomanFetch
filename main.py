import urllib.request


class MaliciousDomainList:
    def __init__(self, url):
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
        print("\n")
        print(self.url_identifier + ":")
        for item in self.dataStr:
            print(" " + item)

    def __contains__(self, url):
        if url in self.dataStr:
            return True
        return False


class MultipleDomainList:
    def __init__(self):
        self.domainCollection = []

    def add_domain_list(self, url):
        self.domainCollection.append(MaliciousDomainList(url))

    def print_all_domain_lists(self):
        for list in self.domainCollection:
            print(list.url_identifier)

    def print_list_contents(self):
        for list in self.domainCollection:
            list.print()

    def search(self, url):
        is_found = False
        for item in self.domainCollection:
            if url in item:
                print("URL {} exists in domain {}".format(url,item.url_identifier))
                is_found = True
        if not is_found:
            print("URL {} cannot be found in any domain list.".format(url))


if __name__ == '__main__':
    # mdl_first = MaliciousDomainList("https://zeustracker.abuse.ch/blocklist.php?download=baddomains")
    # mdl_first.print()
    # mdl_second = MaliciousDomainList("http://mirror1.malwaredomains.com/files/justdomains")
    # mdl_second.print()
    mdl = MultipleDomainList()
    mdl.add_domain_list("https://zeustracker.abuse.ch/blocklist.php?download=baddomains")
    mdl.add_domain_list("http://mirror1.malwaredomains.com/files/justdomains")
    #mdl.print_all_domain_lists()
    mdl.print_all_domain_lists()
    mdl.search("bright.su")

