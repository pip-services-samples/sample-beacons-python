# -*- coding: utf-8 -*-
"""
    app.py
    ~~~~~~~~~~~~~~~~~~~~

    Beacons app run implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
import sys
import traceback
import os

from pip_services3_components.log import ConsoleLogger

# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from pip_beacons_sample_python.container.BeaconsProcess import BeaconsProcess

if __name__ == '__main__':
    runner = BeaconsProcess()
    print("run")
    try:
        runner.run()
    except Exception as ex:
        ConsoleLogger().fatal("Beacons", ex, "Error: ")
        print(traceback.format_exc())
        sys.stderr.write(str(ex) + '\n')
