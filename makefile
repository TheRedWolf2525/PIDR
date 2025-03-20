# Nom de l'exécutable
TARGET = program

# Dossiers
SRC_DIR = src
BUILD_DIR = build

# Compilateur et options
CC = gcc
CFLAGS = -Wall -Wextra -O2
LDFLAGS = -lm

# Règle par défaut
all: $(TARGET)

# Compilation de l'exécutable
$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) *.c $(LDFLAGS)

# Création du dossier build si nécessaire
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Nettoyage des fichiers générés
clean:
	rm -rf $(BUILD_DIR) $(TARGET)

# Recompilation complète
rebuild: clean all
