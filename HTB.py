#!/usr/bin/python
# -*- coding: utf-8 -*-


import base64
import requests

RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
END = '\033[0m'

logo = RED \
    + """                                                                                                                                                                                                     
######                          ###                              
#     #   ##   #    # #    #     #  #    # #    # # ##### ###### 
#     #  #  #  ##  ## ##   #     #  ##   # #    # #   #   #      
#     # #    # # ## # # #  #     #  # #  # #    # #   #   #####  
#     # ###### #    # #  # #     #  #  # # #    # #   #   #      
#     # #    # #    # #   ##     #  #   ##  #  #  #   #   #        
######  #    # #    # #    #    ### #    #   ##   #   #   ######   
                                                                              
         \033[1;34m [+] Hackthebox.gr Invite Code Generator [+]    
                                                                  
\033[1;34mCoded:Nycto                                 

 \033[1;34mHappy Hacking..!!            
--------------------------------------------------------------------
""" \
    + END
print logo

a = requests.post('https://www.hackthebox.eu/api/invite/generate')
print GREEN + a.text + END
print '\n'
b = raw_input(BLUE + BOLD + 'Type the Base64 code : ' + END)
print '\n'
print BLUE + BOLD + 'Decoded Code :  {0}'.format(YELLOW
        + b.decode('base64')) + END


			
