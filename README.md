This is an AQI checker originally indented for Fort Erie.
The goal was to calulate AQI in a town, record date and time and list distance from fort erie.
Current functionality:
- Creates csv files with the results
- Will scrape aqi from anu accuweather.com link
- Will calculate distance from fort erie given the absolute location coordinates

Issues:
- doesn't support spaces in new town names (this is do to the code writing itself in a crude way)


Todo:
- Change Fort Erie to a base_town variable the user can set
- Allow for just the input of a link to create an entry
- Allow for link look up location instead of manual input (may require selenium)
- create a gui
- allow the removal of towns
- possibly rewrite with scrapy
- remove spaces from town add
