import flet as ft
import random 

#funcion principal
def main(page: ft.Page):
    
    global numero_Secreto,entrada_numero,texto_resultado,boton_adivinar
    

    page.title = "Adivina el numero"
    
    #generar un numero aleatorio
    numero_Secreto = random.randint(1,100)
    
    #Crear los elementos de la interfaz
    titulo=ft.Text("Adivina el numero secreto entre el 1 y 100",size= 20,color="white")
    entrada_numero=ft.TextField(label="Tu Adivinaza",width=150)
    boton_adivinar=ft.ElevatedButton("adivinar")
    texto_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="black",
        width=page.window.width,
        height=page.window.height,
        padding=20
        
        
    )
    page.add(contenedor_principal)
    

ft.app(main)

