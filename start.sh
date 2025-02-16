#!/bin/bash

# Spustí Python skript
python3 scrap_all_cars.py

# Spustí analýzu v R
Rscript -e "rmarkdown::render('report.Rmd')"