import pandas as pd
url = "https://es.wikipedia.org/wiki/Ochomil"
ochomil = pd.read_html(url, skiprows=1, header=0)[0]
print(ochomil.iloc[:, :4])
 