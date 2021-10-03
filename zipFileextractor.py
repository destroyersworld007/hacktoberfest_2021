from zipfile import ZipFile


zip_file = "93531.zip"
password = "93531"

with ZipFile(zip_file,"r") as zf:
  p = zf.extractall(pwd=bytes(password,'utf-8'))
  archive = zf.infolist()
  read_me_file = archive[-1]
  zip_file = read_me_file.filename
  password = zip_file.split('.')[0]
  print(zip_file)
  print(password)



while True:
	with ZipFile(zip_file,"r") as zf:
		p = zf.extractall(pwd=bytes(password,'utf-8'))
		archive = zf.infolist()
		read_me_file = archive[-1]
		zip_file = read_me_file.filename
		password = zip_file.split('.')[0]
