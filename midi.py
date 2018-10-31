import music21 as m21
import random
from PIL import Image
import glob
import math
m = 0
for a in range(0,12):
	print("Starting"+ str(a))
	m = 0
	for file in glob.glob("data/midi/*.mid"):
		m = m + 1
		b = m21.converter.parse(file)
		n = b.flat.notes
		t= 0
		g = 0
		for i in n:
			if i.isNote:
				t = t+1
				if i.offset < 60*(a+1) and i.offset > 60*a:
					g = g + 1
			if i.isChord:
				t = t+ len(i.pitches)
				if i.offset < 60*(a+ 1) and i.offset > 60*a:
					g = g + len(i.pitches)

		
		print(t, g, m)
		if t > 16*16*(a+1) and g > 16*16:
			im = Image.new("RGB",(t, 1))
			pixels = im.load()

			z= 0 
			for i in n:
				if  i.offset > 60*a and i.offset < 60*(a+1):
					if i.isNote:
						pixels[z,0] = (i.pitch.midi, int(12*i.quarterLength), (math.trunc(i.offset*4) - 240*a))
						z = z+1
					if i.isChord:
						for j in range(0,len(i.pitches)):
							pixels[z+j,0] = (i.pitches[j].midi, int(12*i.quarterLength), math.trunc(i.offset*4)- 240*a)					
						z = z+ len(i.pitches)
				


			img = Image.new("RGB",(16, 16))
			pixelsn = img.load()

			x = 0

			for y in range(0,16):
				for j in range(0,16):
					pixelsn[j,y]= pixels[x,0]
					x = x + 1
			

			img.save('data/image/image' + str(a)+ str(m) +'.png')
		
