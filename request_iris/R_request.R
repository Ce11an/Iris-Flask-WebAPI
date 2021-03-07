# =============================================================================
# Import Packages
# =============================================================================

library(httr)

# =============================================================================
# Calling API
# =============================================================================

# results base URL
url <- "http://127.0.0.1:5000/results"

# setting params according to index.html
params <- list('Sepal Length' = 1.6, 
               'Sepal Width' = 3.0, 
               'Petal Length' = 1.9, 
               'Petal Width' = 0.2)

# receiving response from API
response <- POST(url, body = params, encode = "json")

# formatting output as text
species_raw <- content(response, as = "text", encoding = "utf-8")

# output from JSON
jsonlite::fromJSON(species_raw)