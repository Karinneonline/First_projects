# list of products
produtos = {123: "Camisa estampada", 124: "Camisa social manga longa", 125: "Calca jeans"}

# list of sales
vendas = [(123, 3, 25.55), (124, 2, 79.99), (125, 1, 99.99)]

head_cupom = """
#####################################################
               C U P O M   F I S C A L                  
#####################################################
Item    Codigo  Descricao   
                                Qtd    VL_unit    Vl
-----------------------------------------------------
"""

print(head_cupom)
count = 0
vl_tot = 0

# loop for with the sales and the products with the cost

for i in range(len(vendas)):
    count += 1
    produto = vendas[i][0]
    qtd = vendas[i][1]
    vl_unit = vendas[i][2]
    vl_item = qtd * vl_unit
    vl_tot = vl_tot + vl_item
    print (int(count), "\t", end = "")
    print (vendas[i][0], "\t", end = "")
    print (produtos[produto], "\t", end = "")
    print("")
    print ("\t" * 7, qtd, "un", "x", end = "")
    print (vl_unit, "\t", end = "")
    print ("=", float(qtd * vl_unit))
    print("\n")

# finishes with the total cost
print ("-" * 25)
print ("TOTAL R$       ", end = "")
print (vl_tot)
print ("-" * 25)


