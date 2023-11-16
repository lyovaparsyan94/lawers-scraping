import g4f

# g4f.debug.logging = True  # Enable logging
# g4f.check_version = False  # Disable automatic version checking
# print(g4f.version)  # Check version
# print(g4f.Provider.Ails.params)  # Supported args

# Automatic selection of provider
# r = "Австралия является одной из самых развитых стран , будучи четырнадцатой по размеру экономикой в мире, и имеет девятое место в мире по ВВП в расчёте на душу населения. Военные расходы Австралии являются двенадцатыми по размеру в мире. С пятым по величине индексом человеческого развития Австралия занимает высокое место во многих сферах, таких как качество жизни, здоровье, образование, экономическая свобода, защита гражданских свобод и политических прав[14]. Австралия является членом G20, ОЭСР, ВТО, АТЭС, ООН, Содружества наций, АНЗЮСа, АУКУСа и Форума тихоокеанских островов."
# my_json = 'Rebecca H. Miller s Education: George Washington University of Law (J.D., cum laude, 2000) Oglethorpe University (B.A., magna cum laude, 1997) contact her +4-555-123-4567 and email email@mail.ru'
html = "my_json=\"\"\"<divclass=\"row\"id=\"member-+15852826975link\"><divclass=\"col-12col-lg-6\"><divclass=\"field\"><iclass=\"fasfa-phone\"></i><ahref=\"tel:%2B234-1-2806989\">+234-1-2806989</a></div><divclass=\"field\"><iclass=\"fasfa-phone\"></i><ahref=\"tel:%2B234-1-4626841%2F3\">+234-1-4626841/3</a></div><divclass=\"field\"><iclass=\"fasfa-fax\"></i><ahref=\"tel:%2B234-1-2716889\">+234-1-2716889</a></div><divclass=\"field\"><iclass=\"fasfa-envelope\"></i><ahref=\"mailto:chinwe.ogban@jee.africa\">chinwe.ogban@jee.africa</a></div><divclass=\"field\"><iclass=\"fasfa-globe\"></i><ahref=\"https://jee.africa/ogban/\">VisitWebsite</a></div></div><divclass=\"col-12col-lg-6\"><divclass=\"fieldcompany-address\"><articledata-history-node-id=\"4968\"class=\"nodecompany-branch-teaserclearfix\"><divclass=\"fieldfield--name-field-companyfield--type-entity-referencefield--label-visually_hidden\"><divclass=\"field__labelvisually-hidden\">ParentCompany</div><divclass=\"field__item\">Jackson,EttiandEdu</div></div><divclass=\"fieldfield--name-field-addressfield--type-addressfield--label-hiddenfield__item\"><pclass=\"address\"translate=\"no\"><spanclass=\"organization\">Jackson,EttiandEdu</span><br><spanclass=\"address-line1\">RCOCourt</span><br><spanclass=\"address-line2\">No3-5SinariDaranijoStreet,offAjoseAdeogun</span><br><spanclass=\"locality\">VictoriaIsland,Lagos</span><br><spanclass=\"country\">Nigeria</span></p></div></article></div></div></div>\"\"\""

# Streamed completion
response = g4f.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": f"using regex find and give me email or phone in text or html doc {html} GIVE ONLY phone and email not other info"}],
  stream=True,
)
# return str(response)
for message in response:
  print(message, flush=True, end='')

# Normal response

# def ask_gpt(promt: str) -> str:
#     response = g4f.ChatCompletion.create(
#         model=g4f.models.gpt_4,
#         messages=[{"role": "user", "content": promt}],
#     )
#
#     return response


# print(ask_gpt(f"find all values from  : {r}"))
