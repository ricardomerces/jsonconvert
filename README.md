# Json Convert
Convert CSV file to JSON file  

## Installation  
  

    git clone https://github.com/ricardomerces/jsonconvert.git
    
    cd jsonconvert
    
    python3 setup.py install

  
## Prerequisite  
  
CSV file name = **file.csv** (in the same directory)
  
## Usage example  
  
**CODE EXAMPLE**  
  
    from jsonconvert import jsonconvert
      
    jsonconvert.convert("host", "core", "memory", "storage") 

    
**CSV file contents:**
  
terminal01,dual core,4GB,2TB  
terminal02,quad core,8GB,4TB  
terminal03,quad core,16GB,4TB  

  
**Output file.json - VALID JSON (RFC 4627)**
 
[
    {
        "host": "terminal01",
        "core": "dual core",
        "memory": "4GB",
        "storage": "2TB"
    },
    {
        "host": "terminal02",
        "core": "quad core",
        "memory": "8GB",
        "storage": "4TB"
    },
    {
        "host": "terminal03",
        "core": "quad core",
        "memory": "16GB",
        "storage": "4TB"
    }
]
