import os
import sys
import time


user = raw_input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'Admin' and user == 'Admin':

    print ("Terima Kasih telah menggunakan script ini")

else:

    print ("Username atau Password salah")
