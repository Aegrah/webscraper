import random
from collections import OrderedDict

headers_list = [
{
    'authority': 'www.funda.nl',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.funda.nl/',
    'accept-language': 'en-GB,en;q=0.9'
},
{
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'nl,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
},
{
    'authority': 'www.funda.nl',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4813.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.funda.nl/',
    'accept-language': 'en-US,en;q=0.9'
},
{
    'authority': 'www.funda.nl',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.funda.nl/',
    'accept-language': 'en-US,en;q=0.9'
},
{
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'TE': 'trailers'
},
{
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
},
]

cookies = {
    'SNLBCORS': 'c2b8961779970dfaf053e9c73f5c945c',
    'SNLB': 'c2b8961779970dfaf053e9c73f5c945c',
    '.ASPXANONYMOUS': '3HjIVscWzX0kdnZlKj854tzOy4ifZtiHnldUFou93PzslpSouk1NuJeZpVtCGORdrbppq-RdNU1d7rRypIlifJttYP_Tvs9kLtA-igrCbwPM-NXpRN9J_bAlhXsbi-_IM1P6wcEVTLdXi4PfAnqWbp82_cs1',
    'sr': '0%7cfalse',
    'lzo': 'koop=%2fkoop%2fmaastricht%2f0-300000%2f',
    'html-classes': 'js',
    '_gid': 'GA1.2.587377365.1641569874',
    'ak_bmsc': '84FFB12E9BAFCF02D6A9A633D2B77620~000000000000000000000000000000~YAAQLU17XCk40TN+AQAAqXYwNQ4wcCWtKjiQsC6EtDxK/YeTjr2MvuAvnZe4M09n1wc66qnvfomycYX5lpzBqFAxpm02yRc9RubDlxVW6tiTAfV6xrOWXMSKyKbrnAsxdMECkxVSBfpurEffNGhVuAuUNcUmj5EyOwKRuoiHL9S/djDRyBvv+7BTskkIsDf60uVwGV7rxbUTQ2bOsifbOl6Vtz1HDg46ozk5OigxCscMF9mc4/Zt/40rwFMU2D4pMPqA6Ru0uwfnR0JLIB0S8+dqsTYbhlCGUiODNqp3aLHzffQhdkCPPWoAJ3rGrq7VYxcP5SHlEJcMXPqdFOTV5F1xWFqb6/3Tot7kcDZwDz7TYPSkfnBgRXYNtc7IMtxpUv8LgSRJ6WyxmWrflxy/qOBauFQ8kvTKqvoykYUQlSp21pmykY1L0kBYW0zLJLxT1XKJTa0y40eXmLY8SxMlQISgrNNu6vYkF2PooloA+u8qvIT+XwoPT4UlW6Qt+01fmWS3xCUndI3KNPaK8ipZ6NzdIF4ddoGpjWhl',
    'OptanonAlertBoxClosed': '2022-01-07T15:37:55.211Z',
    'eupubconsent-v2': 'CPSc68uPSc68uAcABBENB9CgAPLAAAAAAChQILtF7S5dRGPCWG58ZtskOQQPoNSMJgQjABaJImgJwAKAMIQCkmASPATgBAACCAYAKAIBAAFkGAAAAQAAQAAAAAGEQAAABAIIICIAgBIBCAAIAAQAAIAQQAAAgEACAEAAkgAAAIIAQEAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH9uAAAA8JAcAAQAAsACoAGQAOAAeABAADIAGgAPAAiABMACeAFUALAAbwBHACXAGGANUAfoBHACUgGKATEAuQBeYDJAgAgAB4AHwAWgB_AGaAQMBHoCVgwAQABYAbwCWgHUDQAwAuQFoAWkBcggAGAAsAN4BLREAEBcgoBmAA0AB8AGAAZABEACwAGIAPwAmABcgC8AL8AYQBiADaAHiAP4BBACFAEcAJMAUAAqABWgCyAGbANQA1YBxAHIAPMAjgBJoCWgJdATwBPQCkAFfgLQAtIBdwDAgGKgM4AzoBoADTgHCgP0A_YCBAEegJBATEAncBRACmwFmALkAXmAvkYAqAAfABgAGQARAAsABiAD8AJgAXoAwgDEAG2AP4BBACOAEmAKAAVAArQBZADHAGpAOIA5AB5gEcAJbATwBPQCkAFfALuAYqAzgDOgGggNMA04BwgD9gIEAR6AkEBMQCdwFEAKbAWYAvMcAVAAQAA8AC4AHwAWgA5AB-AGgAP4AzQCBgEIAIiAS2AwADAgGvAR6AlYBMQCpgF9DoFAACwAKgAZAA4ACCAGIAZAA0AB4AD4AIgATAAngBVACwAFwAL4AYgA3gCOgEuATAAsQBhgDKAGiAN8AfoBFgCOAEpgLQAtIBdQDFAHUAReAkEBVgC2QFyALzAZIQAegABAAQAAsABoADwAMgAiABYADEAH8ATABNACqAFyALwAvwBhAGIANAAbQA3wB_AIEARYAjgBJgCgAFQAK2AWIBZADNgGoAaoA3wBxADkAHmARwAlIBOACeAFIAKyAV-AtAC0gF3AMAAYqAzgDOgGggNMA04BwgDqQH6AfsBAACBAEegJBATEAncBRACmwFmALZAXIAvklAWAAQAAsADIAHAAYgA8ACIAEwAKoAXAAvgBiADaAI4AaoBHIC0ALSAXUAxQB1AEXgLzJACQALgA5ADeAL4AagBLQDXgJWAXsUgNgALAAqABkADgAIIAYgBkADQAHgARAAmABPACqAFgAL4AYgBYgDKAGiANUAfoBFgCOAEpAReAuQBeYDJCgBMAC4AHwAWgA5AB-AG0AN4AjgBqADXAJaAXUAwABigDXgI9ATEAqYBfQAA.flgAAAAAAAAA',
    'fcvc': '2749lEzl/4aTiNTXvRasIORD6M+1qzOHXSECECyKSpyl381xIfOqGOS1qsjdsDH1YVu',
    'objectnotfound': 'objectnotfound=false',
    '_pbjs_userid_consent_data': '1888430226457592',
    'PubCommonId': 'f2582ffd-9250-4322-9b07-3ea11befa0b0',
    'optimizelyEndUserId': 'oeu1641569892537r0.656993498422086',
    'ajs_anonymous_id': '%2278dcc562-0d7b-4c1b-a92c-2be353048e89%22',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    'fd-user-checked': 'true',
    'id5id': '%7B%22created_at%22%3A%222022-01-07T15%3A38%3A19.766096Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5*1d0Y_UqdWyev99bt2MjSO8eiqsTy3SEMM1I380CjNi4EEMqNLrI_H9lgGN1uZoTFBBEE1IeV1Z13pcfTEtCrjAQS0B_4dUaO3O2J2MVZ8UYEEwW9W5WRnhqz3NHE0iTeBBTY_E3ArKIvL2jdQS4eCwQVRJ7lq8eUl9AGB0f8wr4EFmOjyBt8ovvRUR2mYiBTBBetwQUa32JcdizH7TUPDwQYSWKEgC5u0esafBPeXbIEGbMQdKeJt98WzHONos_jBBrJtd7V56i26QiZfGo8qwQb74rfbKi31yicyvPiOqkEHD-jZjOmo7O6oDZg8KIWBB0rZlChmYZtR92fvQuPzAQe04GrM-gIcO8WHB-6fF8EH-PAZf3lVoQ_5GO99MMrBCDtA8MUAvJr25_sBOyn0QQhe1kAmndwc5huzysQuigEIrs6L7CXLiCanWKsH7g7BCMo2CcJnL_MJzmeZDFKrQQkO8LWxipTKbPCSViCvOMEJWp7gNsoMnRAX9IZtEoaBCa9tage6DPlYH-eLq-uag%22%2C%22universal_uid%22%3A%22ID5*9-Ro-0E8t7O_GdOK_WuGnmGJEfoG3cq6-RgsxRFLeCoEEAJ6I3gY2XGfm2TOYCyDBBHJdzP0wKSuWvLhb_RnqQQSSkgrjxYkGrP2QtQmg3QEE_alfEcbJ_Q06tBLWj0-BBQxgjJ1fCWTs8gMejotegQVGceL4mwh3vZ43ty_v-oEFnR6CYc2OBFldqavf18NBBeOlevKpOuJrherTvQjPwQY9KlhffhSy_cNlnGWCB4EGWFB3FDwQtiGbmXt_yWdBBohdDBYWN5khj6pV1xCWwQbSMAluQIrti3xntPG3O0EHD2HzQIUZMOvY7j3IOmmBB3shh77XqJkgNYyHgJjxgQejrPVZD6UFhYXL_wEOJoEH24Cqa4zxzkm8qmW9NpTBCAtVYGKTpBVKoGdR7QvQQQh8ijQ5OBceW6EQqOVDRoEIuc7gaYi5yhAAFRhQRdZBCM6DJ5DGuC06YdVNJqYGAQksH10afSoIW-hirBCIe8EJZgga1WtPfMLrtIUaz9uBCbdNUFpYYPdLkEBSeKilA%22%2C%22signature%22%3A%22ID5_AcqkkTvYXXeg_8PDHqBDQu5m_j2C3frahOOGwdH0-Dmaqh3_6jIYR-6qBl-Jfvd1E5aKEShBs4hrai-L_mY2TnU%22%2C%22link_type%22%3A1%2C%22cascade_needed%22%3Atrue%2C%22privacy%22%3A%7B%22jurisdiction%22%3A%22gdpr%22%2C%22id5_consent%22%3Atrue%7D%7D',
    'pbjs-unifiedid': '%7B%22TDID%22%3A%2230fe2806-b732-49a4-91b1-b5bbb5a6e627%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222022-01-07T15%3A38%3A19%22%7D',
    'panoramaId_expiry': '1641656299754',
    '_cc_id': 'd8f867366def30de3109a80a71d7b7e',
    '__gads': 'ID=d5465b100d8b48a5-2299e8ab18cd002b:T=1641569899:S=ALNI_MbZOU7B2VrI84LqKwmM0FrWMHtlKA',
    '_gcl_au': '1.1.882314388.1641569900',
    'sessionstarted': 'true',
    '__RequestVerificationToken': '5B4eBhFYJ3iaJbpQ7fKTJ_5Wf688Wv3ORQPmnayut8R7GgJvXrhKOgVZsax766SZvnhDpCSLDACA_TnVX-LDShWjCqY1',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Jan+07+2022+16%3A38%3A49+GMT%2B0100+(Central+European+Standard+Time)&version=6.22.0&consentId=a92d31ff-8081-4725-9494-d92e43df314f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CF01%3A1%2CF02%3A1%2CF03%3A1%2CBG30%3A1%2CF04%3A1%2CC0004%3A1%2CF05%3A1%2CBG29%3A1%2CSTACK39%3A1&hosts=H41%3A1%2CH42%3A1%2CH44%3A1%2CH45%3A1%2CH5%3A1%2CH18%3A1%2CH21%3A1%2CH1%3A1%2CH37%3A1%2CH6%3A1%2CH38%3A1%2CH7%3A1%2CH35%3A1%2CH10%3A1%2CH34%3A1%2CH39%3A1%2CH43%3A1%2CH9%3A1%2CH11%3A1%2CH2%3A1%2CH12%3A1%2CH15%3A1%2CH40%3A1%2CH16%3A1%2CH17%3A1&geolocation=NL%3BNH&AwaitingReconsent=false',
    '_ga_WLRNSHBY8J': 'GS1.1.1641569873.1.1.1641569929.0',
    '_ga': 'GA1.2.2044504201.1641569873',
    'cto_bidid': '-vlkul9vY2hHZ2ZybyUyQnZyZTdsWTJzWHJ0TkdPQXF6QjIzTTNUd1psQnZ2ZmtQVm4xM0o0VnJFb1BkUmNOS3NhaDhyd3lLTTNJZ0U5SU4yUlhiJTJGNFJZeHliTVElM0QlM0Q',
    'cto_bundle': 'H4v6Ll9Vb1k4aGlwbm9QOUcyWG1XNFZkaXdjZVVqZkVpb1BhV3NFWFlaV1BYeHh5ak1hOTF5SG43cUhNTjFwbGcybU5XQlZGUkFKZ0dwaXUzbVQlMkJHMGxUMGxHWSUyRlVtNzhRY1klMkY1T0o1aEVobG5uMEVLUU03TWVHWE45UjVrNmQ3VnRZVQ',
    '_dd_s': 'logs=1&id=2aa0e7f3-9ae4-49cd-9071-d94acc42d9fd&created=1641569873490&expire=1641571008830',
}

ordered_headers_list = []
for headers in headers_list:
    h = OrderedDict()

for header, value in headers.items():
    h[header] = value
    ordered_headers_list.append(h)

for i in range(0,10):
    headers = random.choice(headers_list)
