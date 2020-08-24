import csv, requests

from bs4 import BeautifulSoup

def getURLs(motherURL):
    """Get a list of urls to race data locations -- one for each (race,year)
    pair. Return list of URLs pointing to individual race results.

    INPUT

    motherURL: url to top results page
    """
    
    response = requests.get(motherURL)
    soup = BeautifulSoup(response.text, "html.parser")

    raceURLs = []
    racesList = soup.body.findAll('a')
    for race in racesList:
        try:
            url = race['href']
            if url[:9] == "/results/":
                raceURLs.append("https://dotwatcher.cc" + url)
        except:
            continue

    return raceURLs


def getRaceGenderSplit(raceURL):
    """Get gender split for a race with raceURL results URL. Return triple
    (race, number_of_women, number_of_men).

    """
    print(".", end='', flush=True) # keep track in stdout
    
    response = requests.get(raceURL)
    soup = BeautifulSoup(response.text, "html.parser")
    
    table_cells = soup.body.findAll('td')
    title = soup.find('title') # 1st title contains race title
    race_name = (' ').join(title.text.split(' ')[:-3])
    
    Nw, Nm = 0, 0
    
    for cell in table_cells:
        if cell.text == 'W':
            Nw += 1
        if cell.text == 'M':
            Nm += 1

    return (race_name, Nw, Nm)

def writeCSV(data, filename):
    
    with open(filename,"w")  as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n") 
        writer.writerows(data)

if __name__ == "__main__":

    motherURL = "https://dotwatcher.cc/results" # base url

    print("Scraping URLs...")
    raceURLs = getURLs(motherURL)

    print("Getting individual race data...", end='')
    gender_data = [("race_name", "Nw", "Nm")]
    for race in raceURLs:
        gender_data.append(getRaceGenderSplit(race))

    print("Writing data to CSV file")
    writeCSV(gender_data, "data/gender_split.csv")
    print("done.")
