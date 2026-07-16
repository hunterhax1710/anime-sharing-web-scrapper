# Anime-Sharing Web Scraper

Are you too lazy to always search if there is a new post for John-Doe-Movie? 
Too lazy to always check if someone finally uploaded the actual John-Doe-Movie on Anime-sharing Website? 
Or even better, you want to search for not ONLY John-Doe-Movie, but PeterPan-Sword-Movie and Lazy-Adam-Movie but you are too lazy to search one-by-one. Yea me too.

This is a simple desktop application for scraping search results from Anime-Sharing. The application lets you manage multiple search URLs, organize them into groups, and view newly scraped posts in a single interface. (Made for Lazy people)

## Features

* Able to organize URLs by custom groupings
* Scrape multiple URLs at once
* Scraped links are displayed in a table format (Website|Title) in POST TAB
* Able to add new url sites to scrape in the SITES TAB
* Open posts directly in your default web browser by clicking the title
* Background scraping to keep the interface responsive
* Configuration stored in a JSON file in DATA folder (This contains all your target URL links)

## Requirements

* beautifulsoup4
* PySide6
* requests

Install the dependencies with:

```bash
pip install -r requirements.txt
```

or

```bash
pip install PySide6 requests beautifulsoup4
```

## Project Structure

```
Anime-Sharing-Web-Scraper/
│
├── run.py
├── scraper.py
├── config.py
│
├── Data/
│   └── config.json
│
├── Pages/
│   ├── MainWindow.py
│   └── AddWindow.py
│
└── UI/
    ├── MainUI.py
    └── AddUI.py
```

## Running

Start the application from the project directory.

```bash
python run.py
```

## Configuration

The application stores all configured websites in:

```
Data/config.json
```

Each entry contains a group name and a search URL.

Example:

```json
{
    "1": {
        "group": "Website Alias Here",
        "url": "https://www.anime-sharing.com/search/103867405/?q=JOY+OF+PROGRAMMING+Software+Engineering+Simulator-TENOKE&o=relevance"
    }
}
```

## How It Works

When the application refreshes:

1. All configured URLs are loaded from `config.json`.
2. Each page is scraped for post titles and links.
3. Results are displayed in the Posts page.
4. Clicking a title opens the corresponding post in your browser.

## Notes

This project is intended for personal use. The scraper depends on the current HTML structure of Anime-Sharing. If the site's layout changes, the scraping logic in `scraper.py` may need to be updated.

# License

Made by Lazy People for Lazy People


