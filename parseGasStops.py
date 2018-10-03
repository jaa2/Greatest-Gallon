import pandas
import csv as cs

#Import provided dataset
csv = pandas.read_csv("fuel_card_exportcsvalphabet.csv")

#Create a dataset with one entry for each station
namededuped = csv.drop_duplicates("Merchant Street Address")

#Declare variables
out = []
i = 0
offset = 0

#Add address and merchant name to return list (out)
for index, row in namededuped.iterrows():
    addr = row["Merchant Street Address"]
    name = row["Merchant Name"]
    city = row["Merchant City"]
    out.append([name, str(addr) + " " + str(city) + " Illinois", 0, 0, 0, 0, 0, 0])


#Calculate the running totals of transactions, money spent, and difference from average
for each in range(len(out) - 2):
    addr = out[each][1]
    for inner, row in csv.iterrows():
        inneraddr = csv.loc[offset]["Merchant Street Address"]
        i = offset

        while i <= 6306 and addr.find(csv.loc[i+1]["Merchant Street Address"]) != -1:
            print ([addr, csv.loc[i+1]["Merchant Street Address"]])
            out[each][6] += ((csv.loc[i]["Unit Cost"]) - 2.35)
            out[each][7] += 1
            out[each][5] += (csv.loc[i]["Unit Cost"])
            i += 1
            offset = i
#Calculate the average cost, difference from mean, and % difference from mean using the data collected above
for each in out:

    if each[7] != 0:
        each[2] = each[5]/each[7]
        each[3] = each[6]/each[7]
    each[4] = ((2.35 - each[2]) / 2.35) * 100.0

#Write the final out list to a csv
with open('export.csv', 'w', newline='') as myfile:
    wr = cs.writer(myfile, quoting=cs.QUOTE_ALL)
    for each in out:
        wr.writerow(each)

