<<<<<<< HEAD
def main():
  print("Hello learners!")
=======
import requests
import json
import random


def dish_fetch(num):
    url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.content)

    return {}


def info_dish(dish):
    print("Nombre:", dish.get("name", "No disponible"))
    print("Descripcion:", dish.get("description", "No disponible"))
    print("Ingredientes:", dish.get("ingredients", "No disponibles"))


def main():
  print("Hello learners!")
  while True:
        print("\nMENU DE PLATOS TIPICOS DE COLOMBIA")
        print("1. Mostrar platos tipicos")
        print("2. Buscar un plato por ID")
        print("3. Ver un plato recomendado")
        print("0. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            for num in range(1, 51):
                dish = dish_fetch(num)

                if dish:
                    print(num, "-", dish.get("name", "No disponible"))

        elif opcion == "2":
            try:
                num = int(input("Ingresa el ID del plato: "))
                dish = dish_fetch(num)

                if dish:
                    info_dish(dish)
                else:
                    print("No se encontro el plato.")

            except ValueError:
                print("Debes ingresar un numero entero.")

        elif opcion == "3":
            num = random.randint(1, 50)
            dish = dish_fetch(num)

            if dish:
                print("\nPLATO RECOMENDADO")
                info_dish(dish)
            else:
                print("No se encontro el plato recomendado.")

        elif opcion == "0":
            print("Gracias por visitar nuestro menu colombiano.")
            break

        else:
            print("Opcion no valida.")
>>>>>>> bcfa3e1 ( menú platos tipicos colombianos)

if __name__=="__main__":
  main()