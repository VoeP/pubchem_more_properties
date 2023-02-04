# pubchem_more_properties


I wanted to make this code available to save some other poor sould from some additional google searches. However, after checking if someone else on github had made something similar, I realized that this idea has already been done many times by people smarter than me, which is unsurprising considering how limited the list of properties you can query with PubChemPy are. If you want a more comprehensive version, go check out this repository: https://github.com/mawansui/pubchemprops. 

However, I am still putting this on github, becuse my version is quite easy to understand for beginners and easy for a user to add their own string formatting to if they wish to edit the information retireved from PubChem. What makes it more easy to understand? The reason I say that is because in my version I check which entry is contained in the headings of the xml version of the PubChem webpage. Making this a series of if statements should allow a user to go and add the formatting they want for entries they are dissatisfied with. My version also outputs everything as a pandas table.

A major downside of my version is that it only takes CID:s as input.However, the more popular library, PubChemPy, allows conversion of common names to CID. If you are warking with CAS numbers in python, I recommend that you use cirpy to first transform them into SMILES and then PubChemPy to transform those to CIDs. That's in my opinion more reliable than querying with CAS as the name parameter for PubChemPy to get the CID. You can do this as follows:




'''
list_cas=whatever

cid_based_on_cas=[]

for cas in list_cas:

        smiles=cirpy.resolve(cas, "smiles")
        
        cid=(pubchempy.get_compounds(smiles, namespace='smiles'))
        
        print(cid[0].cid)
        
        cid_based_on_cas.append(cid[0].cid)
 '''       


or if you have a ton of common names that you want to convert to cid:

'''
dic_name_cid={}

for name in name_list:

  while True:
  
   try:
   
    print(name)
    
    cid=(pubchempy.get_compounds(name, namespace='name'))
    
    try:
    
        if len(cid)>1:
        
            cid=cid[0]
            
            dic_name_cid[name]=cid[0].cid
            
        elif len(cid)==1:
        
            dic_name_cid[name]=cid[0].cid
            
    except (AttributeError, TypeError) as e:
    
        dic_name_cid[name]=cid.cid
        
    break
    
   except:
   
       pass
'''
