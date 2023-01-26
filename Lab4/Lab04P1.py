##
# Myles Joubert
# Date - 1/24/2023
# Paint Job Estimator
#
import math

# Global constants for paint job estimator
FEET_PER_GALLON = 147
LABOR_HOURS = 8
LABOR_CHARGE = 46.50
PROJECT_FEE = 75.00

# main module
def main():
    # Ask the user for the wall space in square feet
    feetWall = float(input("Enter the square feet of wall space to be painted: "))

    # Ask the user for the paint price per gallon
    pricePaint = float(input("Enter the price of the paint per gallon: "))
        
    # Calculate gallons of paint
    gallonPaint = math.ceil(feetWall / FEET_PER_GALLON)

    # Calculate labor hours (8 hours labor for every gallon of paint)
    hourLabor = gallonPaint * LABOR_HOURS

    # Calculate labor charge
    costLabor = hourLabor * LABOR_CHARGE + PROJECT_FEE

    # Calculate paint cost
    costPaint = gallonPaint * pricePaint

    # Print cost estimate
    showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor)

# The showCostEstimate function accepts gallonPaint, hourLabor,
# costPaint, costLabor as arguments and displays the corresponding
# data.
def showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor):
# Calculate total cost
    totalCost = costPaint + costLabor

    # Display results
    print (f'Gallons of paint: {gallonPaint}')
    print (f'Hours of labor: {hourLabor}')
    print (f'Paint charges: ${costPaint:.2f}')
    print (f'Labor charges: ${costLabor:.2f}')
    print (f'Total cost: ${totalCost:.2f}')

# Call the main function.
main()
