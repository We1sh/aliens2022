class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициалищирует настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5
        