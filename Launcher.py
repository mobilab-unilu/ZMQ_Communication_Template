import subprocess
import sys
import time
from Logger import get_logger

logger = get_logger()

import os
import subprocess
import sys

def create_virtualenv():

    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
        print("Virtual environment successfully created")

def install_dependencies():

    print("Dependencies installation...")
    subprocess.check_call([os.path.join('venv', 'bin', 'pip'), 'install', '-r', 'requirements.txt'])
    print("Dependencies installed")

def verify_requirements():

    if not os.path.exists('venv'):
        create_virtualenv()
        install_dependencies()
    else:
        print("Virtual environment already existing")
        # Controlla se le dipendenze sono installate
        try:
            subprocess.check_call([os.path.join('venv', 'bin', 'pip'), 'check'])
        except subprocess.CalledProcessError:
            print("Dependencies not present or not installed yet. Install...")
            install_dependencies()

    print("Startup main program...")
    subprocess.check_call([os.path.join('venv', 'bin', 'python'), 'main.py'])

def main():
    python_executable = sys.executable

    # Launch all programs
    router_process = subprocess.Popen([python_executable, 'Router.py'])
    logger.info('LAUNCHER: Router launched')

    dealer1_process = subprocess.Popen([python_executable, 'Dealer_1.py'])
    logger.info('LAUNCHER: Dealer 1 launched')

    dealer2_process = subprocess.Popen([python_executable, 'Dealer_2.py'])
    logger.info('LAUNCHER: Dealer 2 launched')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info('LAUNCHER: Closing all programs')
        router_process.terminate()
        dealer1_process.terminate()
        dealer2_process.terminate()

if __name__ == '__main__':
    verify_requirements()
    main()