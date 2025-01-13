customers = {
  "Name": "Elfan",
  "Age": 30,
  "Address": "Tasik"
}

name = customers['Name'] # get value

customers["Company"] = "PT. Vanzdev Cipta Teknologi" # add data
customers["Name"] = "Saputra" # Edit data
del customers["Address"] # hapus data

for key, value in customers.items():
  print(f"{key}: {value}")

# print (customers.items(
