Location = r'WB_-_Health_Nutrition_and_Population_Statistics.csv'

with open(Location, "rb") as ifile:
	data_rows = ifile.read().split("\r\n")
	
for index, row in enumerate(data_rows):
	data_rows[index]= row

header = data_rows.pop(0).split(",")

new_headers = ["Country", "Country Code", "Indicator", "Indicator Code", "Indicator Value", "Year",  "Source"]

final_data = []
for  data in data_rows:
	 final_data.extend([data.split(",")])

with open("2015_wb_data_clean3.csv", "wb") as xfile:
	for headers in new_headers:
		xfile.write(headers)
		xfile.write(",")
	xfile.write("\n")
	for index,data in enumerate(final_data):
		for x in range(4,58):
			if data[x] == "":
				pass
			else:
				xfile.write("{0},{1},{2},{3},{4},{5},{6}\n".format(data[0], data[1], data[2], data[3], data[x],header[x], "World Bank"))


