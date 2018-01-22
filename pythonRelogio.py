# Relógio com tempo real

Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter
>>> relogio = tkinter.Label()
>>> relogio.pack()
>>> relogio['text'] = '15:55:50'
>>> relogio['font'] = 'Tahoma 50 bold'
>>> from time import strftime
>>> def relogioTempoReal():
	relogio['text'] = strftime('%H:%M:%S')
	relogio.after(1000, relogioTempoReal)

	
>>> relogioTempoReal()
>>> 
