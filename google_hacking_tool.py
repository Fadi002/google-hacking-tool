'''
MIT License
Copyright (c) 2022 fadi
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
try:
    import os, requests, shutil
except ImportError:
    import os;os.system("pip install -r requirements.txt")
    exit('restart program')
def Clear():
    os.system("cls" if os.name == "nt" else "clear")
Clear()
qua = [
    'site:{domain} intitle:index.of',
    'site:{domain} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini',
    'site:{domain} ext:sql | ext:dbf | ext:mdb',
    'site:{domain} ext:log',
    'site:{domain} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup',
    'site:{domain} ext:zip | ext:rar | ext:7z | ext:tar | ext:gz | ext:bz2 | ext:tgz | ext:z',
    'site:{domain} "authentication failure"; logname=" filetype:log',
    'intitle:{domain} "network engineer"',
    'intitle:{domain} "administrative assistant"',
    'intitle:{domain} "adminstrator"',
    'site:{domain} inurl:login',
    'site:{domain}+intext:"sql+syntax+near"+%7C+intext:"syntax+error+has+occurred"+%7C+intext:"incorrect+syntax+near"+%7C+intext:"unexpected+end+of+SQL+command"+%7C+intext:"Warning:+mysql_connect()"+%7C+intext:"Warning:+mysql_query()"+%7C+intext:"Warning:+pg_connect()"',
    'site:{domain} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:xls | ext:xlsx | ext:ods',
    'site:{domain}+ext:php+intitle:phpinfo+"published+by+the+PHP+Group"',
    'site:{domain}+ext:php+intitle:phpinfo+"configuration+file"',
    'site:{domain}+ext:php+intitle:phpinfo+"php.ini"',
    'site:{domain}+ext:php+intitle:phpinfo+"php.ini.defaults"',
    'site:{domain}+ext:php+intitle:phpinfo+"php.ini.global"',
]

def purplepink(text):
    os.system(""); faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded
def filterweb(url):
    if "https://" in url:
        pass
    elif "http://" in url:
        pass
    else:
        url = "https://" + url 
    return url
def clean(url):
    if "https://" in url:
        url = url.replace("https://", "")
    elif "http://" in url:
        url = url.replace("http://", "")
    if url[-1] == "/":
        url = url[:-1]
    return url
print(purplepink('''                                               ,--.!,
                                            ─/   -*-
╔═╗┌─┐┌─┐┌─┐┬  ┌─┐  ╦ ╦┌─┐┌─┐┬┌─┬┌┐┌┌─┐   ,d08b.  '|`
║ ╦│ ││ ┬│ ┬│  ├┤   ╠═╣├─┤│  ├┴┐│││││ ┬   0088MM     
╚═╝└─┘└─┘└─┘┴─┘└─┘  ╩ ╩┴ ┴└─┘┴ ┴┴┘└┘└─┘   `9MMP'
Try to found information about websites.

> Author : Fadi
> GitHub : https://github.com/Fadi002

───────────────MENU───────────────
[1] check website if up or down
[2] check robots.txt of website
[3] try google hacking
──────────────────────────────────'''))
select = input("Enter your choice : ")
try:
    select = int(select)
except:
    input("\nPlease enter a number")
    Clear()
    exit("exiting...")
#--------------------------------------------------------------------------#
if select == 1:
    site = input("Enter website : ")
    site = filterweb(site)
    try:
        x=requests.get(site)
        print("Website is up")
    except:
    
        print("Website is down")
    input("\nPress enter to exit")
    
    Clear()
    
    exit("exiting...")
#--------------------------------------------------------------------------#
elif select == 2:
    site = input("Enter website : ")
    
    site=filterweb(site)
    
    name = site.replace("https://", "").replace("http://", "").replace("/", "")

    x=requests.get(f"{site}/robots.txt")
    
    if x.status_code == 200:
        print(x.text)
        print(f'\nsaved on : {name}\\robots.txt')
    else:   
        print("Website is down / no robots.txt")
    try:
        os.mkdir(name)
    except:
        pass

    with open(name+'\\robots.txt', 'w') as f:
        f.write(x.text)
        f.close()
    
#--------------------------------------------------------------------------#
elif select == 3:
    site = input("Enter website : ")
    
    site=clean(site)

    name = site.replace("https://", "").replace("http://", "").replace("/", "")

    print('copy the keywords and paste them on google\n')

    try:
        os.mkdir(name)
    except:
        pass

    with open(name+'\\keywords.txt', 'w') as f:
        f.write(';generated by Google hacking tools\n')
        f.close()
    for i in qua:
        print(i.replace("{domain}", site))
        with open(name+'\\keywords.txt', 'a') as f:
            f.write(i.replace("{domain}", site)+'\n')
            f.close()
#--------------------------------------------------------------------------#
else:
    
    print("\nPlease select a number between 1 and 3")
    
    Clear()
    
    exit("exiting...")

input('\npress enter to exit')
Clear()
exit("exiting...")