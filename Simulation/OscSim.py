from oscsim_manager import OscSim
import logging
import sys

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

def main() -> None:
    OscSim().start_engine()

if __name__ == '__main__':
    main()