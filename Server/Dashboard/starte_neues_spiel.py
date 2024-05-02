#!C:/Users/id859972/OneDrive - IPT Ostfalia Hochschule für angewandte Wissenschaften/Dokumente/TicTacToe/Server
# test.py
import rtde
import time
import socket

# IP-Adresse und Portnummer
addr = '10.136.90.104'
port = 29999

# TCP-Socket definieren und Verbindung aufbauen
# Timeout nach 2s ohne Verbindungserfolg
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect((addr, port))


def sendCommand(cmd: str) -> None:
    '''
    Funktion zum Senden von Befehlen.
    Übergeben wird der Befehl gemäß Befehlssatz-PDF im Stringformat
    '''
    cmd = cmd + '\n'
    s.sendall(cmd.encode())

    received_message()


def received_message() -> None:
    '''
    Auslesen der Antwort und Schreiben auf die Konsole.
    Kurzer Delay fuer die Verarbeitung des vorhergehenden Befehls
    '''
    time.sleep(1)
    rcvd = s.recv(4096)
    print(rcvd)


def set_int_register(position,value):
    # IP aus Controller eintragen, Port ist fest für RTDE
    con = rtde.RTDE("10.136.90.104", 30004)
    # Verbindung aufbauen
    con.connect()

    # Was soll gelesen werden? (siehe PDF)
    # Namen und Datentyp aus PDF
    con.send_output_setup(variables=[(
        'input_int_register_{}'.format(position))], types=['INT32'])

    # Was soll geschrieben werden? (siehe PDF)
    # Logische UND-Verknüpfung von Maske und zu schreibenden Bits, sodass nur die "maskierten" Bits geändert werden
    setp = con.send_input_setup(variables=[(
        'input_int_register_{}'.format(position))], types=['INT32'])

    # Start der Uebertragung
    con.send_start()
    #Aufruf der Funktion zum Setzen der Int_Variablen.
    # Define a dictionary mapping positions to attribute names
    positions_to_attributes = {
        24: 'input_int_register_24',
        25: 'input_int_register_25',
        26: 'input_int_register_26',
        27: 'input_int_register_27',
        28: 'input_int_register_28',
        29: 'input_int_register_29',
        30: 'input_int_register_30',
        31: 'input_int_register_31',
        32: 'input_int_register_32',
        33: 'input_int_register_33',
        34: 'input_int_register_34',
        35: 'input_int_register_35',
        36: 'input_int_register_36',
        37: 'input_int_register_37',
        38: 'input_int_register_38',
        39: 'input_int_register_39',
        40: 'input_int_register_40',
        41: 'input_int_register_41',
        42: 'input_int_register_42',
        43: 'input_int_register_43',
        44: 'input_int_register_44',
        45: 'input_int_register_45',
        46: 'input_int_register_46',
        47: 'input_int_register_47',
    }

    # Check if the position is in the dictionary
    if position in positions_to_attributes:
        # Get the attribute name corresponding to the position
        attribute_name = positions_to_attributes[position]
        # Set the attribute value dynamically using setattr
        setattr(setp, attribute_name, value)
    else:
        print(f"No attribute found for position {position}")

    con.send(setp)

    time.sleep(1)
    # # Status lesen (führende Nullen werden nicht dargestellt)
    # print('Statusbits: ' + bin(con.receive().robot_status_bits))
    # # Output-Register lesen (führende Nullen werden nicht dargestellt)
    # print('Outputs: ' + bin(con.receive().actual_digital_output_bits))
    # Integer Register lesen
    print('Integer Register: ' + str(con.receive().input_int_register_24))
    

def main():
    '''
    Enthält den gewuenschten Befehlsablauf
    '''
    # Aufruf der Funktion zum Setzen des Schwierigkeitgrades
    #set_int_register(24,3)
    # Laden des Programms.
    sendCommand('load TicTacToe/test.urp')
    # Start des Programms.
    sendCommand('play')

main()

