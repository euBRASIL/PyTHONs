import flet as ft

def main(pagina: ft.Page):
	pagina.title = "euBRASIL"
	pagina.vertical_alignment =ft.MainAxisAlignment.CENTER

	def subtrair(e):
		print(e)
		caixa_texto.value= str(int(caixa_texto.value)-1)
		pagina.update()
		pass

	def somar(e):
		print(e)
		caixa_texto.value= str(int(caixa_texto.value)+1)
		pagina.update()
		pass
	
	botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=subtrair)
	caixa_texto = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)
	botao_mais  = ft.IconButton(ft.icons.ADD, on_click=somar)

	pagina.add(ft.Row([botao_menos, caixa_texto, botao_mais], alignment=ft.MainAxisAlignment.CENTER))


# Visualizar no Browser : 
# ft.app(target=main, view=ft.WEB_BROWSER)


ft.app(target=main) 