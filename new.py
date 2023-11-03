
from flask import Flask,render_template,request,redirect,url_for,session,send_from_directory
import socket,subprocess
import platform
import requests
from bs4 import BeautifulSoup
import json,os
from werkzeug.utils import secure_filename

ip_url=""
def_url = ""
CUR_DIR = os.getcwd()+'/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  
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
            global ip_url
            ip_url = request.form["ip_url"]
            if ip_url!="" and ip_url is not None:
                print(ip_url)
                data = display_data()
                path = def_url.split("8000")
                return render_template('listcont1.html', data=data, url=def_url,cur_dir=path[1])
            
        
    return render_template("index.html")
    
@app.route('/display_data',methods=['GET', 'POST'])
def display_data():
    global def_url
    

    if 'call_count' not in session:
            session['call_count'] = 0


    if request.method == 'POST':
        
        
        if "home" in request.form:
            def_url = ip_url+'/'
            soup = scrape_data(def_url)
            if soup:
                data = extract_data(soup)
                path = def_url.split("8000")
                print(def_url,"defurllll")
                return render_template('listcont1.html', data=data, url=def_url,cur_dir=path[1])
            
        if "url" in request.form:
            temp = def_url
     
            dir = request.form["url"]
            def_url = temp + dir
        else:
            def_url = ip_url+'/'
      
            
    if def_url:
        
        soup = scrape_data(def_url)
        if soup:
            data = extract_data(soup)
            path = def_url.split("8000")
            if ip_url+'/' != def_url:
                
                return render_template('listcont1.html', data=data, url=def_url,cur_dir=path[1])
            return data
        

    return "Failed to scrape data."


@app.route('/upload',methods=["POST"])
def upload():
   if request.method == 'POST':
        
        # if "home" in request.form:
        #     def_url = ip_url+'/'
        #     if def_url:
        
        #         soup = scrape_data(def_url)
        #         if soup:
        #             data = extract_data(soup)
        #             path = def_url.split("8000")
                    
                        
        #             return render_template('listcont1.html', data=data, url=def_url,cur_dir=path[1])
                    

        uploaded_file = request.files['file']
        data = request.form["data"]
        data = data.replace("\'", "\"")
        data = json.loads(data)
        
        path = def_url.split("8000")
        SAVE_DIR = CUR_DIR+path[1]

        if uploaded_file.filename != "":
            data.append({'name':uploaded_file.filename,'type':'file'})
            filename = secure_filename(uploaded_file.filename)
            app.config["UPLOAD_FOLDER"] = SAVE_DIR
            uploaded_file.save(app.config["UPLOAD_FOLDER"]+filename)
        else:
            if "fold" in request.form:
                fname = request.form["foldername"]
                app.config["UPLOAD_FOLDER"] = SAVE_DIR+fname
                os.mkdir(app.config["UPLOAD_FOLDER"])
                data.append({'name':fname,'type':'folder'})
        return render_template('listcont1.html', data=data, url=def_url,cur_dir=CUR_DIR)
   return render_template('index.html')    

if __name__ == "__main__":
    app.run(port=5053,host="0.0.0.0",debug=True)
