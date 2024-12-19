
# Общие задания

---

## Задание 1

- Создать два связанных класса:
    - **ImageHandler** — класс для базовой работы с изображениями (загрузка, сохранение, изменение размеров и форматов).
    - **ImageProcessor** — класс для обработки изображения (применение фильтров, добавление текста, поворот).
- Класс **ImageHandler** должен:
    - Принимать путь к изображению при инициализации.
    - Содержать методы для загрузки изображения, сохранения и изменения его размера.
    - Обеспечивать передачу изображения в класс **ImageProcessor**.
- Класс **ImageProcessor** должен:
    - Принимать изображение, переданное из **ImageHandler**.
    - Содержать методы для применения различных фильтров, добавления текста и других эффектов.

<aside>
🚨

В каждом классе нужно реализовать свой функционал, указанный в варианте далее

</aside>

# Индивидуальные задания

---

## Задание 2


### **Вариант 3**

1. В классе **ImageHandler**:
    - Реализовать метод для уменьшения изображения (thumbnail) с максимальными размерами 200x200 пикселей.
    - Реализовать метод для сохранения уменьшенного изображения с новым именем.
2. В классе **ImageProcessor**:
    - Применить фильтр контуров (CONTOUR).
    - Добавить текст "Вариант 3" в центре изображения.
