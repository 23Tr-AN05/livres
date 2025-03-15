from bs4 import BeautifulSoup

# Fonction pour ajouter plusieurs lignes à un tableau spécifique
def add_multiple_rows_to_table(html_file):
    # Ouvrir le fichier HTML et le lire
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    
    # Trouver tous les tableaux dans le fichier
    tables = soup.find_all('table')
    
    if tables:
        print(f"\nIl y a {len(tables)} tableau(x) dans le fichier.")
        
        # Afficher les tables trouvées et demander à l'utilisateur de choisir un tableau
        for idx, table in enumerate(tables):
            print(f"{idx + 1}. Tableau {idx + 1}")
        
        try:
            table_choice = int(input("Sélectionnez le tableau auquel vous souhaitez ajouter des lignes (entrez le numéro) : ")) - 1
            if table_choice < 0 or table_choice >= len(tables):
                print("Numéro de tableau invalide.")
                return
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return

        # Sélectionner le tableau choisi
        selected_table = tables[table_choice]
        
        # Noms des colonnes du tableau (supposons qu'elles soient les mêmes pour tous les tableaux)
        column_names = [th.get_text() for th in selected_table.find_all('th')]

        # Demander combien de lignes l'utilisateur souhaite ajouter
        try:
            num_rows = int(input("Combien de lignes souhaitez-vous ajouter ? "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return

        # Ajouter les lignes
        for row in range(num_rows):
            print(f"\nAjout de la ligne {row + 1} :")
            new_row_data = []
            
            # Demander à l'utilisateur de saisir les valeurs pour chaque colonne
            for column_name in column_names:  # Pour chaque nom de colonne
                value = input(f"Entrez la valeur pour la colonne '{column_name}': ")
                new_row_data.append(value)
            
            # Créer une nouvelle ligne <tr>
            new_row = soup.new_tag('tr')
            
            # Ajouter un espace avant chaque <td> (pour le code source HTML)
            for data in new_row_data:
                # Ajouter un espace avant chaque cellule <td>
                new_row.append(soup.new_string("\n    "))  # Ajout d'un espace pour l'indentation
                
                new_cell = soup.new_tag('td')
                new_cell.string = data
                new_row.append(new_cell)

            # Ajouter la ligne au tableau sélectionné
            selected_table.append(new_row)
            
            # Ajouter un retour à la ligne après chaque </tr> pour la lisibilité
            selected_table.append(soup.new_string("\n"))

        # Sauvegarder les modifications dans le fichier HTML
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"{num_rows} lignes ajoutées avec succès au tableau {table_choice + 1} !")
    else:
        print("Aucun tableau trouvé dans le fichier HTML.")

# Exemple d'utilisation
html_file = 'README.md'  # Nom du fichier HTML

# Ajouter plusieurs lignes au tableau en demandant les valeurs à l'utilisateur
add_multiple_rows_to_table(html_file)
