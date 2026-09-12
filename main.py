from datetime import datetime

# Входные данные предметной области (простые типы данных)
station_name = "ЭЗС #101 (CCS Combo 2, 150 кВт)"
station_power_kw = 150.0
price_per_kwh = 18.5
is_station_active = True
user_balance = 500.0

booking_date_str = "2026-09-15 14:00"
requested_duration_hours = 0.5


def check_station_availability(is_active):
    """Функция 1: Проверка доступности станции для бронирования."""
    if is_active:
        return "Станция активна и доступна для бронирования."
    else:
        return "Станция временно временно не работает или обслуживается."


def calculate_charging_cost(power_kw, duration_hours, tariff_per_kwh):
    """Функция 2: Расчет полной стоимости зарядной сессии."""
    total_energy_kwh = power_kw * duration_hours
    total_cost = total_energy_kwh * tariff_per_kwh
    return total_cost


def process_booking(balance, cost, date_str):
    """Функция 3: Оформление бронирования с проверкой баланса."""
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    formatted_date = parsed_date.strftime("%d.%m.%Y в %H:%M")

    if balance >= cost:
        remaining_balance = balance - cost
        return f"Успешно! Слот забронирован на {formatted_date}. Ост. баланс: {remaining_balance:.2f} руб."
    else:
        needed = cost - balance
        return f"Ошибка бронирования! Недостаточно средств. Пополните баланс на {needed:.2f} руб."


# Выполнение начального сценария
print(f"=== {station_name} ===")
print(f"Статус: {check_station_availability(is_station_active)}")

charging_cost = calculate_charging_cost(station_power_kw, requested_duration_hours, price_per_kwh)
print(f"Расчетная стоимость зарядки ({requested_duration_hours} ч): {charging_cost:.2f} руб.")

booking_result = process_booking(user_balance, charging_cost, booking_date_str)
print(f"Результат: {booking_result}")