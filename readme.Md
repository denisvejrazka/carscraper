# Web Scraping and Analysis of Sports Cars

This project scrapes data about sports cars from the website sportovnivozy.cz using a Python script, then analyzes the data using R in HTML format.

## Project Setup

### Requirements:
- Python 3.x
- R (with necessary packages)
- Ansible (for deployment automation)

### Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/denisvejrazka/carscraper.git
    ```

2. Set up the environment with Ansible:

    - Install dependencies (Python, R, etc.):

      ```bash
      ansible-playbook playbook.yml
      ```

3. Run the project:

    1. The Python script `scrap_all_cars.py` will be executed automatically by Ansible. This script scrapes data from the website.
    2. After scraping, the report in `report.Rmd` is rendered using the R Markdown package.

    The report will be saved as an HTML file, which you can view in your browser.

### Docker Setup (Optional)

You can also use Docker for an isolated environment.

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Start the scraping and analysis process:

    ```bash
    docker-compose up
    ```

### Output

- A `.csv` file containing the scraped car data.
- An HTML file containing the analysis report.