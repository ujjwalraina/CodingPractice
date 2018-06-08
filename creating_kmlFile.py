import simplekml
#creating a kml file
kml = simplekml.Kml()
kml.newpoint(name="office",coords=[(77.071417,28.451778)])   #long,lat
kml.newpoint(name="janakpuri",coords=[(77.087838,28.621899)])   #long,lat
kml.save("/home/ujjwal/Desktop/file.kml")