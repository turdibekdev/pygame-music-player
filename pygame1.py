# t.me/turdibekdev

# paketni chaqirish uchun
from pygame import *

# mixer'ni ishlatish
mixer.init()

# musiqani yuklash
mixer.music.load("Doxxim_songi_uchrashuv.mp3")

# musiqani ovozini sozlash
mixer.music.set_volume(0.5)

# musiqani oynatish
mixer.music.play()


#musiqani davomiyligini saqlash
while True:
	print("Buyruqlar royxati\n")
	print("Toxtatish: T yoki t")
	print("Davom ettirish: D yoki d ")
	print("Yakunlash: S yoki s ")
	
	# buyruni qabul qilish
	cd = input("       ")
	
	if cd == "T" or cd == "t":
		# musiqani toxtatib turish
		mixer.music.pause()
		
	elif cd == "D" or cd == "d":
		# musiqani yana davom ettirish
		mixer.music.unpause()
		
	else:
		# musiqani yakunlash
		mixer.music.stop()