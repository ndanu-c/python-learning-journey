shoppinglist = ["Banana", "Orange", "Apple", "Mango", "Lemon"];
print(shoppinglist);
print(shoppinglist[0]);
print(shoppinglist[-1])
print(len(shoppinglist))

shoppinglist.append("Avocado");
shoppinglist.insert(2, "Pineapple");
shoppinglist.extend(["Watermelon", "Grapes"]);
print(shoppinglist);

shoppinglist.remove("Mango");
shoppinglist.pop(0)
print(shoppinglist);

shoppinglist = ["Banana", "Orange", "Apple", "Mango", "Lemon"];
shoppinglist[2] = "Pineapple";
shoppinglist[4] = "Watermelon";
print(shoppinglist)

shoppinglist = ["Banana", "Orange", "Apple", "Mango", "Lemon"];
del shoppinglist[1];
print(shoppinglist);

shoppinglist = ["Banana", "Orange", "Apple", "Mango", "Lemon"];
shoppinglist.clear();
print(shoppinglist)

shoppinglist = ["Banana", "Orange", "Apple", "Mango", "Lemon"];
shoppinglist.sort()
print(shoppinglist);

shoppinglist = ["Banana", "Orange", "Apple", "Mango", "Lemon"];
shoppinglist.sort(reverse=True);
print(shoppinglist);