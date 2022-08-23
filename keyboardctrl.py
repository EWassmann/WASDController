import serial
#connecting to the arduinop using serial communications

arduino = serial.Serial(
port = '/dev/ttyACM0',
baudrate = 2000000, #perhaps make this lower need to do research
bytesize = serial.EIGHTBITS,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
timeout = 5,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout = 2
)
#these write strins to the arduino which it then uses to determine how to move, b is not used in this code,
#it is left over from other search code.
#----------------Functions---------------------------
def Left():
    arduino.write("1".encode()) 
    
def Forward():
    arduino.write("0".encode())
  
def Right():
    arduino.write("2".encode())
  
def Stop():
    arduino.write("4".encode())
   
def Back():
    arduino.write("3".encode())
   
def Search():
    arduino.write("5".encode())
    


#----------------------------------------------------
#waits for an input and then runs the command which tells the arduino what to do, gotta figure out how to not have to hit enter every time

while True:

    directions = input()
    if directions == "w":
        Forward()
    if directions == "a":
        Left()
    if directions =="d":
        Right()
    if directions == "s":
        Stop()
    if directions == "ss":
        Back()    

