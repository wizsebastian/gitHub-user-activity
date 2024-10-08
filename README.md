# GitHub User Activity

![GitHub Activity CLI](https://img.shields.io/badge/CLI-GitHub%20Activity-brightgreen)

**GitHub User Activity** is a command-line tool (CLI) that allows you to fetch and display the latest GitHub events for a given user. This project is built with Python, utilizing the `requests` and `rich` libraries for fetching data and displaying it in a visually appealing format. inspired by the project idea from [roadmap.sh]("https://roadmap.sh/projects/github-user-activity").

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and use the `github-user-activity` CLI tool, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/yourusername/github-user-activity.git
cd github-user-activity
```

### Create and Activate Virtual Environment

```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install the CLI Tool

```bash
pip install .
```

## Usage

Once installed, you can fetch the latest GitHub events for any user by running the following command:

```bash
github-activity <username>
```

Replace `<username>` with the GitHub username you want to query.

### Example

```bash
github-activity octocat
```

This command will display the latest events for the GitHub user `octocat`.

## Features

- **Fetch Latest Events**: Retrieve the most recent events from any GitHub user.
- **Rich Formatting**: Beautiful output with styled text and tables using the `rich` library.
- **Event Types**: Support for different event types including issues, pull requests, pushes, and more.

## Project Structure

```plaintext
github-user-activity/
├── github_activity/
│   ├── __init__.py
│   └── main.py
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

- **`github_activity/`**: Contains the main Python module for the CLI tool.
- **`main.py`**: The core script that defines the CLI functionality.
- **`setup.py`**: Configuration for packaging and distribution.
- **`requirements.txt`**: Lists the dependencies needed for the project.
- **`README.md`**: Project documentation.