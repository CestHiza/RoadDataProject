# generate_metadata.py
from xml.etree.ElementTree import Element, SubElement, ElementTree, indent

# Create the root element
root = Element("metadata")

# Add main elements as specified
identificationInfo = SubElement(root, "idinfo")
title = SubElement(identificationInfo, "citation")
citeinfo = SubElement(title, "citeinfo")
origin = SubElement(citeinfo, "origin").text = "Hiza Mvuendy (Synthetic Data Generator)"
pubdate = SubElement(citeinfo, "pubdate").text = "20240522" # Example: YYYYMMDD
resTitle = SubElement(citeinfo, "title").text = "Road Network Dataset" # Changed from 'title' to 'resTitle' for FGDC-like structure

descript = SubElement(identificationInfo, "descript")
abstract = SubElement(descript, "abstract").text = "Synthetic road data for infrastructure analysis, including road ID, name, length, condition, and WKT geometry."
purpose = SubElement(descript, "purpose").text = "To provide a sample dataset for testing GIS and database workflows."

status = SubElement(identificationInfo, "status")
progress = SubElement(status, "progress").text = "Complete"
update = SubElement(status, "update").text = "As needed" # Maintenance and update frequency

# Spatial Data Organization Information
spdoinfo = SubElement(root, "spdoinfo")
direct = SubElement(spdoinfo, "direct").text = "Vector"
ptvctinf = SubElement(spdoinfo, "ptvctinf")
sdtsterm = SubElement(ptvctinf, "sdtsterm")
sdtstype = SubElement(sdtsterm, "sdtstype").text = "String" # For WKT geometry
ptvctcnt = SubElement(sdtsterm, "ptvctcnt").text = "100" # Number of road segments

# Distribution Information
distinfo = SubElement(root, "distinfo")
distrib = SubElement(distinfo, "distrib")
cntinfo_dist = SubElement(distrib, "cntinfo") # Contact info for distributor
cntperp_dist = SubElement(cntinfo_dist, "cntperp")
cntper_dist = SubElement(cntperp_dist, "cntper").text = "Hiza Mvuendy"
cntorg_dist = SubElement(cntperp_dist, "cntorg").text = "Personal Project"
cntpos_dist = SubElement(cntinfo_dist, "cntpos").text = "Data Creator"
cntaddr_dist = SubElement(cntinfo_dist, "cntaddr")
addrtype_dist = SubElement(cntaddr_dist, "addrtype").text = "mailing and physical address"
address_dist = SubElement(cntaddr_dist, "address").text = "N/A"
city_dist = SubElement(cntaddr_dist, "city").text = "N/A"
state_dist = SubElement(cntaddr_dist, "state").text = "N/A"
postal_dist = SubElement(cntaddr_dist, "postal").text = "N/A"
country_dist = SubElement(cntaddr_dist, "country").text = "N/A"
cntvoice_dist = SubElement(cntinfo_dist, "cntvoice").text = "N/A"

distliab = SubElement(distinfo, "distliab").text = "Although these data have been processed successfully on a computer system, no warranty expressed or implied is made by the originator regarding the utility of the data on any other system, nor shall the act of distribution constitute any such warranty. The originator is not responsible for any errors or omissions in the data."
stdorder = SubElement(distinfo, "stdorder")
digform = SubElement(stdorder, "digform")
digtinfo = SubElement(digform, "digtinfo")
formname = SubElement(digtinfo, "formname").text = "CSV, SQL Server Table"
digtopt = SubElement(digform, "digtopt")
onlinopt = SubElement(digtopt, "onlinopt")
computer = SubElement(onlinopt, "computer")
networka = SubElement(computer, "networka")
networkr = SubElement(networka, "networkr").text = "roads.csv, SQL Database" # Location of data

# Metadata Reference Information
metainfo = SubElement(root, "metainfo")
metd = SubElement(metainfo, "metd").text = "20240522" # Metadata date
metc = SubElement(metainfo, "metc") # Metadata contact
cntinfo_meta = SubElement(metc, "cntinfo")
cntperp_meta = SubElement(cntinfo_meta, "cntperp")
cntper_meta = SubElement(cntperp_meta, "cntper").text = "Hiza Mvuendy"
cntorg_meta = SubElement(cntperp_meta, "cntorg").text = "Personal Project"
cntpos_meta = SubElement(cntinfo_meta, "cntpos").text = "Metadata Creator"
# ... (add more contact details for metadata if needed, similar to distributor)

metstdn = SubElement(metainfo, "metstdn").text = "FGDC Content Standard for Digital Geospatial Metadata"
metstdv = SubElement(metainfo, "metstdv").text = "FGDC-STD-001-1998"

# Create an ElementTree object
tree = ElementTree(root)

# Pretty print the XML
indent(tree, space="\t", level=0)

# Write to an XML file with XML declaration
try:
    with open("roads_metadata.xml", "wb") as f: # Write in binary mode for encoding
        tree.write(f, encoding="utf-8", xml_declaration=True)
    print("roads_metadata.xml generated successfully.")
    print("This is a more structured XML, but full FGDC compliance is extensive.")
except Exception as e:
    print(f"Error writing XML file: {e}")