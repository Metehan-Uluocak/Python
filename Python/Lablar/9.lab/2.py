def get_file_path(tree, node):
    path = ""
    for parent, children in tree.items():
        if node in children:
            path = get_file_path(tree, parent)
            break
    return path + "/" + node if path or node in tree else f"{node} dosyasi agacta bulunmamaktadir."


folder_tree = {
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}

while True:
    user_input = input("Dosya adını girin (çıkmak için 'q' tuşuna basın): ")
    
    if user_input.lower() == 'q':
        break
    
    file_path = get_file_path(folder_tree, user_input)
    
    print(file_path)
