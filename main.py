import datetime

from TgParsingEngine import TgChannelParsingEngine
from properties import APTREPORTS_CHAT_ID, BACK_URL, TI_TRENDS_CHAT_ID, BLEEPING_COMPUTER_CHAT_ID, T_HUNTER_CHAT_ID, \
    SEC_ATOR_CHAT_ID, RED_TEAM_CHAT_ID, AVLEONOV_RUS_CHAT_ID, POSITIVE_CHAT_ID, CYBER_THREAT_INT_CHAT_ID, \
    DATA_LEAK_MONITOR

if __name__ == '__main__':
    chat_ids_list = [APTREPORTS_CHAT_ID,
                     TI_TRENDS_CHAT_ID,
                     BLEEPING_COMPUTER_CHAT_ID,
                     T_HUNTER_CHAT_ID,
                     SEC_ATOR_CHAT_ID,
                     RED_TEAM_CHAT_ID,
                     AVLEONOV_RUS_CHAT_ID,
                     POSITIVE_CHAT_ID,
                     CYBER_THREAT_INT_CHAT_ID,
                     DATA_LEAK_MONITOR]

    TgChannelParsingEngine(BACK_URL, chat_ids_list).run()
