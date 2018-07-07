import lirc

socket = lirc.init("myprogram")
print(lirc.nextcode())

lirc.deinit()