my_string = "O rato roeu a roupa do rei de Roma"

my_list = my_string.split('r')
print(my_list)

# FAZENDO BUSCA NA STRING
search = my_string.find("rei")
print(my_string[search:])

# SUBSTITUIR VALORES POR OUTROS
my_string = my_string.replace("o rei", "a rainha")
print(my_string)