def math_func (a,b,c):
    try:
        if not all(isinstance(x, (int, float)) for x in [a, b, c]):
            raise ValueError("Все аргументы должны быть числами.")
        digit = 1e-9
        if abs(a + b - c) < digit:
            return '+'
        elif abs(a - b - c) < digit:
            return '-'
        elif abs(a * b - c) < digit:
            return '*'
        elif abs(a / b - c) < digit:
            return '/'
        else:
            return 'Операция не определена'
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception as e:
        return f"Ошибка: {e}"
print(math_func(1,2,1))