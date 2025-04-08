Название проекта: Авто-тесты для платформы Stape

Тестирование покрывается базовые сценарии работы с платформой Stape (открытие страницы, проверка валидности кнопок)

Для запуска: python test_index_page.py

Стек: Python + Playwright

Планируется добавить: проверку авторизации и регистрации пользователя, запрос восстановление пароля.

Пример кода:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        time.sleep(10)
