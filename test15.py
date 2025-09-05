from playwright.sync_api import sync_playwright, expect
import time
import random
import re

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context(
        permissions=["geolocation"], 
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.155 Safari/537.36"
    )
    pagina = contexto.new_page()

    url_correta = "https://www.bet365.bet.br/#/HO/"
    print(f"Acessando o site: {url_correta}")
    pagina.goto(url_correta, timeout=60000)

    try:
        print("Procurando e clicando no botão de aceitar cookies...")
        pagina.get_by_role("button", name="Aceitar").click(timeout=10000)
        print("Cookies aceitos.")
    except Exception:
        print("Botão de cookies não encontrado, continuando...")

    print("Clicando no botão de Login principal...")
    try:
        expect(pagina.get_by_text('Login').nth(1)).to_be_visible(timeout=60000)
        pagina.get_by_text('Login').nth(1).click()
        print("Botão de login correto foi clicado.")
    except Exception as e:
        print(f"Não foi possível clicar no botão de Login. Erro: {e}")
        pagina.screenshot(path="erro_screenshot.png")
        navegador.close()
        exit()

    try:
        print("Aguardando o formulário de login aparecer...")
        form_login = pagina.locator(".lms-StandardLogin")
        expect(form_login).to_be_visible(timeout=15000)
        print("Formulário visível.")

        campo_usuario = pagina.get_by_placeholder("Usuário ou endereço de e-mail")
        expect(campo_usuario).to_be_editable(timeout=10000)
        usuario = "COLOCAR SEU USUÁRIO AQUI"
        print(f"Digitando usuário: {usuario}")
        campo_usuario.type(usuario, delay=random.randint(100, 250)) 

        time.sleep(random.uniform(0.5, 1.2))

        campo_senha = pagina.get_by_placeholder("Senha")
        expect(campo_senha).to_be_editable(timeout=10000)
        senha = "COLOCAR SUA SENHA AQUI"
        print("Digitando senha...")
        campo_senha.type(senha, delay=random.randint(120, 300)) 
        
        print("Finalizando o login...")
        pagina.get_by_text("Login", exact=True).first.click()

        print("Aguardando confirmação do login...")
        expect(pagina.locator('.hm-MainHeaderRHSLoggedIn')).to_be_visible(timeout=20000)
        print("Login efetuado com sucesso!")
        
        pausa_humana = random.uniform(1.5, 3.0)
        print(f"Pausando por {pausa_humana:.2f} segundos antes de clicar...")
        time.sleep(pausa_humana)
        
        print("Procurando e clicando em 'Ao-Vivo'...")
        link_ao_vivo = pagina.get_by_text("Ao-Vivo", exact=True)
        expect(link_ao_vivo).to_be_enabled(timeout=10000)
        link_ao_vivo.click()

        print("Aguardando a URL ser atualizada para a seção Ao-Vivo...")
        expect(pagina).to_have_url(
            re.compile(r".*#/IP/.*"), timeout=15000
        )
        print("URL atualizada com sucesso!")
        
        print("\n\033[92m>>> Automação concluída com sucesso! <<<\033[0m")
        input("O navegador permanecerá aberto. Pressione Enter no terminal para fechar.")

    except Exception as e:
        print(f"\033[91mERRO durante a automação: {e}\033[0m")
        pagina.screenshot(path="erro_automacao.png")
        print("Uma screenshot do erro foi salva como 'erro_automacao.png'")
        input("Pressione Enter para fechar...")