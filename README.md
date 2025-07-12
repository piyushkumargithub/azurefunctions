# ⚡ Azure Functions with Python (v2)

This repository contains Azure Functions implemented using Python module v2. It's designed to be run locally with full simulation of Azure resources using tools like Azurite and Azure Storage Explorer.

## 🛠 Prerequisites

### 1. Install Azure Core Tools
To run Azure Functions locally, [install Azure Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local).

> **Note:** A system restart may be required after installation on Windows.

### 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv virtualenv_name
virtualenv_name\Scripts\activate
```

Once activated, the environment name will appear on the left side of your command prompt.

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

## 🚀 Running the Function App

Start the app locally using:

```bash
func start
```

Once running, you can hit the respective endpoints to test your functions.

## 🧪 Simulating Azure Storage

Use **Azurite** to simulate Azure Storage accounts locally.

- [Install Azurite](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite)
- Or simply:

```bash
npm install -g azurite
azurite
```

## 🗂 Accessing Storage Locally

Download [Azure Storage Explorer](https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer) to interact with your storage accounts locally.

## 🔧 Configuration

Create a `local.settings.json` file in the root of your Function directory with the following content:

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true"
  }
}
```

---
