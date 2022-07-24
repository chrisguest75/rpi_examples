import logging
import requests 

logger = logging.getLogger('rpiclient.send')

class send():
    def __init__(self, grid: Text, trie: Type[dictionary_abc]):
        width = 4
        height = 4
        logger.info(f"Grid \"{grid}\" split into {width}x{height}", extra={"grid": grid})
        self._board = wordament_helper._board_state(width, height, grid)
        self._trie = trie