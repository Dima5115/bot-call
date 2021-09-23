import os
import sys
import time


banner="""

              LOGIN, SOLDUDO JONGEN!.....
                 |Dima Os Group|


            |---------------------|     |------------------|
            |       SOLDUDO       |     | SOLDUDO?         |
            |  |---------------|  |     |------------------|
            |--|               |--|          .
                ----\\  // ----            .
                                         .
                 [--]     [--]        .

             \ \               / /
              \ \             / /
               \ \           / /
                \ \         / /
                 \ \       / /
                  \ \     / /
                   \ \   / /



"""

os.system('clear')
print (banner)
user = raw_input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'Admin' and user == 'Admin':

    print ("Terima Kasih telah menggunakan script ini")

else:

    print ("Username atau Password salah")
