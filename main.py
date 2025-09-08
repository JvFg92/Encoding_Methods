import Codify as cd

if __name__ == "__main__":
    message, binary_message = cd.get_data()
    print(f"Your message is: {message}")
    print(f"Binary representation: {binary_message}")
    while True:
        print("\nChoose an encoding scheme:")
        print("1. 2B1Q")
        print("2. 8B6T")
        print("3. 4DPAM5")
        print("4. MLT-3")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '6':
            cd.encode_2b1q(binary_message)
            cd.encode_8b6t(binary_message)
            cd.encode_4dpam5(binary_message)
            cd.encode_mlt3(binary_message)
            break
        
        if choice == '1':
            cd.encode_2b1q(binary_message)
        elif choice == '2':
            cd.encode_8b6t(binary_message)
        elif choice == '3':
            cd.encode_4dpam5(binary_message)
        elif choice == '4':
            cd.encode_mlt3(binary_message)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")