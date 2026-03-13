def add_product(inventory, name, qty, price):
    if qty <= 0 or price <= 0:
        print("Cantidad y precio deben ser positivos.")
        return False
    if name in inventory:
        print("Producto ya existe.")
        return False
    inventory[name] = {'quantity': qty, 'price': price}
    print("Producto agregado.")
    return True

def view_inventory(inventory):
    if not inventory:
        print("Inventario vacío.")
        return
    total_general = 0
    for name, data in inventory.items():
        qty = data['quantity']
        price = data['price']
        total = qty * price
        total_general += total
        print(f"Producto: {name}, Cantidad: {qty}, Precio: {price}, Total: {total}")
    print(f"Total general: {total_general}")

def search_product(inventory, name):
    if name in inventory:
        data = inventory[name]
        qty = data['quantity']
        price = data['price']
        total = qty * price
        print(f"Producto: {name}, Cantidad: {qty}, Precio: {price}, Total: {total}")
    else:
        print("Producto no encontrado.")

def update_quantity(inventory, name, new_qty):
    if new_qty <= 0:
        print("Cantidad debe ser positiva.")
        return False
    if name in inventory:
        inventory[name]['quantity'] = new_qty
        print("Cantidad actualizada.")
        return True
    else:
        print("Producto no encontrado.")
        return False

def delete_product(inventory, name):
    if name in inventory:
        del inventory[name]
        print("Producto eliminado.")
        return True
    else:
        print("Producto no encontrado.")
        return False

def main():
    inventory = {}
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            name = input("Nombre del producto: ")
            try:
                qty = int(input("Cantidad: "))
                price = float(input("Precio: "))
                add_product(inventory, name, qty, price)
            except ValueError:
                print("Entrada inválida.")
        elif opcion == '2':
            view_inventory(inventory)
        elif opcion == '3':
            name = input("Nombre del producto a buscar: ")
            search_product(inventory, name)
        elif opcion == '4':
            name = input("Nombre del producto: ")
            try:
                new_qty = int(input("Nueva cantidad: "))
                update_quantity(inventory, name, new_qty)
            except ValueError:
                print("Entrada inválida.")
        elif opcion == '5':
            name = input("Nombre del producto a eliminar: ")
            delete_product(inventory, name)
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
