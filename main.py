import app

def main():
    print("="*48,
        "\nThis project demonstrates how Python can automate tasks in excel.\n",
        "="*48)

    file_input = input("Input file name:\n> ")

    file_output = input("Where do you want to store the changes?\n> ")

    app.process_workbook(file_input, file_output)

if __name__ =='__main__':
    main()