from aiogram.dispatcher.filters.state import State, StatesGroup


class BotState(StatesGroup):
    gender = State()
    goal = State()
    weight = State()
    height = State()
    age = State()
    activity = State()
    
    
info = 'Вычисления базируются на основе формулы Харриса-Бенедикта. Обратите внимание, что формулу Харриса-Бенедикта нельзя ' \
               'применять очень полным людям (формула переоценивает их действительную потребность в калориях) и очень мускулистым ' \
               '(формула недооценивает их действительные потребности). Формула может быть использована для расчёта калорийности' \
               'для лиц старше 18 лет. Тем не менее, расчеты по уравнению Харриса–Бенедикта – прекрасная точка отсчета, ее показатели ' \
               'могут лечь в основу эффективной и сбалансированной диеты, она позволяет оценить свои энергетические потребности, ' \
               'пересмотреть и скорректировать рацион, чтобы в конечном итоге достичь тех параметров, который каждый считает для ' \
               'себя максимально приемлемыми.'

activity_message = 'Укажите уровень вашей активности:\n\n\n' \
                   '1️⃣ Низкая или отсутствует\n\n' \
                   '2️⃣ Невысокая активность (1–3 тренировки в неделю)\n\n' \
                   '3️⃣ Умеренная активность (3–5 тренировок в неделю)\n\n' \
                   '4️⃣ Высокая активность (6–7 тренировок в неделю)\n\n' \
                   '5️⃣ Экстремально высокая активность (2 и более тренировок в день)'

activity_indexes = {
    '1️⃣': 1.2,
    '2️⃣': 1.375,
    '3️⃣': 1.55,
    '4️⃣': 1.725,
    '5️⃣': 1.9
}

goal_indexes = {
    'Похудение': 0.85,
    'Набор массы': 1.15,
    'Поддержание формы': 1
}


def calculator(user_data: dict) -> str:
    if user_data['gender'] == 'Мужчина 👨':
        result = activity_indexes[user_data['activity']] * (
                88.362 + 13.397 * int(user_data['weight']) + 4.799 * int(
            user_data['height']) - 5.677 * int(user_data['age']))
    else:
        result = activity_indexes[user_data['activity']] * (447.593 + 9.247 * int(
            user_data['weight']) + 3.098 * int(
                user_data['height']) - 4.330 * int(
                    user_data['age']))
        
    return f"Ваш суточный калораж составляет {int(goal_indexes[user_data['goal']] * result)} калорий"

        
