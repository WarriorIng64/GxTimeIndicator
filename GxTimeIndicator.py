# This file is part of GxTimeIndicator.
# Copyright (C) 2014 Christopher Kyle Horton <christhehorton@gmail.com>

# GxTimeIndicator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GxTimeIndicator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GxTimeIndicator. If not, see <http://www.gnu.org/licenses/>.


# GxTimeIndicator
# This indicator displays the current time.

self.time_string = ""

self.SetIcon(pygame.image.load("indicators/default/GxTimeIndicator/clock.png"))
self.image = self.icon

self.click_code = """
pygame.quit()
sys.exit()
"""

self.frame_code = """
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute
second = current_time.second
ampm = ''
time_string = ' '
if hour < 12:
  ampm = 'AM'
  time_string += str(hour)
else:
  ampm = 'PM'
  time_string += str(hour - 12)
time_string += ':'
if minute < 10:
  time_string += '0'
time_string += str(minute) + ':'
if second < 10:
  time_string += '0'
time_string += str(second) + ' ' + ampm + ' '
if self.time_string != time_string:
  self.image = indicator_font.render(time_string, True, glass.accent_color)
  self.width = self.image.get_width()
"""
