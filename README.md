# FileHub : Remote Server File Manager

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)


[Project description: FileHub is a web-based application that allows users to interact with files and directories on a remote server through a user-friendly interface. This project is particularly useful in scenarios where users need to manage files and resources on a remote server, such as deploying and configuring web applications, sharing files, or simply accessing resources from a different location.]

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Contributing](#contributing)
  

## Features


1. **HTTP Server Start**: Start an HTTP server by clicking the "Create" button.
2. **Server IP Display**: Display the IP address of the HTTP server to which the user is connected.
3. **Connect to User-Defined URLs**: Allow users to input a custom URL and connect to the specified HTTP server.
4. **Browse Files and Directories**: Display files and directories from the connected HTTP server.
5. **Dynamic Directory Navigation**: Enable users to navigate through directories and view the contents.
6. **Interactive User Interface**: A user-friendly interface with buttons and links for controlling server connection and file navigation.
7. **Copy URL to Clipboard**: A "Copy" button that allows users to copy the server URL to their clipboard.
8. **Flexible URL Handling**: Handling user inputs and displaying appropriate content based on the URL entered or chosen.
9. **Error Handling**: Providing informative messages in case of connection errors or failures to scrape data.
10. **Responsive UI**: A responsive design that adapts to various screen sizes and devices. 


## Demo
### Landing Page:
![Landin Page](https://github.com/Mathii0402/FileHub/blob/main/demo%20/screenshot1.png)
Receiver should hit recieve button.
### Reciever:
![Receiver](https://github.com/Mathii0402/FileHub/blob/main/demo%20/screenshot2.png)
Receiver can copy the link and send it to the sender who is in the network
### Sender:
After sender hits the send button he will see a prompt to enter the link of the receiver
![Paste in the prompt](https://github.com/Mathii0402/FileHub/blob/main/demo%20/screenshot3.png)
After pasting he will connect to the receivers system.
### Transfer:
![Upload using upload button](https://github.com/Mathii0402/FileHub/blob/main/demo%20/screenshot4.png)


## Installation


- pip install -r requirements.txt
- python server.py


## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes, commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.
