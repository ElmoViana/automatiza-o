from playwright.sync_api import sync_playwright
#import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    # abrir o navegador e concedendo as permissões e localização
    pagina = navegador.new_page()
    # navegar para uma página
    pagina.goto("https://www.bet365.bet.br/#/HO/")
    # pegar informações da pagina
    print(pagina.title())
    # selecionar um elemento na tela
    pagina.get_by_text('Login').nth(1).click()
    #selecionar varios elementos na tela
    
    #preenchimento de formulario
    pagina.get_by_role("textbox", name="Usuário ou endereço de e-mail").click()
    pagina.get_by_role("textbox", name="Usuário ou endereço de e-mail").press("elmobill", delay=150 #Atraso de 150ms entre cada letra
                                                                              )
    pagina.get_by_role("textbox", name="Senha").click()
    pagina.get_by_role("textbox", name="Senha").press("TainaMonica1213.", delay=120 #Atraso de 120ms entre cada letra
                                                      )
    pagina.get_by_text("Login", exact=True).first.click()
    #pagina.get_by_role("button", name="Aceitar todos").click()
    #pagina.get_by_text("Ao-Vivo", exact=True).click()
    #navegando para pagina de aposta ao-vivo
    
    
   # time.sleep(15)
    pagina.pause()