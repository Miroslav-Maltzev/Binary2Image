file_name = input("Введите имя файла\n-->")

if file_name[-4:] != ".txt":
    file_name += ".txt"


bin_file = open(file_name, "r")
bin_text = bin_file.read()

#textWithoutSpace - camelCase
#TextWithoutSpace - PascalCase

bin_text = bin_text.strip()
list = bin_text.split(' ')
bytes_array = bytearray(len(list))

def bin_encoder(bin_text, bytes_array):
    #decoded_text = ''
    bin_text = bin_text.strip()
    for i in bin_text.split(' '):
        #decoded_text += str(int(i, 2))
        print(int(i,2))
        bytes_array.append(int(i, 2))

    return bytes_array

result = bin_encoder(bin_text, bytes_array)

# file = open("result_txt.txt", "w")
# file.write(result)
# file.close()

file = open("result.txt", "wb")

byteObject = bytes(result)
#print(result)
#print(byteObject)

file.write(byteObject)
file.close()