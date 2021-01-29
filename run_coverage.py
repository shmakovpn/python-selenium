"""
run_coverage.py
+++++++++++++++

Runs tests and coverage in *python_selenium/tests*.

Usage:

.. code-block:: bash
 
 python run_coverage.py

| Author: shmakovpn <shmakovpn@yandex.ru>
| Date: 2020-01-28
"""
import os
# The path to the folder of this script
SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))


def run_coverage() -> None:
    """Executes *coverage run* command"""
    coverage_cmd: str = f'coverage run --source=python_selenium -m pytest python_selenium/tests'
    os.system(coverage_cmd)
    report_cmd: str = 'coverage report'
    os.system(report_cmd)
    print('__END__')


if __name__ == '__main__':
    run_coverage()
