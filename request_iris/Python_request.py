# =============================================================================
# Import Packages
# =============================================================================

import requests

# =============================================================================
# Calling API
# =============================================================================

# results base URL
url = 'http://localhost:5000/results'

# setting params according to index.html
# recieving response from API
r = requests.post(url, json={'Sepal Length': 1.6,
                             'Sepal Width': 1.9,
                             'Petal Length': 3.0,
                             'Petal Width': 0.2})

# formatting output
print(r.json())
