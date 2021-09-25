import geocoder
import requests
import sys
from datetime import datetime, timezone
import logger
import subprocessrunner

try:
    # Get current location
    geoResponse = geocoder.ip('me')
    logger.info(f'Current location: {geoResponse.latlng}')

    # Fetch current sunset/sunrise
    date = datetime.today().strftime('%Y-%m-%d')
    url = f'https://api.sunrise-sunset.org/json?lat={geoResponse.lat}&lng={geoResponse.lng}&date={date}&formatted=0'
    response = requests.get(url).json()
    sunset = datetime.fromisoformat(response['results']['sunset'])
    sunrise = datetime.fromisoformat(response['results']['sunrise'])
    now = datetime.now(tz=timezone.utc)
    logger.info(f'Sunset: {sunset} · Sunrise: {sunrise} · Now: {now}')

    # Determine if nighttime
    useDarkTheme = now > sunset or now < sunrise
    logger.info(f'Setting {"dark" if useDarkTheme else "light"} theme...')

    # Set registry key
    # reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f
    # reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f
    regPath = 'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    regValue = '0' if useDarkTheme else '1'
    subprocessrunner.run(['reg', 'add', regPath, '/v', 'AppsUseLightTheme',
                   '/t', 'REG_DWORD', '/d', regValue, '/f'])
    subprocessrunner.run(['reg', 'add', regPath, '/v', 'SystemUsesLightTheme',
                   '/t', 'REG_DWORD', '/d', regValue, '/f'])
except:
    logger.error('Unexpected error:', sys.exc_info()[0])
    raise
