
from flask import Flask,render_template,request,redirect,url_for,session
import socket,subprocess
import platform
import requests
from bs4 import BeautifulSoup


ip_url=""
def_url = ""
app = Flask(__name__)
app.secret_key = "hvggfgxhdergfcfchjtvj"





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
    ct = 1
    for link in links:
        name = link.get_text()
        href = link.get('href')

        print(href,ct)
        ct+=1
        if href.endswith('/'):
            data.append({'name': name, 'type': 'folder'})
        elif href.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            data.append({'name': name, 'type': 'image'})
        else:
            data.append({'name': name, 'type': 'file'})
    return data
 

@app.route('/',methods=['GET', 'POST'])
def index():
    global def_url
    
    if request.method=='POST':
        if 'but2' in request.form:
            if platform.system().lower() == 'linux':
                http_server_process = subprocess.Popen(['python3', '-m', 'http.server'])
            else:
                http_server_process = subprocess.Popen(['python', '-m', 'http.server'])
            cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            cli.connect(("8.8.8.8",80))
            ip = cli.getsockname()[0]
            return render_template('index.html',ip=ip)
        
        if 'but1' in request.form:
            print(1)
            global ip_url
            ip_url = request.form["ip_url"]
            if ip_url!="" and ip_url is not None:
                data = display_data()
                print("hii",data)
                return render_template('listcont.html', data=data, url=def_url)
            
        
    return render_template("index.html")
    
@app.route('/display_data',methods=['GET', 'POST'])
def display_data():
    global def_url
    

    if 'call_count' not in session:
            session['call_count'] = 0


    if request.method == 'POST':
        
        if "url" in request.form:
            temp = def_url
            print("displ")
            dir = request.form["url"]
            def_url = temp + dir
            print("dir'==>", dir)
            print("def_url==>", def_url)

        else:
            print("hellolo")
            # def_url = "http://192.168.45.122:8000"
            def_url = ip_url+'/'

    if def_url:
        
        soup = scrape_data(def_url)
        if soup:
            data = extract_data(soup)
            if ip_url+'/' != def_url:
                
                return render_template('listcont.html', data=data, url=def_url)
            return data
        

    return "Failed to scrape data."



if __name__ == "__main__":
    app.run(port=5051,host="0.0.0.0",debug=True)
