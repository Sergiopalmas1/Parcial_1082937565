def has_min_length(contraseña):
    return len(contraseña) >= 8

def has_max_length(contraseña):
    return len(contraseña) <= 20

def has_uppercase(contraseña):
    return any(c.isupper() for c in contraseña)

def has_lowercase(contraseña):
    return any(c.islower() for c in contraseña)

def has_digit(contraseña):
    return any(c.isdigit() for c in contraseña)

def has_special(contraseña):
    return any(c in '!@#$%^&*' for c in contraseña)

def validar_contraseña(contraseña):
    return (has_min_length(contraseña) and
            has_max_length(contraseña) and
            has_uppercase(contraseña) and
            has_lowercase(contraseña) and
            has_digit(contraseña) and
            has_special(contraseña))

def get_missing_criteria(contraseña):
    missing = []
    if not has_min_length(contraseña):
        missing.append("Mínimo 8 caracteres")
    if not has_max_length(contraseña):
        missing.append("Máximo 20 caracteres")
    if not has_uppercase(contraseña):
        missing.append("Al menos una mayúscula")
    if not has_lowercase(contraseña):
        missing.append("Al menos una minúscula")
    if not has_digit(contraseña):
        missing.append("Al menos un número")
    if not has_special(contraseña):
        missing.append("Al menos un carácter especial: !@#$%^&*")
    return missing

if __name__ == "__main__":
    while True:
        contraseña = input("Ingresa una contraseña: ")
        if validar_contraseña(contraseña):
            print("Contraseña válida.")
            break
        else:
            missing = get_missing_criteria(contraseña)
            print("Contraseña inválida. Le falta:")
            for item in missing:
                print(f"- {item}")
