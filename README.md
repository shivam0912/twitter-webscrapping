  #                                                                       Web Scrapping of Twitter Trending using Selenium

## Project Overview
A web application that scrapes and displays the top 5 trending topics on Twitter using Selenium, Flask, and MongoDB.

## Features
- Automated Twitter login
- Web scraping of trending topics
- Proxy-based IP rotation
- MongoDB data storage
- Simple web interface to trigger scraping
## Trending data stores in MongoDB 

![Screenshot 2025-01-01 230417](https://raw.githubusercontent.com/shivam0912/twitter-webscrapping/refs/heads/master/images/db-ss.png)


## Trending data renders on UI

![Screenshot 2025-01-01 223002](https://raw.githubusercontent.com/shivam0912/twitter-webscrapping/refs/heads/master/images/local-run.png)





## Prerequisites
- Python 3.8+
- Chrome WebDriver
- ProxyMesh account
- MongoDB

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/twitter-webscrapping.git
cd twitter-webscrapping
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate 
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
- Update `config.py` with:
  - Twitter credentials
  - MongoDB URI
  - ProxyMesh API details

## Running the Application
```bash
python run.py
```

## Environment Setup
- Create `.env` file for sensitive configurations
- Install Chrome WebDriver compatible with your Chrome version

## Project Structure
- `config/`: Configuration files
- `src/`: Source code (scraper, routes)
- `templates/`: HTML templates
- `run.py`: Application entry point

## Key Dependencies
- Flask
- Selenium
- PyMongo
- ProxyMesh

## Troubleshooting
- Ensure Chrome WebDriver matches Chrome version
- Check network and proxy configurations
- Verify MongoDB connection

## Limitations
- Requires active Twitter login
- Dependent on Twitter's HTML structure
