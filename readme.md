# Database and tbales on my mysql
## Master
```sql
CREATE SCHEMA `master` ;

CREATE TABLE `master`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idusers_UNIQUE` (`id` ASC) VISIBLE);
```

## Slave
```sql
CREATE SCHEMA `slave` ;

CREATE TABLE `slave`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `idusers_UNIQUE` (`id` ASC) VISIBLE);
```


# Adapte for your environment
Change values:
```python
host: str = 'localhost',
user: str = 'root',
password: str = '1234567',
database: str = 'slave | master',
```
on [master file](https://github.com/Computer-Science-Course/master-user-simulation/blob/main/simulator/models/database/master.py) and [slave file](https://github.com/Computer-Science-Course/master-user-simulation/blob/main/simulator/models/database/slave.py) to adapt to your environment.

# Create Virtual environmen
```bash
python -m venv .venv
```

# Activate Virtual environment
```bash
source .venv/bin/activate
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Run the app
```bash
python simulator
```