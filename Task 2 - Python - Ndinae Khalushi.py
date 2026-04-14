#importing required libraries
import requests
import csv

#function definition for printing the url status codes
def url_status_codes(url_file):
    #opening csv file in read mode
    with open(url_file,mode = 'r', encoding = 'utf-8') as urlFile:
        #reading each line of data as a dictionary (urlColumn: urlData)
        urlData = csv.DictReader(urlFile)
        urlColumn = urlData.fieldnames[0] 

        for line in urlData:
            #removing any spaces on each url before requesting the status
            url = line[urlColumn].strip()

            try:
                #get request for each of the urls
                urlStatus = requests.get(url)
                #print status code and the corresponding url if request is successful
                print(f"({urlStatus.status_code}) {url}")

            #excpetion handling for requests that are not successful
            except requests.exceptions.HTTPError as errh:
                print(f"(Error - HTTP) {errh} {url}")
            except requests.exceptions.ReadTimeout as errrt:
                print(f"(Error - Took Too Long (Timeout)) {errrt} {url}")
            except requests.exceptions.ConnectionError as conerr:
                print(f"(Error - No Connection) {conerr} {url}")
            except requests.exceptions.RequestException as errex:
                print(f"(Error - Other Reasons) {errex} {url}")

#defining variable for the csv file name
url_file = "Task 2 - Intern.csv"

#main function
if __name__ == "__main__":
    url_status_codes(url_file)
