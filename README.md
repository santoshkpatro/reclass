# Reclass

### Requirements

- PostgreSQL
- NodeJs
- Python3

# Installation

### Post-installation steps

1. Database Setup

```bash
# create a new user reclass as specified in dev env
sudo -u postgres createuser reclass

# get into the psql prompt to do some work
sudo -u postgres psql

# setup password for the user reclass
\password reclass
# when prompted enter `12345` as password

# Let's create development database
create database reclass_development;

# Grant reclass user access to db
grant all privileges on database reclass_development to reclass;

# then quit
\q

```

2. Python Virtualenv setup ( skip if you know how to use python venv)

## Easy installation (Linux/MacOS)

```
./scripts/setup.sh
```

## Manual installation
