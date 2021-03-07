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
params <- list('Sepal Length' = 6.9, 
               'Sepal Width' = 3.1, 
               'Petal Length' = 5.1, 
               'Petal Width' = 2.3)

# receiving response from API
response <- POST(url, body = params, encode = "json")

# formatting output as text
species_raw <- content(response, as = "text", encoding = "utf-8")

# output from JSON
jsonlite::fromJSON(species_raw)