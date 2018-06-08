import pandas
import simplekml
import tkinter
from tkinter.filedialog import askopenfilename

def open_file():
    global infile
    infile = askopenfilename()


def kml_generator(outfile="/home/ujjwal/Desktop/file2.kml"):
    data_frame = pandas.read_csv(infile)
    kml = simplekml.Kml()
    for lon,lat in zip(data_frame["Longitude"],data_frame["Latitude"]):
        kml.newpoint(name = "point",coords= [(lon,lat)])
    kml.save(outfile)

window = tkinter.Tk()
window.title("KML Generator")
label = tkinter.Label(window,text="This program generates a KML file.")
label.pack()
browse_button = tkinter.Button(window,text="Browse",command=open_file)
browse_button.pack()
Generate_KML_button = tkinter.Button(window,text="Generate KML",command=kml_generator)
Generate_KML_button.pack()
tkinter.mainloop()