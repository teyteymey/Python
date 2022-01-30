import requests
import json
import datetime

def obtener_cookies():

    cookies = {
        'KEYCLOAK_LOCALE': 'ca',
        'KEYCLOAK_REMEMBER_ME': 'username:tatiana.meyer.u%40gmail.com',
        'AUTH_SESSION_ID': 'dc8b2f61-f60c-4155-bbb1-fd82061ff9fe.BlackWidow',
        'AUTH_SESSION_ID_LEGACY': 'dc8b2f61-f60c-4155-bbb1-fd82061ff9fe.BlackWidow',
        'KC_RESTART': 'eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIwNWNkMzBmNS0yZjdiLTQ1NWQtOTI3MS0wOTJjYTI3ZWYxM2YifQ.eyJjaWQiOiJqb3RtYmVfaWRwIiwicHR5Ijoib3BlbmlkLWNvbm5lY3QiLCJydXJpIjoiaHR0cHM6Ly9hdXRoLnRtYi5jYXQvYXV0aC9yZWFsbXMvdG1iL2Jyb2tlci9qb3RtYmUvZW5kcG9pbnQiLCJhY3QiOiJBVVRIRU5USUNBVEUiLCJub3RlcyI6eyJzY29wZSI6Im9wZW5pZCIsImlzcyI6Imh0dHBzOi8vYXV0aC50bWIuY2F0L2F1dGgvcmVhbG1zL2pvdG1iZSIsInJlc3BvbnNlX3R5cGUiOiJjb2RlIiwiY2xpZW50X3JlcXVlc3RfcGFyYW1fa2NfbG9jYWxlIjoiY2EiLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2F1dGgudG1iLmNhdC9hdXRoL3JlYWxtcy90bWIvYnJva2VyL2pvdG1iZS9lbmRwb2ludCIsInN0YXRlIjoia1QzdDhoNkhfWHA1cDktNmFnd25NMThUamg1dHlSZTB0Rl9HdFF3dXZ1dy5jRlpvTEhJOGYydy53ZWJfdG1iIiwibm9uY2UiOiJ6eldZbjlMZkdXSW02aEtKTHhfUmlRIn19.HWA4x2wGrbCyLqAt8vbWu12J2O6je6JxyYjct8x8cyw',
        'user_level': '%7B%22id%22%3A2%2C%22code%22%3A%22N2%22%2C%22name%22%3A%22Nivell%202%22%2C%22description%22%3A%22Nivel%202%22%2C%22minPoints%22%3A200%2C%22maxPoints%22%3A500%2C%22points%22%3A462%7D',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://auth.tmb.cat',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://auth.tmb.cat/auth/realms/jotmbe/protocol/openid-connect/auth?scope=openid&state=kT3t8h6H_Xp5p9-6agwnM18Tjh5tyRe0tF_GtQwuvuw.cFZoLHI8f2w.web_tmb&response_type=code&client_id=jotmbe_idp&redirect_uri=https%3A%2F%2Fauth.tmb.cat%2Fauth%2Frealms%2Ftmb%2Fbroker%2Fjotmbe%2Fendpoint&ui_locales=ca&kc_locale=ca&nonce=zzWYn9LfGWIm6hKJLx_RiQ',
        'Accept-Language': 'es-ES,es;q=0.9',
    }

    params = (
        ('session_code', 'voUDvvMjuHHpCN4YLO6XycVn8CxgIw1KGI_kYyzxfBY'),
        ('execution', 'c4587a2a-020c-44e1-9d3e-8eba0bf4e29e'),
        ('client_id', 'jotmbe_idp'),
        ('tab_id', 'k34B43Ggr4c'),
    )

    data = {
      'username': 'tatiana.meyer.u@gmail.com',
      'password': '3Cerditos',
      'rememberMe': 'on'
    }

    response = requests.post('https://auth.tmb.cat/auth/realms/jotmbe/login-actions/authenticate', headers=headers, params=params, cookies=cookies, data=data)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    response = requests.post('https://auth.tmb.cat/auth/realms/jotmbe/login-actions/authenticate?session_code=voUDvvMjuHHpCN4YLO6XycVn8CxgIw1KGI_kYyzxfBY&execution=c4587a2a-020c-44e1-9d3e-8eba0bf4e29e&client_id=jotmbe_idp&tab_id=k34B43Ggr4c', headers=headers, cookies=cookies, data=data)
    print(response.content)
    print(response.cookies)

#cookiestati =     'cookie': 'JoTMBeKCSession=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqOWt6MkV0WWZNM0tVYXI0aGhoZjZHcjdSN1QxQWVHb3NvdG12MEZOTjZBIn0.eyJleHAiOjE2NDM1NzEyNjEsImlhdCI6MTY0MzU2NDA2MSwiYXV0aF90aW1lIjoxNjQzNTY0MDU4LCJqdGkiOiI4OTNlYTQzZi05ZjVmLTRhN2YtOWZjNy0xM2UyYzZkYTcwMTQiLCJpc3MiOiJodHRwczovL2F1dGgudG1iLmNhdC9hdXRoL3JlYWxtcy90bWIiLCJhdWQiOiJodHRwczovL2FwaS50bWIuY2F0Iiwic3ViIjoiYTI1YmQ5OGItMzc1Ni00OTkyLWI3MWYtZTE5ODNiNGExYzZmIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViX3RtYiIsIm5vbmNlIjoiNWVmOGZkYzItNDlkNy00NTAyLThjZGQtNTUxNGE4NGJlNTk5Iiwic2Vzc2lvbl9zdGF0ZSI6IjcxMDdjNzI5LTQyMDYtNDQ0Mi04YmQxLWY2ZGM0M2NiNTY1NiIsImFjciI6IjEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFwaV9zY29wZXMiLCJhcGlfc2NvcGVzIjpbInJlYWQ6ZWNvbW1yX3ByZSIsIm1hbmFnZTpqb3RtYmUiLCJyZWFkOnByb2dfcHVudHMiLCJyZWFkOmVjb21tciIsImFwaTp2MyJdLCJlbWFpbF9yZXB1dGF0aW9uX3Njb3JlIjowLCJuYW1lIjoiVGF0aWFuYSBJbmdyaWQgTWV5ZXIgVXJhbiIsImVtYWlsX2Rpc3Bvc2FibGUiOmZhbHNlLCJ1dWlkIjoiZWQwZWI5MzAtNjJmYy00OWRmLTk0ZDMtOWE4MmQwMWFmZGI3IiwiZW1haWwiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIn0.P2a2_vh77yXvNx_-peJxu1PLZJyNsB_3kQVX4eV9urfl573daOMtzVK5n89uMH0EpJ0_gLM_LsG5WIE-8JDewm9mumU09Bfv__6l67_nXbtESHfBm0PiesIsuFRRVFBFJC0R4vUxOo-q6RwNF6YNXR4TQ6qiWfaXaIs_gj28hpnEXuBNXJLQlFHTWqPN_6bmUOq3Ga9rLscgMHCeYi8xR2SlL482gAhjyP-40_ITwkzT2YJ2z8ZZBL-5lPZJY-UEEcmwqZLQljav12wrv3uRZX6K-qlmdsjhXB0tYnUg56Rz-gNVIbATBAb3ZS9Z40ajhu6vMymh_CEMVqABRKG75g; PHPSESSID=i99nqc2kjc41che021npndhel6; user=%7B%22nom%22%3A%22Tatiana%20Ingrid%22%2C%22cognom1%22%3A%22Meyer%22%2C%22cognom2%22%3A%22Uran%22%2C%22acceptacioTermesLegals%22%3A4%2C%22clientId%22%3A844940%7D; user_level=%7B%22id%22%3A2%2C%22code%22%3A%22N2%22%2C%22name%22%3A%22Nivell%202%22%2C%22description%22%3A%22Nivel%202%22%2C%22minPoints%22%3A200%2C%22maxPoints%22%3A500%2C%22points%22%3A462%7D; JoTMBeSession=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqOWt6MkV0WWZNM0tVYXI0aGhoZjZHcjdSN1QxQWVHb3NvdG12MEZOTjZBIn0.eyJleHAiOjE2NDM1NzEyNjEsImlhdCI6MTY0MzU2NDA2MSwiYXV0aF90aW1lIjoxNjQzNTY0MDU4LCJqdGkiOiI4OTNlYTQzZi05ZjVmLTRhN2YtOWZjNy0xM2UyYzZkYTcwMTQiLCJpc3MiOiJodHRwczovL2F1dGgudG1iLmNhdC9hdXRoL3JlYWxtcy90bWIiLCJhdWQiOiJodHRwczovL2FwaS50bWIuY2F0Iiwic3ViIjoiYTI1YmQ5OGItMzc1Ni00OTkyLWI3MWYtZTE5ODNiNGExYzZmIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViX3RtYiIsIm5vbmNlIjoiNWVmOGZkYzItNDlkNy00NTAyLThjZGQtNTUxNGE4NGJlNTk5Iiwic2Vzc2lvbl9zdGF0ZSI6IjcxMDdjNzI5LTQyMDYtNDQ0Mi04YmQxLWY2ZGM0M2NiNTY1NiIsImFjciI6IjEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFwaV9zY29wZXMiLCJhcGlfc2NvcGVzIjpbInJlYWQ6ZWNvbW1yX3ByZSIsIm1hbmFnZTpqb3RtYmUiLCJyZWFkOnByb2dfcHVudHMiLCJyZWFkOmVjb21tciIsImFwaTp2MyJdLCJlbWFpbF9yZXB1dGF0aW9uX3Njb3JlIjowLCJuYW1lIjoiVGF0aWFuYSBJbmdyaWQgTWV5ZXIgVXJhbiIsImVtYWlsX2Rpc3Bvc2FibGUiOmZhbHNlLCJ1dWlkIjoiZWQwZWI5MzAtNjJmYy00OWRmLTk0ZDMtOWE4MmQwMWFmZGI3IiwiZW1haWwiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIn0.P2a2_vh77yXvNx_-peJxu1PLZJyNsB_3kQVX4eV9urfl573daOMtzVK5n89uMH0EpJ0_gLM_LsG5WIE-8JDewm9mumU09Bfv__6l67_nXbtESHfBm0PiesIsuFRRVFBFJC0R4vUxOo-q6RwNF6YNXR4TQ6qiWfaXaIs_gj28hpnEXuBNXJLQlFHTWqPN_6bmUOq3Ga9rLscgMHCeYi8xR2SlL482gAhjyP-40_ITwkzT2YJ2z8ZZBL-5lPZJY-UEEcmwqZLQljav12wrv3uRZX6K-qlmdsjhXB0tYnUg56Rz-gNVIbATBAb3ZS9Z40ajhu6vMymh_CEMVqABRKG75g',

def participar():
    headers = {
        'authority': 'jotmbe.tmb.cat',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://jotmbe.tmb.cat',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://jotmbe.tmb.cat/ca/promocions/moonfall-2022',
        'accept-language': 'es-ES,es;q=0.9',
        'cookie': 'JoTMBeKCSession=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqOWt6MkV0WWZNM0tVYXI0aGhoZjZHcjdSN1QxQWVHb3NvdG12MEZOTjZBIn0.eyJleHAiOjE2NDM1NzEyNjEsImlhdCI6MTY0MzU2NDA2MSwiYXV0aF90aW1lIjoxNjQzNTY0MDU4LCJqdGkiOiI4OTNlYTQzZi05ZjVmLTRhN2YtOWZjNy0xM2UyYzZkYTcwMTQiLCJpc3MiOiJodHRwczovL2F1dGgudG1iLmNhdC9hdXRoL3JlYWxtcy90bWIiLCJhdWQiOiJodHRwczovL2FwaS50bWIuY2F0Iiwic3ViIjoiYTI1YmQ5OGItMzc1Ni00OTkyLWI3MWYtZTE5ODNiNGExYzZmIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViX3RtYiIsIm5vbmNlIjoiNWVmOGZkYzItNDlkNy00NTAyLThjZGQtNTUxNGE4NGJlNTk5Iiwic2Vzc2lvbl9zdGF0ZSI6IjcxMDdjNzI5LTQyMDYtNDQ0Mi04YmQxLWY2ZGM0M2NiNTY1NiIsImFjciI6IjEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFwaV9zY29wZXMiLCJhcGlfc2NvcGVzIjpbInJlYWQ6ZWNvbW1yX3ByZSIsIm1hbmFnZTpqb3RtYmUiLCJyZWFkOnByb2dfcHVudHMiLCJyZWFkOmVjb21tciIsImFwaTp2MyJdLCJlbWFpbF9yZXB1dGF0aW9uX3Njb3JlIjowLCJuYW1lIjoiVGF0aWFuYSBJbmdyaWQgTWV5ZXIgVXJhbiIsImVtYWlsX2Rpc3Bvc2FibGUiOmZhbHNlLCJ1dWlkIjoiZWQwZWI5MzAtNjJmYy00OWRmLTk0ZDMtOWE4MmQwMWFmZGI3IiwiZW1haWwiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIn0.P2a2_vh77yXvNx_-peJxu1PLZJyNsB_3kQVX4eV9urfl573daOMtzVK5n89uMH0EpJ0_gLM_LsG5WIE-8JDewm9mumU09Bfv__6l67_nXbtESHfBm0PiesIsuFRRVFBFJC0R4vUxOo-q6RwNF6YNXR4TQ6qiWfaXaIs_gj28hpnEXuBNXJLQlFHTWqPN_6bmUOq3Ga9rLscgMHCeYi8xR2SlL482gAhjyP-40_ITwkzT2YJ2z8ZZBL-5lPZJY-UEEcmwqZLQljav12wrv3uRZX6K-qlmdsjhXB0tYnUg56Rz-gNVIbATBAb3ZS9Z40ajhu6vMymh_CEMVqABRKG75g; PHPSESSID=i99nqc2kjc41che021npndhel6; user=%7B%22nom%22%3A%22Tatiana%20Ingrid%22%2C%22cognom1%22%3A%22Meyer%22%2C%22cognom2%22%3A%22Uran%22%2C%22acceptacioTermesLegals%22%3A4%2C%22clientId%22%3A844940%7D; user_level=%7B%22id%22%3A2%2C%22code%22%3A%22N2%22%2C%22name%22%3A%22Nivell%202%22%2C%22description%22%3A%22Nivel%202%22%2C%22minPoints%22%3A200%2C%22maxPoints%22%3A500%2C%22points%22%3A462%7D; JoTMBeSession=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqOWt6MkV0WWZNM0tVYXI0aGhoZjZHcjdSN1QxQWVHb3NvdG12MEZOTjZBIn0.eyJleHAiOjE2NDM1NzEyNjEsImlhdCI6MTY0MzU2NDA2MSwiYXV0aF90aW1lIjoxNjQzNTY0MDU4LCJqdGkiOiI4OTNlYTQzZi05ZjVmLTRhN2YtOWZjNy0xM2UyYzZkYTcwMTQiLCJpc3MiOiJodHRwczovL2F1dGgudG1iLmNhdC9hdXRoL3JlYWxtcy90bWIiLCJhdWQiOiJodHRwczovL2FwaS50bWIuY2F0Iiwic3ViIjoiYTI1YmQ5OGItMzc1Ni00OTkyLWI3MWYtZTE5ODNiNGExYzZmIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViX3RtYiIsIm5vbmNlIjoiNWVmOGZkYzItNDlkNy00NTAyLThjZGQtNTUxNGE4NGJlNTk5Iiwic2Vzc2lvbl9zdGF0ZSI6IjcxMDdjNzI5LTQyMDYtNDQ0Mi04YmQxLWY2ZGM0M2NiNTY1NiIsImFjciI6IjEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIGFwaV9zY29wZXMiLCJhcGlfc2NvcGVzIjpbInJlYWQ6ZWNvbW1yX3ByZSIsIm1hbmFnZTpqb3RtYmUiLCJyZWFkOnByb2dfcHVudHMiLCJyZWFkOmVjb21tciIsImFwaTp2MyJdLCJlbWFpbF9yZXB1dGF0aW9uX3Njb3JlIjowLCJuYW1lIjoiVGF0aWFuYSBJbmdyaWQgTWV5ZXIgVXJhbiIsImVtYWlsX2Rpc3Bvc2FibGUiOmZhbHNlLCJ1dWlkIjoiZWQwZWI5MzAtNjJmYy00OWRmLTk0ZDMtOWE4MmQwMWFmZGI3IiwiZW1haWwiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJ0YXRpYW5hLm1leWVyLnVAZ21haWwuY29tIn0.P2a2_vh77yXvNx_-peJxu1PLZJyNsB_3kQVX4eV9urfl573daOMtzVK5n89uMH0EpJ0_gLM_LsG5WIE-8JDewm9mumU09Bfv__6l67_nXbtESHfBm0PiesIsuFRRVFBFJC0R4vUxOo-q6RwNF6YNXR4TQ6qiWfaXaIs_gj28hpnEXuBNXJLQlFHTWqPN_6bmUOq3Ga9rLscgMHCeYi8xR2SlL482gAhjyP-40_ITwkzT2YJ2z8ZZBL-5lPZJY-UEEcmwqZLQljav12wrv3uRZX6K-qlmdsjhXB0tYnUg56Rz-gNVIbATBAb3ZS9Z40ajhu6vMymh_CEMVqABRKG75g',
    }

    data = {
      'key': 'key_6371',
      'aaid': '32',
      'oid': '6371'
    }

    response = requests.post('https://jotmbe.tmb.cat/ca/ajax/x_logAccioMMGG', headers=headers, data=data)
    print(response.content)
    print(response.status_code)


def escribir_response():
    x = datetime.datetime.now()

    f = open("outputTMB.txt", "a")
    #escribe mes dia hora, response
    f.write(x.strftime("%b")+
            " " +
            x.strftime("%d") +
            " "+
            x.strftime("%X")+
            ", response= " +
            str(response.content)+
            "\n")
    f.close()




