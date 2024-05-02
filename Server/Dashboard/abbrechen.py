#!C:/Users/id859972/OneDrive - IPT Ostfalia Hochschule für angewandte Wissenschaften/Dokumente/TicTacToe/Server
# test.py
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
    msg = rcvd.decode('UTF-8')
    if msg == 'true':
        print('running')
    print('erhaltene nachricht{}'.format(rcvd))


def main():
    '''
    Enthält den gewuenschten Befehlsablauf
    '''
    # Aufruf der Funktion zum Setzen des Schwierigkeitgrades
    #set_int_register(24,3)
    # Laden des Programms.
    state = sendCommand('running')
    sendCommand('stop')
    # Start des Programms.
    #sendCommand('popup Abbrechen wurde ausgewählt!')

main()

