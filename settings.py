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
        self.ship_limit = 3
        
        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        self.fleet_direction = 1
        # 1 - вправо, -1 - влево