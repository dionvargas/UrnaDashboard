# Resolve problemas de atualizações
sudo apt update
apt --fix-broken install

# Atualizando o sistema
sudo apt update && sudo apt upgrade -y

# Instalando o wget
sudo apt install wget -y

# Instalando o MySQL
sudo apt install mariadb-server
## USAR user 'root' e senha '123456'
sudo mysql_secure_installation

# Instalando pacotes do Python
pip install pygame --break-system-packages
pip install flask --break-system-packages
pip install mysql-connector-python --break-system-packages
pip install matplotlib --break-system-packages
pip install numpy --break-system-packages
pip install pillow --break-system-packages
