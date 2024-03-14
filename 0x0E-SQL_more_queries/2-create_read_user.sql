# Define database and user
DATABASE="hbtn_0d_2"
USER="user_0d_2"
PASSWORD="user_0d_2_pwd"

# Check if the database exists
EXISTING_DB=$(mysql -uroot -puser_0d_2_pwd -e "SHOW DATABASES LIKE '$DATABASE';")

# Extracting the result from the query output
EXISTING_DB=$(echo "$EXISTING_DB" | tail -n 1)

if [[ $EXISTING_DB == "$DATABASE" ]]; then
    echo "Database '$DATABASE' already exists. Skipping creation."
else
    # Create the database
    mysql -uroot -puser_0d_2_pwd -e "CREATE DATABASE IF NOT EXISTS $DATABASE;"
    echo "Database '$DATABASE' created."
fi

# Check if the user exists
EXISTING_USER=$(mysql -uroot -puser_0d_2_pwd -e "SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = '$USER' AND host = 'localhost');")

# Extracting the result from the query output
EXISTING_USER=$(echo "$EXISTING_USER" | tail -n 1)

if [[ $EXISTING_USER == 1 ]]; then
    echo "User '$USER' already exists. Skipping creation."
else
    # Create the user and grant privileges
    mysql -uroot -puser_0d_2_pwd -e "CREATE USER IF NOT EXISTS '$USER'@'localhost' IDENTIFIED BY '$PASSWORD';"
    mysql -uroot -puser_0d_2_pwd -e "GRANT SELECT ON $DATABASE.* TO '$USER'@'localhost';"
    mysql -uroot -puser_0d_2_pwd -e "FLUSH PRIVILEGES;"
    echo "User '$USER' created with SELECT privilege on database '$DATABASE'."
fi

