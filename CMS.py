import builtwith
import urllib
import bs4
import os


print '''
                  
########         ###        ##        #######
#               #   #      #  #       #
#              #     #    #    #      #######     
#            #        #  #      #           #
########   ##          ##        ##   ####### 

usage ==> * http://site.com *

'''     
while True:
    print "\n"
    print "***********"
    print  "\n"
    u = raw_input('Enter The Domain with "http://" : ')
    os.system("cls")
    link = urllib.urlopen(u)

    source = link.read()

    if "wp-content" in source:
        print "\n\t [*] CMS is Wordpress [*]"
        t = "w"
    elif "joomla" or "/index.php?option=com_" in source:
        print "\n\t [*] CMS is Joomla [*]"
        t = "j"
    elif "vbulletin" in source:
        print "\n\t [*] CMS is Vbulletin [*]"     
    else:
        print "\n\t [!] Can't realize [!]"

    if t== "w":
        url = builtwith.builtwith(u)
        print "\n"
        print "Web Server => ",url['web-servers'][0]
        print "\n"
        print "java script framework =>",url['javascript-frameworks'][0]
        print  "\n"
        print "Program language =>",url['programming-languages'][0]
        print "\n"
        r = urllib.urlopen(u+"/wp-login.php")
        if r.code == 200:
            print "Page Login is => /wp-login.php"
            print "\n"
        r = urllib.urlopen(u+"/readme.html")
        if r.code == 200:
            print "Check  =>"+u+"/readme.html"
            print "\n"
            print "*****************************"
            print "\n"
            print "[*] Plugins [*]"
        filter = bs4.BeautifulSoup(source , "html.parser")
        for plugin in filter.find_all("link"):
            pl = plugin.get("href")
            tl = plugin.get("href")
            if "/wp-content/plugins" in pl and  "/wp-content/plugins" in tl:
                p = pl[39:]
                pl= p.find("/")
                print "\n",p[:pl]
    elif t == "j":
        
        url = builtwith.builtwith(u)
    
        print "\n"
        print "Web Server => ",url['web-servers'][0]
        print "\n*********"
        print "java script framework =>",url['javascript-frameworks'][0]
        print "\n*********"
        print "Program language =>",url['programming-languages'][0]
        print "\n*********"
        print "Page Login is => /administrator.php"
        print "\n****************"
        print "[*] Components [*] \n"
        filter = bs4.BeautifulSoup(source , "html.parser")
        for component in filter.find_all("link"):
            comp = component.get("href")
            if "/components" in comp:
                comp1 = comp[12:]
                comp = comp1.find("/")
                print "\n",comp1[:comp]
        print "\n*****************"
        print "[*] Plugins [*]"
        filter = bs4.BeautifulSoup(source, "html.parser")
        for plug in filter.find_all("link"):
            plugs = plug.get("href")
            if "plugins/system/" in plugs:
                plugs1 = plugs[16:]
                plugs = plugs1.find("/")
                print "\n",plugs1[:plugs]       


