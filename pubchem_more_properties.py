

import urllib.request
import pandas as pd
import json
import numpy as np
import re



def pubsearch(CID: int) -> pd.DataFrame:
    result_table=pd.DataFrame(columns=["CID", "Exact Mass",	"Density",  "Decomposition", "Chemical Classes", "XLogP", "Molecular Weight",	
                                "Log Kow", "Boiling Point",
                                   "Vapor Pressure",	"Solubility",
                                   "Stability", "Topological Polar Surface Area", "Complexity",
                                   "Hydrogen Bond Donor Count",
                                   "Hydrogen Bond Donor Count",
                                   "pH", "Formal Charge", "Rotatable Bond Count",                                   
                                   "Monoisotopic Mass",
                                   "Heavy Atom Count",                                       
                                   "Isotope Atom Count",                                       
                                   "Defined Atom Stereocenter Count",                                       
                                   "Undefined Atom Stereocenter Count",                                       
                                   "Defined Bond Stereocenter Count",                                       
                                   "Covalently-Bonded Unit Count","Undefined Bond Stereocenter Count"])
    
    
    
    query_string= "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{0}/JSON/?response_type=save&response_basename=compound_CID_{0}"

    filename=urllib.request.urlopen(query_string.format(CID))

    
    ##get response from server, then decode, then encode into utf 8  again while discarding all non utf8 characters
    #from the resulting string. json.loads only accepts utf encoded characters. json.loads() takes a string and transforms it into a dictionary
    
    file_response = filename.read()
    encoding = filename.headers.get_content_charset('latin')
    decoded_file = file_response.decode(encoding)
    decoded_file.encode('utf-8', errors='ignore').decode('utf-8')
    data1=json.loads(decoded_file)

    result_table["CID"] = [CID]

    location_all_props= data1["Record"]["Section"]
    experimental_props="foo"
    for i in location_all_props:
        if i["TOCHeading"]=="Chemical and Physical Properties":
            base_physicochem=i["Section"]

    if isinstance(base_physicochem, list):

        for i in range(len(base_physicochem)):
            if base_physicochem[i]["TOCHeading"]=="Computed Properties":
                computed_props= base_physicochem[i]
            if base_physicochem[i]["TOCHeading"]=="Experimental Properties":
                experimental_props= base_physicochem[i]

    if isinstance(computed_props, dict):
        computed_props=computed_props["Section"]
    if experimental_props != "foo":
        if isinstance(experimental_props, dict):
            experimental_props=experimental_props["Section"]
    #try:
    #    computed_props=data1["Record"]["Section"][3]["Section"][0]["Section"]
    #except:
    #    print("aa")
    #    computed_props=data1["Record"]["Section"][2]["Section"]["Section"]
    #    if isinstance(computed_props, list):
    #        computed_props=computed_props[0]
    #        if "Section" in computed_props.keys():
    #            computed_props=computed_props["Section"]
    #            print(computed_props)
    #print(computed_props)
    for i in computed_props:
        TOCHeading = i["TOCHeading"]
        entry=i["Information"][0]["Value"]

        if "Exact Mass" in TOCHeading:
            result_table["Exact Mass"] = entry["StringWithMarkup"][0]["String"]
            
        
        if "XLogP3"in TOCHeading:
            entry=entry["Number"]
            result_table["XLogP"] = entry
        
        if "Molecular Weight"in TOCHeading:
            entry=entry["StringWithMarkup"][0]["String"]
            result_table["Molecular Weight"] = entry

        
        if "LogP"in TOCHeading:
            result_table["Log Kow"] = entry
                    
            
        if "Vapor Pressure"in TOCHeading:
            result_table["Vapor Pressure"] = entry

        
        if "Stability"in TOCHeading:
            result_table["Stability"] = entry["Number"]

        
        if "Hydrogen Bond Donor Count"in TOCHeading:
            result_table["Hydrogen Bond Donor Count"] = entry["Number"]

            
        if "Hydrogen Bond Donor Count"in TOCHeading:
            result_table["Hydrogen Bond Donor Count"] = entry["Number"]

        
        if "Complexity"in TOCHeading:
            result_table["Complexity"] = entry["Number"]

        
        if "Solubility"in TOCHeading:
            result_table["Solubility"] = entry


        if "Density"in TOCHeading:
            result_table["Density"] = entry["StringWithMarkup"][0]["String"]

            
        if "Decomposition"in TOCHeading:
            result_table["Decomposition"] = entry["StringWithMarkup"][0]["String"]

        
        if "Topological Polar Surface Area"in TOCHeading:
            entry=entry["Number"]
            result_table["Topological Polar Surface Area"] = entry

        
        if "Boiling Point" in TOCHeading:
            result_table["Boiling Point"] = entry

            
        if "Chemical Classes" in TOCHeading:
            result_table["Chemical Classes"] = entry["StringWithMarkup"][0]["String"]        

        
        if "Rotatable Bond Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Rotatable Bond Count"] = entry

            
        if "Monoisotopic Mass"in TOCHeading:
            entry=entry["StringWithMarkup"][0]
            result_table["Monoisotopic Mass"] = entry

            
        if "Heavy Atom Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Heavy Atom Count"] = entry

            
        if "Isotope Atom Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Isotope Atom Count"] = entry

            
        if "Defined Atom Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Defined Atom Stereocenter Count"] = entry

            
        if "Undefined Atom Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Undefined Atom Stereocenter Count"] = entry

            
        if "Defined Bond Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Defined Bond Stereocenter Count"] = entry

            
        if "Covalently-Bonded Unit Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Covalently-Bonded Unit Count"] = entry

            
        if "Undefined Bond Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Undefined Bond Stereocenter Count"] = entry

        
        if "pH"in TOCHeading:
            entry=str(entry["StringWithMarkup"][0]["String"])

            result_table["pH"] = entry

            
        if "Formal Charge"in TOCHeading:
            entry=str(entry["Number"])

            result_table["Formal Charge"] = entry



    if experimental_props != "foo":
      for i in experimental_props:
        TOCHeading = i["TOCHeading"]
        entry=i["Information"][0]["Value"]


        if "Exact Mass" in TOCHeading:
            result_table["Exact Mass"] = entry["StringWithMarkup"][0]["String"]
            
        
        if "XLogP3"in TOCHeading:
            entry=entry["Number"]
            result_table["XLogP"] = entry
        
        if "Molecular Weight"in TOCHeading:
            entry=entry["StringWithMarkup"][0]["String"]
            result_table["Molecular Weight"] = entry

        
        if "LogP"in TOCHeading:
            try:
                entry=str(entry["StringWithMarkup"][0]["String"])

            except KeyError:
                entry=entry["Number"]
            result_table["Log Kow"] = entry

        

        if "pH"in TOCHeading:
            entry=str(entry["StringWithMarkup"][0]["String"])
            result_table["pH"] = entry
            
        
        if "Formal Charge"in TOCHeading:
            entry=str(entry["Number"])

            result_table["Formal Charge"] = entry

            
        if "Vapor Pressure"in TOCHeading:
            entry = entry["StringWithMarkup"][0]["String"]
            result_table["Vapor Pressure"] = entry

        
        if "Stability"in TOCHeading:
            result_table["Stability"] = entry["StringWithMarkup"][0]["String"]

        
        if "Solubility"in TOCHeading:
            result_table["Solubility"] = entry["StringWithMarkup"][0]["String"]

        
        if "Topological Polar Surface Area"in TOCHeading:
            entry=entry["Number"]
            result_table["Topological Polar Surface Area"] = entry

        
        if "Rotatable Bond Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Rotatable Bond Count"] = entry

            
        if "Monoisotopic Mass"in TOCHeading:
            entry=entry["StringWithMarkup"][0]
            result_table["Monoisotopic Mass"] = entry

            
        if "Heavy Atom Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Heavy Atom Count"] = entry

            
        if "Isotope Atom Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Isotope Atom Count"] = entry

            
        if "Defined Atom Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Defined Atom Stereocenter Count"] = entry

            
        if "Undefined Atom Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Undefined Atom Stereocenter Count"] = entry

            
        if "Defined Bond Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Defined Bond Stereocenter Count"] = entry

            
        if "Covalently-Bonded Unit Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Covalently-Bonded Unit Count"] = entry

            
        if "Undefined Bond Stereocenter Count"in TOCHeading:
            entry=entry["Number"]
            result_table["Undefined Bond Stereocenter Count"] = entry

                
        if "Boiling Point" in TOCHeading:
            entry = entry["StringWithMarkup"][0]["String"]
            result_table["Boiling Point"] = entry

            
        if "Chemical Classes" in TOCHeading:
            result_table["Chemical Classes"] = entry["StringWithMarkup"][0]["String"]   
            
        if "Density"in TOCHeading:
            result_table["Density"] = entry["StringWithMarkup"][0]["String"]
            
        if "Decomposition"in TOCHeading:
            result_table["Decomposition"] = entry["StringWithMarkup"][0]["String"]

    return(result_table)


def cid_list_search(list_CID):

    table_full=pd.DataFrame(columns=["CID", "Exact Mass",	"XLogP", "Molecular Weight",	"Log Kow", "Boiling Point",
                                   "Vapor Pressure",	"Solubility",
                                   "Stability", "Topological Polar Surface Area"])
    table_full=pubsearch(list_CID[0])
    for i in np.arange(1, len(list_CID)):
      print(list_CID[i])
      try:
        
        interim_table=pubsearch(list_CID[i])

        table_full=pd.concat([table_full, interim_table])
      except:
        print(i)
      
        
    return(table_full)
        
