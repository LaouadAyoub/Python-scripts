import xml.etree.ElementTree as ET
import subprocess
import os

# Chargement du fichier XML
fileXml = ""
tree = ET.parse('file.xml')
root = tree.getroot()

# Initialisation de la liste de packages
packages = []

# Boucle sur les éléments "package"
for package in root.findall('package'):
    # Ajout de l'attribut "id" de l'élément à la liste de packages
    packages.append(package.get('id'))
print(packages)
# Boucle sur la liste de packages
path = "C:\src\YAMA\EIT.SystemesExternes.Prestations\EIT.SystemesExternes.Prestations.Infrastructure.WebApplication"
# Changer de répertoire courant
os.chdir(path)

package1 = "Ayoub"
cmd = f"dotnet add package {package1}"
print(cmd)


for package in packages:
    # Commande pour installer chaque package via NuGet
    cmd = f"dotnet add package {package}"
    # Exécution de la commande
    subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Package {package} installed successfully")



