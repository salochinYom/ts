# Copyright (C) 2018, Cristian-Ioan Vasile (cvasile@bu.edu)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from lomap.classes import Ts

if __name__ == '__main__':
    # You may need to update this using absolute paths, depending on your system's configuration.
    ts = Ts.load('./simple_network.yaml')
    ts.visualize()

    ts = Ts.load('./traffic_light.yaml')
    ts.visualize()

    ts = Ts.load('./pedestrian_signal.yaml')
    ts.visualize()
