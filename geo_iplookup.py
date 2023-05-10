import requests
import os
import rich
from rich import print
from rich.console import Console
from rich.table import Table

def hackertarget_lookup():
    ip = input("[DOse]ip lookup: ").strip()
    url = 'https://json.geoiplookup.io/'+ip
    data = requests.get(url)

    table = Table(title="[italic magenta1]IP info👾[/italic magenta1]")
    table.add_column("IP INFO "+ip, justify="left", style="magenta")
    table.add_column("IP DATA", justify="left", style="magenta")

    ip = data.json()['ip']
    isp = data.json()['isp']
    org = data.json()['org']
    host = data.json()['hostname']
    city = data.json()['city']
    country = data.json()['country_code']
    cont = data.json()['continent_code']
    cont_name = data.json()['continent_name']
    region = data.json()['region']
    dis = data.json()['district']
    time = data.json()['timezone_name']
    con_type = data.json()['connection_type']
    asn_org = data.json()['asn_org']
    asn = data.json()['asn']
    cash_type = data.json()['currency_code']
    cash_name = data.json()['currency_name']

    table.add_row(ip, "IP ADDRESS")
    table.add_row(isp, "INTERNET SERVICE PROVIDER")
    table.add_row(org, "ORGANIZATION")
    table.add_row(host, "DNS")
    table.add_row(city, "CITY")
    table.add_row(country, "COUNTRY CODE")
    table.add_row(cont_name, "CONTINENT NAME")
    table.add_row(cont, "CONTINENT CODE")
    table.add_row(region, "REGION")
    table.add_row(dis, "DISTRICT")
    table.add_row(time, "TIME ZONE")
    table.add_row(con_type, "CONNECTION TYPE")
    table.add_row(asn_org, "ASN ORGANIZATION")
    table.add_row(asn, "ASN")
    table.add_row(cash_type, "CURRENCY CODE")
    table.add_row(cash_name, "CURRENCY NAME")
    console = Console()
    console.print(table)
