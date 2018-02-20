import urllib.request

class maliciousDomainList:
    def __init__(self, url):
        url = urllib.request.urlopen("https://zeustracker.abuse.ch/blocklist.php?download=baddomains")
        data = url.read()
        parsed_data = str(data, 'utf-8').split("\n")
        self.dataStr = []
        for item in parsed_data:
            self.dataStr.append((item,url))

    def print(self):
        print(self.dataStr[0][1] + ":")
        for item in self.dataStr:
            print(" " + item[0])



if __name__ == '__main__':
    #"https://zeustracker.abuse.ch/blocklist.php?download=baddomains"
    mdl = maliciousDomainList("https://zeustracker.abuse.ch/blocklist.php?download=baddomains")

