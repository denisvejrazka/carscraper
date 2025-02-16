FROM rocker/r-ver:4.4.1

RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev \
    git \
    curl \
    libsqlite3-dev \
    pandoc \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN ln -s /usr/bin/python3 /usr/bin/python

RUN R -e "install.packages(c('psych', 'ggplot2', 'lmtest', 'knitr', 'rmarkdown'))"

RUN pip3 install beautifulsoup4 requests

WORKDIR /app

COPY . /app

EXPOSE 8787

RUN chmod +x start.sh

CMD ["./start.sh"]