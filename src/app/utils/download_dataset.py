import os
import kagglehub
import shutil

def download_ratings_electronics():
    # Carpeta y nombres de archivo
    base_dir = os.path.join("data", "amazon-products-reviews")
    original_file_name = "ratings_Electronics (1).csv"
    desired_file_name = "ratings_electronics.csv"
    file_path = os.path.join(base_dir, desired_file_name)

    # Si el archivo ya existe
    if os.path.exists(file_path):
        print(f"El archivo ya está disponible en: {file_path}")
        return file_path

    # Descargar dataset
    print("Descargando dataset desde KaggleHub...")
    dataset_path = kagglehub.dataset_download("saurav9786/amazon-product-reviews")
    print(f"Ruta del dataset descargado: {dataset_path}")

    # Buscar y copiar el archivo
    found = False
    for root, _, files in os.walk(dataset_path):
        if original_file_name in files:
            # Crear carpeta solo si se encuentra el archivo
            os.makedirs(base_dir, exist_ok=True)
            src_file = os.path.join(root, original_file_name)
            shutil.copy2(src_file, file_path)
            print(f"Ruta del dataset: {file_path}")
            found = True
            break

    if not found:
        print(f"Error: No se encontró el archivo '{original_file_name}' en el dataset descargado.")
        return None

    return file_path
