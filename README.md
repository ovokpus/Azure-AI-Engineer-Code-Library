# Azure-AI-Engineer-Code-Library

Fully implemented Python code solutions covering the Azure AI Engineer Knowledge Base

---

<div>
 <img src="https://github.com/ovokpus/Azure-AI-Engineer-Code-Library/blob/main/assets/readmeimg.png">
</div>

---

## Setup

---

# Lab Environment Setup

These exercises were completed them on my local computer. You can do so by installing the following software. You may experience unexpected dialogs and behavior when using your own environment. Due to the wide range of possible local configurations, the course team cannot support issues you may encounter in your own environment.

> **Note**: The instructions below are for a Windows 10 computer. You can also use Linux or MacOS. You may need to adapt the lab instructions for your chosen OS.

---

## Provision a Cognitive Services resource

Azure Cognitive Services are cloud-based services that encapsulate artificial intelligence capabilities you can incorporate into your applications. You can provision individual cognitive services resources for specific APIs (for example, **Text Analytics** or **Computer Vision**), or you can provision a general **Cognitive Services** resource that provides access to multiple cognitive services APIs through a single endpoint and key. In this case, you'll use a single **Cognitive Services** resource.

1. Open the Azure portal at `https://portal.azure.com`, and sign in using the Microsoft account associated with your Azure subscription.
2. Select the **&#65291;Create a resource** button, search for *cognitive services*, and create a **Cognitive Services** resource with the following settings:
    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Choose or create a resource group (if you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided)*
    - **Region**: *Choose any available region*
    - **Name**: *Enter a unique name*
    - **Pricing tier**: Standard S0
3. Select the required checkboxes and create the resource.
4. Wait for deployment to complete, and then view the deployment details.
5. Go to the resource and view its **Keys and Endpoint** page. This page contains the information that you will need to connect to your resource and use it from applications you develop. Specifically:
    - An HTTP *endpoint* to which client applications can send requests.
    - Two *keys* that can be used for authentication (client applications can use either key to authenticate).
    - The *location* where the resource is hosted. This is required for requests to some (but not all) APIs.

---

## Use the Azure AI Python SDK

You can write code that consumes cognitive services REST APIs directly, but there are software development kits (SDKs) for many popular programming languages. My focus here is on Python. Using the SDK can greatly simplify development of applications that consume cognitive services.

Configuration settings: After obtaining the key and endpoint, or other applicable environment variables from Azure, store them in a `.env` file right beside the Python module

    - **Python**: .env

Open the configuration file and update the configuration values it contains to reflect the **endpoint** and an authentication **key** for your cognitive services resource. Save your changes.

The `.env` files do not appear on the repository, as it is best practice to not expose credentials publicly. Those files are added to `.gitignore`, to precent github from tracking any changes to those files.

---
### Base Operating System (Windows 10)

#### Windows 10

Install Windows 10 and apply all updates.

---

### Browser (Edge or Chrome)

Either browser works fine for this solution implementation

---

### Python (and required packages)

1. Download version 3.8 from <https://docs.conda.io/en/latest/miniconda.html>
2. Run setup to install - **Important**: Select the options to add Miniconda to the PATH variable and to register Miniconda as the default Python environment.
3. After installation, open the Anaconda prompt and enter the following commands to install packages:

```bash
pip install flask requests python-dotenv pylint matplotlib pillow
pip install --upgrade numpy
```

---

### Azure CLI

1. Download from <https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest>
2. Install using the default options

---

### Git

1. Download and install from <https://git-scm.com/download.html>, using the default options

---

### Visual Studio Code (and extensions)

1. Download from <https://code.visualstudio.com/Download>
2. Install using the default options
3. After installation, start Visual Studio Code and on the **Extensions** tab (CTRL+SHIFT+X), search for and install the following extensions from Microsoft:
    - Python
    - Azure Functions
    - PowerShell

---

### Bot Framework Emulator

Follow the instructions at <https://github.com/Microsoft/BotFramework-Emulator/blob/master/README.md> to download and install the latest stable version of the Bot Framework Emulator for your operating system.

---

### Bot Framework Composer

Install from <https://docs.microsoft.com/en-us/composer/install-composer>.

---
