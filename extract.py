"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.

Task 2a done by emanoeltadeu@gmail.com
"""
import csv
import json
import math

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    
    with open(neo_csv_path) as infile:
        reader = csv.DictReader(infile)
        for linha in reader:
            designation = linha["pdes"]
            diameter = float(linha["diameter"]) if linha["diameter"] else math.nan
            hazardous = linha["pha"] == "Y"
            name = linha["name"] or None
            
            # add a NearEarthObject object
            neos.append(NearEarthObject(designation, name, diameter, hazardous))

    return neos


def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path) as infile:
        js = json.load(infile)
        reader = [dict(zip(js["fields"], data)) for data in js["data"]]
        
        approaches = []
        for linha in reader:
            designation=linha["des"]
            time=linha["cd"]
            distance=float(linha["dist"])
            velocity=float(linha["v_rel"])
            
            # add a CloseApproach object
            approaches.append(CloseApproach(designation,time,distance,velocity))    
            
    return approaches
