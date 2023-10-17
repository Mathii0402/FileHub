from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
def_url = "http://192.168.144.122:8000"
# Function to scrape data from a specific URL
def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    return None

# Function to extract and organize data for display
def extract_data(soup):
    data = []
    # Extract data based on the page's structure
    links = soup.find_all('a')
    for link in links:
        name = link.get_text()
        href = link.get('href')
        # full_url = os.path.join(base_url, href)  # Create the full URL
        if href.endswith('/'):
            data.append({'name': name, 'type': 'folder'})
        elif href.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            data.append({'name': name, 'type': 'image'})
        else:
            data.append({'name': name, 'type': 'file'})
    return data

# Route to display the scraped and organized data for a specific folder
@app.route('/display_data',methods=['GET', 'POST'])
def display_data():
    global def_url
    if request.method=='POST':
        temp = def_url
        print("displ")
        dir = request.form["url"]

        def_url = temp+dir
        print("dir'==>",dir)
        print("def_url==>",def_url)
        
        
    else:
        def_url = "http://192.168.144.122:8000/"
        # url = request.args.get('url',"http://192.168.144.122:8000/")  # Get the URL parameter
    if def_url:
        soup = scrape_data(def_url)
        if soup:
            # base_url = os.path.dirname(url)  # Extract the base URL
            data = extract_data(soup)
            return render_template('listcont.html', data=data, url=def_url)
    return "Failed to scrape data."

if __name__ == '__main__':
    app.run(debug=True,port=5052,host="0.0.0.0")
