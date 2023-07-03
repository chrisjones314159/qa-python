import csv

# companies = []
# months = []

# sales = {}

# with open("output.csv") as file:
#     lines = file.readlines()

#     for line in lines[0].split(","):
#         months.append(line.strip())
    
#     for line in lines:
#         list = []
#         company = ""
#         l = line.split(",\"")

#         for i in l:
#             i = i.replace(",", "")
#             i = i.replace("\"", "")
#             list.append(i)
#             company = list[0]
    
#         del list[0]

#         if len(list) > 1:
#             print(list[0])
        
#         companies.append(company)
#         ints = [eval(k) for k in list]
#         sales.update({company: sum(ints)})

    
#     del sales[companies[0]]
#     del companies[0]
#     print(months)
#     print(sales)



# companies = []
# sales = []

# with open("output.csv") as csvfile: # dont need r or w as csv module handles this. 
#     reader = csv.reader(csvfile) # reader function from the cvs module, which reads all the lines.
#     next(reader) # skips the first line dont need the header data
#     for row in reader:
#         companies.append(row[0])
#         sales.append([int(x.replace(",", "")) for x in row[1:]]) # iterates from index 1 to the end, changes from str to int and gets rid of ","
# #print(sales)
# monthly_sum = [sum(x) for x in zip(*sales)] # unpacks the list of lists into tuples, and sums.

# #print(monthly_sum)

# yearly_sum = {}
# for i in range(len(companies)):
#     yearly_sum[companies[i]] = sum(sales[i])

# print("monthly sales:", monthly_sum)
# print("yearly sales:")
# for company, sales in yearly_sum.items():
#     print(company, sales)





companies = []
sales = []
months = []

mSale = []
month = []

compSales = {}
monthSales = {}
cSale = []


with open("output.csv") as file:

    months = file.readline().split(",")

    lines = file.readlines()

    for line in lines:
        line = line.split(",\"")
        
        # Creating list of Companies
        for comp in range(0, 1):
            companies.append(line[0])
        # Deletes the company from the line
        del line[0]


        comp = []
        for sale in line:
            sale = sale.replace(",", "")
            sale = sale.replace("\"", "")
            comp.append(int(sale.strip()))

        mSale.append(comp)
        cSale.append(sum(comp))

    for c in range(0 ,len(companies)):
        compSales.update({companies[c]: cSale[c]})


    # Appends the sum of each month to a list
    for k in range(len(mSale[0])):
        sum1 = [mSale[x][k] for x in range(len(mSale))]
        month.append(sum(sum1))
   
    # Combines the sum of each month with the corresponding month values into a dictionary
    for m in range(0, len(months)):
        monthSales.update({months[m]: month[m]})

  
    print(compSales)
    print(monthSales)