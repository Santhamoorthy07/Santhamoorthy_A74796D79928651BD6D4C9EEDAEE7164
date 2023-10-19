def Linear_Search_Product(productlist,targetproduct):
  indices=[]

  for index,product in enumerate(productlist):
    if (product==targetproduct):
      indices.append(index)
  return indices

products=["shoes","boat","loafer","shoes","sandal","shoes"]
target1="shoes"
target2="orange"

result1=Linear_Search_Product(products,target1)
print(result1)

result2=Linear_Search_Product(products,target2)
print(result2)