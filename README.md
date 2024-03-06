# Django-Recipes

Создайте проект Django и приложение(я) для сайта рецептов.

## Модели

Для работы с пользователями используйте встроенного в Django User`a.
Подготовьте нижеперечисленные модели:

- Рецепты:
  - Название
  - Описание
  - Шаги приготовления
  - Время приготовления
  - Изображение
  - Автор
  - \*другие поля на ваш выбор, например ингредиенты и т.п.
- \*Категории рецептов
  - Название
  - \*другие поля на ваш выбор
- \*Связующая таблица для связи Рецептов и Категории
  - \*обязательные для связи поля
  - \*другие поля на ваш выбор

## Шаблоны

Подготовьте базовый шаблон проекта и нижеперечисленные дочерние шаблоны:

- Главная с 5 случайными рецептами кратко
- Страница с одним подробным рецептом
- Страницы регистрации, авторизации и выхода пользователя
- Страница добавления/редактирования рецепта
- \*другие шаблоны на ваш выбор

## Формы

Создайте формы для ввода и редактирования информации (рецептов) в вашем
проекте. Интегрируйте их в шаблоны.

## Представления

Создайте представления, которые охватывают весь ваш проект: модели, формы,
шаблоны.

## Маршруты

Подключите маршруты, убедитесь в работоспособности представлений и связанных
с ними моделей, форм и шаблонов.

## Облачный сервер и наполнение

Разверните рабочий проект на сервере. Наполните базу данных как минимум пятью
рецептами.
