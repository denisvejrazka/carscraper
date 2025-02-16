# Web Scraping and Analysis of Sports Cars

This project scrapes data about sports cars from the website sportovnivozy.cz using a Python script, then analyzes the data using R in HTML format.

## Project Setup

### Requirements:
- Python 3.x
- R (with necessary packages)
- Docker (for containerized deployment) or Ansible (for automated setup)

### Getting Started

You can set up and run the project in three different ways: using Docker, Ansible, or manually installing dependencies.

#### 1. Using Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/denisvejrazka/carscraper.git
    cd carscraper
    ```

2. Build the Docker image:

    ```bash
    docker-compose build
    ```

3. Start the scraping and analysis process:

    ```bash
    docker-compose up
    ```

#### 2. Using Ansible

1. Clone the repository:

    ```bash
    git clone https://github.com/denisvejrazka/carscraper.git
    cd carscraper
    ```

2. Install dependencies using Ansible:

    ```bash
    ansible-playbook playbook.yml
    ```

3. Run the project:
    - The Python script `scrap_all_cars.py` will be executed automatically by Ansible. This script scrapes data from the website.
    - After scraping, the report in `report.Rmd` is rendered using the R Markdown package.
    
    The report will be saved as an HTML file, which you can view in your browser.

#### 3. Manual Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/denisvejrazka/carscraper.git
    cd carscraper
    ```

2. Install dependencies manually:

    - Install Python packages:
      ```bash
      pip install -r requirements.txt
      ```
    
    - Install required R packages in R:
      ```r
      install.packages(c("rmarkdown", "ggplot2", "dplyr"))
      ```

3. Run the scraping script:
    ```bash
    python scrap_all_cars.py
    ```

4. Generate the report in R:
    ```r
    rmarkdown::render("report.Rmd")
    ```

### Output

- A `.csv` file containing the scraped car data.
- An HTML file containing the analysis report.