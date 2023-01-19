![E-LBF](https://github.com/m4kr0-3Px/E-LBF/blob/main/web_brute_force.jpeg)
# E-LBF
 This tool was created with the aim of brute force the login page of websites.<br><br>There are 3 options in this vehicle. These are: To learn the user name information, to do brute force to log in with the known user name, and the last one is to perform brute force in both parts without knowing both the username and the password. Whichever of the options you choose, certain inputs are taken from you.After these inputs pass through a verification mechanism, the desired operation is performed.<br><br>In order to use the inputs given while using this tool, the request Burp Suit etc. sent by post method is captured with a tool and the requirements are written to the places. For example, you need to know the data of an outgoing request with the username parameter and the password parameter. While the 'variable' parts in the program are the username and password parameters I have just mentioned, the parts called 'value' are the paths of the wordlists taken from you.Therefore, even if the request that does not contain the username, password, and parameters such as the confirmation button is caught, I do not think it will provide any benefit. Although this tool works on many sites, the most effective area is WordPress-based sites.
 
 ## Usage:
 **git clone https://github.com/m4kr0-3Px/E-LBF.git<br>cd E-LBF<br>python3 web_brute_force.py**

 
 ## Social Media
 [Linkedin](https://www.linkedin.com/in/eren-polat-6a5048248/)<br>
 [Web Site](https://www.infcommunity.web.tr/)
 
