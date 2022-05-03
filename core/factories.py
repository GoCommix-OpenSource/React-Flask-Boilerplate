from dotenv import dotenv_values
from pathlib import Path



# Customexceptions Exceptions
class AppError(Exception):
    pass

class SettingsError(Exception):
    pass

# config helpers
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
settings=dotenv_values(BASE_DIR/".env")
setting_name = f'core.config.{settings.get("WEBAPP_ENV","dev").capitalize()}Config'
static_url_path= BASE_DIR/'app/views/'
