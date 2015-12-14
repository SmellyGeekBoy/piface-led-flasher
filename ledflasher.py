#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ledflasher.py
#  
#  Copyright 2014 Rees Clissold
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def main():
	from time import sleep
	import pifacedigitalio as p
	p.init()
	speed = 1

	while(True):
		if p.digital_read(0):
			speed = 0.7
		elif p.digital_read(1):
			speed = 0.5
		elif p.digital_read(2):
			speed = 0.4
		elif p.digital_read(3):
			speed = 0.2
		elif p.digital_read(4):
			speed = 0.05
		
		print("Speed:" + str(speed))
		
		p.digital_write(0,1) #turn 0 on (green)
		p.digital_write(3,1) #turn 3 on (buzzer)
		sleep(speed)
		p.digital_write(3,0) #turn 3 off (buzzer)
		p.digital_write(0,0) #turn 0 off (green)
		p.digital_write(1,1) #turn 1 on (yellow)
		p.digital_write(3,1) #turn 3 on (buzzer)
		sleep(speed)
		p.digital_write(3,0) #turn 3 off (buzzer)
		p.digital_write(1,0) #turn 1 off (yellow)
		p.digital_write(2,1) #turn 2 on (red)
		p.digital_write(3,1) #turn 3 on (buzzer)
		sleep(speed)
		p.digital_write(3,0) #turn 3 off (buzzer)
		p.digital_write(2,0) #turn 2 off (red)
	
	return 0

if __name__ == '__main__':
	main()
