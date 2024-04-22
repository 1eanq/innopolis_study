def process_operation(operation):
    match operation:
        case "save":
            print("сохранить")
        case "load":
            print("загрузить")
        case _:
            print("неизвестная операция")


op = input()
process_operation(op)
