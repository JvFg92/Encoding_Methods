import matplotlib.pyplot as plt

def plot_signal(signal, title):
    plt.figure(figsize=(10, 4))
    plt.step(range(len(signal)), signal, where='post')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Voltage Level')
    plt.ylim(min(signal)-1, max(signal)+1)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_')}.png")  # Save the plot as an image
    plt.close()

def get_data():
  data = input("Enter your message: ")
  qtd = len(data)
  if qtd >= 5:
    print("Message must be no longer than 4 characters. Enter a new message.")
    return get_data()
  else:
      binary_message = ''.join(format(ord(char), '08b') for char in data)
      return data, binary_message

def encode_2b1q(binary_data):
    signal = []
    for i in range(0, len(binary_data), 2):
        dibit = binary_data[i:i+2]
        if dibit == '10':
            signal.append(1)
        elif dibit == '11':
            signal.append(3)
        elif dibit == '01':
            signal.append(-1)
        elif dibit == '00':
            signal.append(-3)
    print(f"2B1Q Signal Levels: {signal}")
    plot_signal(signal, "2B1Q Encoding")

def encode_8b6t(binary_data):
    mapping = {
        '000000': -7, '000001': -5, '000010': -3, '000011': -1,
        '000100': 1, '000101': 3, '000110': 5, '000111': 7,
        '001000': -6, '001001': -4, '001010': -2, '001011': 0,
        '001100': 2, '001101': 4, '001110': 6, '001111': 8,
        '010000': -8, '010001': -7, '010010': -5, '010011': -3,
        '010100': -1, '010101': 1, '010110': 3, '010111': 5,
        '011000': 7, '011001': 8, '011010': 6, '011011': 4,
        '011100': 2, '011101': 0, '011110': -2, '011111': -4,
        '100000': -6, '100001': -8, '100010': -7, '100011': -5,
        '100100': -3, '100101': -1, '100110': 1, '100111': 3,
        '101000': 5, '101001': 7, '101010': 8, '101011': 6,
        '101100': 4, '101101': 2, '101110': 0, '101111': -2,
        '110000': -4, '110001': -6, '110010': -8, '110011': -7,
        '110100': -5, '110101': -3, '110110': -1, '110111': 1,
        '111000': 3, '111001': 5, '111010': 7, '111011': 8,
        '111100': 6, '111101': 4, '111110': 2, '111111': 0
    }
    signal = []
    for i in range(0, len(binary_data), 6):
        sextet = binary_data[i:i+6]
        if sextet in mapping:
            signal.append(mapping[sextet])
        else:
            print(f"Invalid sextet: {sextet}")
            signal.append(0)
    print(f"8B6T Signal Levels: {signal}")
    plot_signal(signal, "8B6T Encoding")

def encode_4dpam5(binary_data):
    mapping = {
        '00': -3, '01': -1, '10': 1, '11': 3
    }
    signal = []
    for i in range(0, len(binary_data), 2):
        dibit = binary_data[i:i+2]
        if dibit in mapping:
            signal.append(mapping[dibit])
        else:
            print(f"Invalid dibit: {dibit}")
            signal.append(0)
    print(f"4DPAM5 Signal Levels: {signal}")
    plot_signal(signal, "4DPAM5 Encoding")

def encode_mlt3(binary_data):
    signal = []
    last_level = 0
    for bit in binary_data:
        if bit == '1':
            if last_level == 0:
                last_level = 1
            elif last_level == 1:
                last_level = -1
            else:
                last_level = 0
        signal.append(last_level)
    print(f"MLT-3 Signal Levels: {signal}")
    plot_signal(signal, "MLT-3 Encoding")

