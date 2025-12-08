import pandas

data = {
  "Usernames": ["admin", "Charles", "Upesh"],
  "Passwords": ["password", "Charl13", "May1991*"]
}

dataframe = pandas.DataFrame(data)

print(dataframe)

dataframe.to_csv("data.csv", index=False)