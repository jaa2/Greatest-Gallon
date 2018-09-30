# Greatest-Gallon
Kyle McNamara, Sean Coughlin, James Austgin, Isaac Warren


**General Program Description**

This program is for the police department, fire department, and other Champaign-Urbana public service vehicles. 
Greatest Gallon will display where to get the cheapest gas to these organizations to help reduce their costs.

**Python Script parseGasStops**

Takes in an excel spreadsheet and an alphabetized version of the spreadsheet by gas station name.

Calculates average unit cost from every transaction that took place during the year. Calculates average unit cost for each individual gas station.

Returns 2D array containing each gas station’s name, address, number of units recorded, the difference of A and B (the difference of the averages),
average difference of the unit cost of each gas station and the total average unit cost (A-B) / number of units recorded, percent difference between the station’s average and the total average, and average cost per gallon.

Returns as a csv file.

**Wolfram Program**

Takes in csv file that parseGasStops returns.

Uses Wolfram to create a dynamic map showing each gas station with a color to display how cheap or expensive it is (from green (cheap) to red (expensive)). 
When the user clicks an individual gas station, more information will be shown including the gas station name, address, average unit cost, average difference between its average and the total average, and the percent difference.
