import json

data = {
    "CURRENT ADDRESS": "12",
    "HIP": 13.0,
    "WEIGHT": 31.0,
    "शरीरिक संगठन(Body Frame)?": "jka",
    "शरीर संहनन(Body Bulk)?": "kwje",
    "शारीरिक संहनन (मांसपेशीय)Body Build (Musculature)?": "kjk",
    "माथे की लंबाई(Forehead Length)?": 2.0,
    "नाखून बनावट(Nails Texture)?": "a",
    "नाखुनो का रंग(Nails Colour)?": "a",
    "उंगली के नाखुन का आकार(Finger Nail Size)?": "a",
    "त्वचा की उपस्थिति(Skin Appearance)?": "a"
}

# Write to JSON file with UTF-8 encoding
with open('data1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
