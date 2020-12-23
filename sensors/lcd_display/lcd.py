import lcddriver
import sys
import time

lcd = lcddriver.lcd()
i =0
for arg in sys.argv:
	if i>0:
		lcd.lcd_display_string(arg, i)
	i+=1

time.sleep(5)

lcd.lcd_clear()
