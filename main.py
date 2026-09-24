from lib import calculate_discount, format_user_name

def main():
    print("=== Демонстрація роботи модулів ===")
    
    # Форматування імені
    formatted_name = format_user_name(" іван ", "петренко")
    print(f"Студент: {formatted_name}")
    
    # Розрахунок знижки
    original_price = 1200.0
    discount = 15.0
    final_price = calculate_discount(original_price, discount)
    
    print(f"Початкова ціна: {original_price} грн")
    print(f"Ціна зі знижкою ({discount}%): {final_price:.2f} грн")

if __name__ == "__main__":
    main()