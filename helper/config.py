#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = "2444842"
    API_HASH = "90d5589b9d2c0b1702ef81a7d6a57173"
    BOT_TOKEN = "1886077796:AAEKQiQsHJOZhxPrrD2R2l6KcTNWZMXiiX8"
    OWNER = "1316963576"
    LOG = "-1001378474072"
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
