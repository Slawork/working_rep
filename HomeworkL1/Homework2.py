suits = {
    '♠': 'пики',
    '♣': 'крести',
    '♦': 'бубны',
    '♥': 'червы'
}
card = input("Введите карту: ").strip()
suit_symbol = card[-1]
suit_name = suits.get(suit_symbol, "неизвестная масть")
print(f"Масть карты: {suit_name}")