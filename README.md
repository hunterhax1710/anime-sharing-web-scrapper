# Anime-Sharing Web Scraper

A simple desktop application for scraping search results from Anime-Sharing. The application lets you manage multiple search URLs, organize them into groups, and view newly scraped posts in a single interface.

## Features

* Add and remove search URLs without editing code.
* Organize URLs by group.
* Scrape multiple search pages at once.
* View scraped posts grouped by their source.
* Open posts directly in your default web browser.
* Background scraping to keep the interface responsive.
* Configuration stored in a JSON file.

## Requirements

* Python 3.10 or newer
* PySide6
* requests
* beautifulsoup4

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
        "group": "anime-sharing",
        "url": "https://www.anime-sharing.com/search/101702893/?q=RJ01571551&o=relevance"
    }
}
```

## How It Works

When the application refreshes:

1. All configured URLs are loaded from `config.json`.
2. Each page is scraped for post titles and links.
3. Results are displayed in the Posts page.
4. Clicking a title opens the corresponding forum post in your browser.

## Notes

This project is intended for personal use. The scraper depends on the current HTML structure of Anime-Sharing. If the site's layout changes, the scraping logic in `scraper.py` may need to be updated.

## License

This project is released under the MIT License.


