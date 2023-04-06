# Outage API Report Generator

This is a program designed to collect and send data using the KrakenFlex systems API. You can amend the API key, the base url, the site_id and the cut off date for outages in the [.env](.env) file.

I've utilised a [Makefile](Makefile) for this project, so setup should be a breeze 🥳

1. Ensure you're at the root of the project in your terminal
2. To set up the environment run `make setup`
3. For running tests use the command `make test`
4. To simply run the program it's `make run`
