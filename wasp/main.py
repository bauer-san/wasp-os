# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2020 Daniel Thompson

import wasp
from gadgetbridge import *
wasp.system.schedule()

from clockNOW import ClockNOWApp
wasp.system.register(ClockNOWApp())
