import basc_py4chan

class URL (basc_py4chan.URL):
    # see BASC-py4chan's `url.py` for an example of how to set up
    # the URLs.
    def __init__(self, https=False):
        # Your API URL Subdomains
        DOMAIN = { }

        # Your API URL Templates
        TEMPLATE = { }

        # Your API Listings
        LISTING = { }

        # combine all dictionaries into self.URL dictionary
        self.URL = TEMPLATE
        self.URL.update({'domain': DOMAIN})
        self.URL.update({'listing': LISTING})

class Board(basc_py4chan.Board):
    # add your own overrides here, or leave it alone
    pass

class Thread(basc_py4chan.Threads):
    # add your own overrides here, or leave it alone
    pass

class Post(basc_py4chan.Post):
    # add your own overrides here, or leave it alone
    pass

# note that all classes must be in one file (we recommend
#   py?chan/__init__.py ), due to how python modules work