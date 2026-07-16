import json

CONFIG_FILE = "DATA/config.json"

# Loads config.json
def load_sites():
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Override config.json by taking in a whole new set of config.json dictionary
def save_sites(sites):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(sites, file, indent=4)


# Adding a new site
def add_site(group, url):
    sites = load_sites()

    if sites:
        # Gets all the id/key, then find the max id + 1
        new_id = str(max(int(id) for id in sites.keys()) + 1)
    else:
        new_id = "1"

    sites[new_id] = {
        "group": group,
        "url": url
    }
    save_sites(sites)


# Removing a site by id/key
def remove_site(site_id):
    sites = load_sites()
    del sites[str(site_id)]
    save_sites(sites)







