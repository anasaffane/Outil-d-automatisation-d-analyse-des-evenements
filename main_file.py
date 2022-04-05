import brand_monit
import config
import dns_option
import file_sandbox
import phishing_analysis
import reputation_check
import sanitize
import time
import url_decoding

def main_switch(selected_option):
    if selected_option == 0 :
        exit()
    if selected_option == 1 :
        reputation_check.input_validate()
    if selected_option == 2 :
        dns_option.menu()
    if selected_option == 3 :
        phishing_analysis.menu()
    if selected_option == 4 :
        url_decoding.menu()
    if selected_option == 5 :
        file_sandbox.file_sandbox()
    if selected_option == 6 :
        sanitize.menu()
    if selected_option == 7 :
        brand_monit.menu()
    if selected_option == 8 :
        config.menu()

if __name__ == '__main__' :
    print("\n")

    print("OUTIL D'AUTOMATISATION DE L'ANALYSE DES ÉVÉNEMENTS DE SÉCURITÉ\n")

    time.sleep(1)
    while True:
        try:
            config.fetch_api_key()
        except:
            config.menu()
            config.fetch_api_key()
            
        print("\n Merci de choisir une parmis les options suivant : ")
        print("OPTION 1: Reputation/Blocklist Check (IPs, Domains, URLs, Hashes)")
        print("OPTION 2: DNS/WHOIS Lookup Options")
        print("OPTION 3: Email Security (Phishing Email Analysis)")
        print("OPTION 4: URL Decoding for Investigation")
        print("OPTION 5: File Upload for Sandboxing")
        print("OPTION 6: Sanitization of IOCs for email")
        print("OPTION 7: Brand Monitoring & Analysis")
        print("OPTION 8: Help & Configuration/Re-configuration")
        print("OPTION 0: Exit Tool")
        
        selected_option=int(input())
        if 0 <= selected_option < 9:
            main_switch(selected_option)
        else :
            print("Merci de choisir l'option correct")

