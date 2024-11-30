from Car import Car
from classes.Brand import Brand

def create_car(cars):
    print("\x1b[2J\x1b[1;1H")
    model = str(input("Informe o modelo do veículo"))
    year = int(input("Informe o ano do veiculo"))
    color = str(input("Informe a cor do veiculo"))
    name = str(input("Informe o nome do veiculo"))

    brand = Brand("VolksWagen", "O carro com rodas")
    car = Car(brand, model, year, color, name)
    cars.append(car)
    print(f"Car {car} added to the list")

def show_cars(cars):
    print("\x1b[2J\x1b[1;1H")
    if len(cars) == 0:
        print("Nenhum veiculo cadastrado")
        return

    for car in cars:
        print(car)

def start_system():
    cars = []
    while True:
        print("\x1b[2J\x1b[1;1H")
        print("=== Welcome ===")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos cadastrados")

        option = int(input("Informe a opção desejada"))
        match option:
            case 1:
                create_car(cars)
            case 2:
                show_cars(cars)
            case 3:
                print("Encerrando...")
                break
            case _:
                print("Funcão inválida")

print("\x1b[2J\x1b[1;1H")
start_system()


