class Settings:
    """Класс для хранения настроек"""

    def __init__(self):
        """Инициализация настроек игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # (1) - движение флота вправо, (-1) - движение флота влево
