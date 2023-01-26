#
# Myles Joubert
# 1/13/2023
# Wavelength Classifier
#

# Get the wavelength.
wavelength = int(input('Enter the wavelength (in nm): '))

# Determine the classification of the wavelength
# and display the result.
if wavelength < 10:
    print('Below range')
elif wavelength >= 10 and wavelength < 401:
    print('Infrared')
elif wavelength >= 401 and wavelength <= 700:
    print('Visible light')
elif wavelength > 700 and wavelength < 1000:
    print('Ultraviolet')
else:
    print('Above range')
