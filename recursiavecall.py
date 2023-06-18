def getRecursiveCall(arrInput, arrT):

    print(f"input: {arrInput} arrT: {arrT}")
    tempToken = arrT.pop(0)    
    for input in arrInput:        
      if len( arrT ) > 0 :
          temp = getRecursiveCall(input.split( tempToken ), arrT)
          return tempToken.join( arrInput) + temp
      else:
          return " ".join([ x for x in tempToken.join(arrInput)])

def main():
    target = "aaXXbbYYccZZ"
    arrT = ["XX", "YY", "ZZ"]   

    # for data in arrT:
    #   arrSplit = target.split(data)
    
    result = getRecursiveCall([target], arrT)
    print(f"result: {result}")
if __name__ == "__main__":
    main()
