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
r = requests.post(url, json={'Sepal Length': 5.1,
                             'Sepal Width': 3.5,
                             'Petal Length': 1.4,
                             'Petal Width': 0.2})

# formatting output
print(r.json())
