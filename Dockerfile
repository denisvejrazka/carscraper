# Use a base image with R
FROM rocker/r-ver:4.4.1

# Install dependencies for R
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev \
    git \
    curl \
    libsqlite3-dev \
    pandoc \
    && rm -rf /var/lib/apt/lists/*

# Install Python and necessary libraries
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic link for python3 to python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install R packages for the analysis
RUN R -e "install.packages(c('psych', 'ggplot2', 'lmtest', 'knitr', 'rmarkdown'))"

# Install Python dependencies
RUN pip3 install beautifulsoup4 requests

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Expose the port for Jupyter (optional)
EXPOSE 8787

# Make the start.sh script executable
RUN chmod +x start.sh

# Default command to run when the container starts
CMD ["./start.sh"]