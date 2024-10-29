import json
import random

# Путь к JSON файлу
file_path = 'data/plots.json'

# Загрузка данных из JSON файла
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Функция для генерации случайного элемента из таблицы Менделеева
def random_mineral():
    elements = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", 
        "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", 
        "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", 
        "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", 
        "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", 
        "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", 
        "Caesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", 
        "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", 
        "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", 
        "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", 
        "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", 
        "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", 
        "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", 
        "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", 
        "Oganesson"
    ]
    return random.choice(elements)

# Список изображений для обновления данных
images_to_update = [
    "images/sand.png"
]

# Обновляем данные для всех участков
for plot in data:
    if plot.get("image") in images_to_update:  # Проверка на наличие изображения в списке
        plot["🏠 Land Type"] = "Sand"
        plot["💰 Minerals"] = random_mineral()
        plot["🌟 Rarity"] = "Epic"
        plot["💧 Water"] = str(random.randint(1, 5))
        plot["📈 Income"] = str(random.randint(1, 80))
        plot["🌊 View"] = "Ocean"
        plot["📦 Storage"] = str(random.randint(30, 70))
        plot["link"] = "https://commerce.coinbase.com/checkout/c5e7dac9-6baa-4800-b0d9-893f3fc7b16c"

# Сохранение обновленных данных обратно в файл
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Обновление завершено.")