

def abfrage_kmeldung():
    global Vname,Nname, Nname_chef, arbeit, arbeit_strasse, arbeit_postlzahl, arbeit_stadt, geschlecht
    Vname = input("Bitte geben Sie ihren Vornamen ein: ")
    Nname = input("Bitte geben Sie ihre Nachnamen ein: ")
    
    Nname_chef = input("Bitte geben Sie den Nachnamen von ihrem Verantwortlichen/Chef ein: ")
    geschlecht = input("Bitte geben Sie [wenn sie wollen] das Geschlecht von ihrem Verantwortlichen/Chef ein: ")
    arbeit = input("Bitte geben Sie den Namen ihrer Arbeitsstelle an: ")
    arbeit_strasse = input("Bitte geben Sie den Straßennamen ihrer Arbeitsstelle an: ")
    arbeit_postlzahl = input("Bitte geben Sie die Postleitzahl ihrer Arbeistelle an: ")
    arbeit_stadt = input("Bitte geben Sie die Stadt ihrer Arbeitsstelle an: ")
    
    return arbeit,arbeit_strasse,arbeit_postlzahl,arbeit_stadt,Vname,Nname,geschlecht,Nname_chef

def text_kmeldung():
    print(arbeit)
    print(arbeit_strasse)
    print(arbeit_postlzahl+" "+ arbeit_stadt)
    print("\n")
    
    if geschlecht == "Frau" or geschlecht == "frau": 
      print("Sehr geehrte Frau "+Nname_chef+",\n\n")
    else:
        print("Sehr geehrter Herr "+Nname_chef+",\n\n")
          
    print("hiermit möchte ich Sie darüber informieren, dass ich heute aus gesundheitlichen Gründen\nleider nicht auf der Arbeit erscheinen kann. Ich werde schnellstmöglich einen Arzt aufsuchen \nund Sie im Anschluss unverzüglich über die voraussichtliche Dauer meiner Arbeitsunfähigkeit informieren.\n")
    print("\n\n")
    print("Die Arbeitsunfähigkeitsbescheinigung schicke ich Ihnen schnellstmöglich zu,\nsodass diese Ihnen innerhalb der nächsten drei Tage vorliegt.")
    print("\n\n")
    print("Mit freundlichen Grüßen")
    print("\n")
    print(Vname+" "+ Nname) 
    
   