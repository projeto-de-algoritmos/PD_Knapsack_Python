if __name__ == "__main__":
    print('Digite o Peso Total da Mochila:')
    weight = input()
    
    itemVector = []

    while(True):
        print('Digite o nome do item que deseja levar (Digite 0 para finalizar):')
        itemName = input()
        if(itemName == '0'):
            break
        
        print('Digite o valor do item \'' + itemName.upper() + '\':' )
        itemWeight = input()

        print('Digite o peso do item: \'' + itemName.upper() + '\':' )
        itemValue = input()

        item = (itemName, itemWeight, itemValue)
        itemVector.append(item)

    print(itemVector)

    matrix = [[0 for col in range(weight)] for row in range(len(itemVector))]
    print(matrix)

