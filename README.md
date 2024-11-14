# Hyperledger Fabric Django Project

This project is a Django web application that enables users to upload a document, convert it to JSON format, and store it on a Hyperledger Fabric blockchain network.

## Prerequisites

1. **Python 3.6+** (Install from [python.org](https://www.python.org/downloads/))
2. **Django** (Install via pip)
3. **Hyperledger Fabric Network** (Set up following the [Hyperledger Fabric documentation](https://hyperledger-fabric.readthedocs.io/))
4. **Docker** (Required for running Hyperledger Fabric network)

## Project Setup

### 1. Clone the Repository

Clone this repository to your local machine:
```git clone git@github.com:victorgearhead/HyperLedger-Fabric---Data-Fabrication.git```

## Install Django and Dependencies

To install Django and any additional dependencies for the project, follow these steps:

**Install Django**: Use `pip` to install Django.
   ```pip install django```

# Start the Hyperledger Fabric Network

To start the Hyperledger Fabric network for this project, follow these steps:

## Prerequisites

Make sure you have:
- Installed **Docker** (required to run Hyperledger Fabric).
- Set up the **Hyperledger Fabric** environment (refer to the [Hyperledger Fabric documentation](https://hyperledger-fabric.readthedocs.io/)).

## Steps to Start the Network

1. **Navigate to the Fabric Samples Directory**

   If you followed the standard installation, navigate to the `test-network` directory:
   ```cd fabric-samples/test-network```

2. **Start the Fabric Network and Create a Channel**

   Run the following command to start the network, create a channel (e.g., mychannel), and use Certificate Authorities:
   ```./network.sh up createChannel -c mychannel -ca```

3. **Deploy the Chaincode**

   To deploy a specific chaincode on your channel, use the following command:
   ```./network.sh deployCC -ccn docChaincode -ccp ../chaincode/docChaincode -ccl go```

## Set Up Django Project

1. **Navigate to the project directory**
   ```cd yourproject```

2. **Run Django migrations to initialize the database:**

   ```python manage.py migrate```

## Run the Django Server

1. **To start the Django development server:**
   ```python manage.py runserver```
The server will run at http://127.0.0.1:8000/ by default.

## Upload a Document

1. Open the Django application in your web browser by navigating to http://127.0.0.1:8000/.
2. You will be prompted to upload a document.
3. Upon uploading, the document will be converted to JSON format.
4. The JSON data will then be uploaded to the Hyperledger Fabric network.
