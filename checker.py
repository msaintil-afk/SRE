#Simple App check connectivity to a url

import urllib.request as urllib 

def main(url):
    print("Checking Connectivity")

    response = urllib.urlopen(url)
    print("Coonected to", url, "succesfully")
    print ("The response code was:", response.getcode())

print("This is a Site Connectivity Testing App")
input_url = input("Input the url of the site you want to check:")

main(input_url)