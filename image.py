import music21 
import random
from PIL import Image
import math


for m in range(0,5):
	im = Image.open("a"+str(m)+".png")
	pixels = im.load()


	output_notes = []
	for z in range(0,3):
		print(z)
		for w in range(0,3):
			for a in range(1,5):
				for j in range(16*z,16*(1+z)):
					i = 16*w
					while i <16*(1 + w):
						pixelcolor = pixels[i,j]
						new_note = music21.note.Note(pixelcolor[0])
						new_note.offset = pixelcolor[2]*(a/2)
						new_note.quarterLength = (pixelcolor[1]/a)*(1/12)
						new_note.volume = .3
						output_notes.append(new_note)
						i = i +1
				
				midi_stream = music21.stream.Stream(output_notes)
				midi_stream.write('midi', fp='music/'+ str(m) +'/musica'+'z'+str(z)+str(w)+str(a)+'.mid')
				output_notes = []
