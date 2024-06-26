firmware_vectors = {
    "B900": "KL_U_ROM_ENABLE",
    "B903": "KL_U_ROM_DISABLE",
    "B906": "KL_L_ROM_ENABLE",
    "B909": "KL_L_ROM_DISABLE",
    "B90C": "KL_ROM_RESTORE",
    "B90F": "KL_ROM_SELECT",
    "B912": "KL_CURR_SELECTION",
    "B915": "KL_PROBE_ROM",
    "B918": "KL_ROM_DESELECT",
    "B91B": "KL_LDIR_LDIR",
    "B91E": "KL_LDDR_LDDR",
    "B921": "KL_POLL_SYNCHRONOUS",
    "B941": "RST_7_INTERRUPT_ENTRY",
    "B978": "KL_EXT_INTERRUPT_ENTRY",
    "B984": "KL_LOW_PCHL_CONT",
    "B98A": "RST_1_LOW_JUMP_CONT",
    "B9B9": "KL_FAR_PCHL_CONT",
    "B9C1": "KL_FAR_ICALL_CONT",
    "B9C7": "RST_LOW_FAR_CALL",
    "BA17": "KL_SIDE_PCHL_CONT",
    "BA1D": "RST_2_LOW_SIDE_CALL",
    "BA35": "RST_5_FIRM_JUMP",
    "BA51": "KL_L_ROM_ENABLE",
    "BA58": "KL_L_ROM_DISABLE",
    "BA5F": "KL_U_ROM_ENABLE",
    "BA66": "KL_U_ROM_DISABLE",
    "BA70": "KL_ROM_RESTORE",
    "BA79": "KL_ROM_SELECT",
    "BA7E": "KL_PROBE_ROM",
    "BA87": "KL_ROM_DESELECT",
    "BA9D": "KL_CURR_SELECTION",
    "BAA1": "KL_LDIR",
    "BAA7": "KL_LDDR",
    "BAAD": "KL_ROM_OFF_CONFIG_SAVE",
    "BAC6": "RST_4_RAM_LAM",
    "BAD7": "KL_RAM_LAM_IX",
    "BB00": "KM_INITIALISE",
    "BB03": "KM_RESET",
    "BB06": "KM_WAIT_CHAR",
    "BB09": "KM_READ_CHAR",
    "BB0C": "KM_CHAR_RETURN",
    "BB0F": "KM_SET_EXPAND",
    "BB12": "KM_G_ET_EXPAND",
    "BB15": "KM_EXP_BUFFER",
    "BB18": "KM_WAIT_KEY",
    "BB1B": "KM_READ_KEY",
    "BB1E": "KM_TEST_KEY",
    "BB21": "KM_GET_STATE",
    "BB24": "KM_GET_JOYSTICK",
    "BB27": "KM_SET_TRANSLATE",
    "BB2A": "KM_GET_TRANSLATE",
    "BB2D": "KM_SET_SHIFT",
    "BB30": "KM_GET_SHIFT",
    "BB33": "KM_SET_CONTROL",
    "BB36": "KM_GET_CONTROL",
    "BB39": "KM_SET_REPEAT",
    "BB3C": "KM_GET_REPEAT",
    "BB3F": "KM_SET_DELAY",
    "BB42": "KM_GET_DELAY",
    "BB45": "KM_ARM_BREAK",
    "BB48": "KM_DISARM_BREAK",
    "BB4B": "KM_BREAK_EVENT",
    "BB4E": "TXT_INITIALISE",
    "BB51": "TXT_RESET",
    "BB54": "TXT_VDU_ENABLE",
    "BB57": "TXT_VDU_DISABLE",
    "BB5A": "TXT_OUTPUT",
    "BB5D": "TXT_WR_CHAR",
    "BB60": "TXT_RD_CHAR",
    "BB63": "TXT_SET_GRAPHIC",
    "BB66": "TXT_WIN_ENABLE",
    "BB69": "TXT_GET_WINDOW",
    "BB6C": "TXT_CLEAR_WINDOW",
    "BB6F": "TXT_SET_COLUMN",
    "BB72": "TXT_SET_ROW",
    "BB75": "TXT_SET_CURSOR",
    "BB78": "TXT_GET_CURSOR",
    "BB7B": "TXT_CUR_ENABLE",
    "BB7E": "TXT_CUR_DISABLE",
    "BB81": "TXT_CUR_ON",
    "BB84": "TXT_CUR_OFF",
    "BB87": "TXT_VALIDATE",
    "BB8A": "TXT_PLACE/REMOVE_CURSOR",
    "BB8D": "TXT_PLACE/REMOVE_CURSOR",
    "BB90": "TXT_SET_PEN",
    "BB93": "TXT_GET_PEN",
    "BB96": "TXT_SET_PAPER",
    "BB99": "TXT_GET_PAPER",
    "BB9C": "TXT_INVERSE",
    "BB9F": "TXT_SET_BACK",
    "BBA2": "TXT_GET_BACK",
    "BBA5": "TXT_GET_MATRIX",
    "BBA8": "TXT_SET_MATRIX",
    "BBAB": "TXT_SET_M_TABLE",
    "BBAE": "TXT_GET_M_TABLE",
    "BBB1": "TXT_GET_CONTROLS",
    "BBB4": "TXT_STR_SELECT",
    "BBB7": "TXT_SWAP_STREAMS",
    "BBBA": "GRA_INITIALISE",
    "BBBD": "GRA_RESET",
    "BBC0": "GRA_MOVE_ABSOLUTE",
    "BBC3": "GRA_MOVE_RELATIVE",
    "BBC6": "GRA_ASK_CURSOR",
    "BBC9": "GRA_SET_ORIGIN",
    "BBCC": "GRA_GET_ORIGIN",
    "BBCF": "GRA_WIN_WIDTH",
    "BBD2": "GRA_WIN_HEIGHT",
    "BBD5": "GRA_GET_W_WIDTH",
    "BBD8": "GRA_GET_W_HEIGHT",
    "BBDB": "GRA_CLEAR_WINDOW",
    "BBDE": "GRA_SET_PEN",
    "BBEl": "GRA_GET_PEN",
    "BBE4": "GRA_SET_PAPER",
    "BBE7": "GRA_GET_PAPER",
    "BBEA": "GRA_PLOT_ABSOLUTE",
    "BBED": "GRA_PLOT_RELATIVE",
    "BBF0": "GRA_TEST_ABSOLUTE",
    "BBF3": "GRA_TEST_RELATIVE",
    "BBF6": "GRA_LINE_ABSOLUTE",
    "BBF9": "GRA_LINE_RELATIVE",
    "BBFC": "GRA_WR_CHAR",
    "BBFF": "SCR_INITIALISE",
    "BC02": "SCR_RESET",
    "BC05": "SCR_SET_OFFSET",
    "BC08": "SCR_SET_BASE",
    "BC0B": "SCR_GET_LOCATION",
    "BC0E": "SCR_SET_MODE",
    "BC11": "SCR_GET_MODE",
    "BC14": "SCR_CLEAR",
    "BC17": "SCR_CHAR_LIMITS",
    "BC1A": "SCR_CHAR_POSITION",
    "BC1D": "SCR_DOT_POSITION",
    "BC20": "SCR_NEXT_BYTE",
    "BC23": "SCR_PREV_BYTE",
    "BC26": "SCR_NEXT_LINE",
    "BC29": "SCR_PREV_LINE",
    "BC2C": "SCR_INK_ENCODE",
    "BC2F": "SCR_INK_DECODE",
    "BC32": "SCR_SET_INK",
    "BC35": "SCR_GET_INK",
    "BC38": "SCR_SET_BORDER",
    "BC3B": "SCR_GET_BORDER",
    "BC3E": "SCR_SET_FLASHING",
    "BC41": "SCR_GET_FLASHING",
    "BC41": "SCR_GET_FLASHING",
    "BC4A": "SCR_CHAR_INVERT",
    "BC4A": "SCR_CHAR_INVERT",
    "BC50": "SCR_SW_ROLL",
    "BC53": "SCR_UNPACK",
    "BC56": "SCR_REPACK",
    "BC59": "SCR_ACCESS",
    "BC5C": "SCR_PDCELS",
    "BC5F": "SCR_HORIZONTAL",
    "BC62": "SCR_VERTICAL",
    "BC65": "CAS_INITIALISE",
    "BC68": "CAS_SET_SPEED",
    "BC6B": "CAS_NOISY",
    "BC6E": "CAS_START_MOTOR",
    "BC71": "CAS_STOP_MOTOR",
    "BC74": "CAS_RESTORE_MOTOR",
    "BC77": "CAS_IN_OPEN",
    "BC7A": "CAS_IN_CLOSE",
    "BC7D": "CAS_IN_ABANDON",
    "BC80": "CAS_IN_CHAR",
    "BC83": "CAS_IN_DIRECT",
    "BC86": "CAS_RETURN",
    "BC89": "CAS_TEST_EOF",
    "BC8C": "CAS_OUT_OPEN",
    "BC8F": "CAS_OUT_CLOSE",
    "BC92": "CAS_OUT_ABANDON",
    "BC95": "CAS_OUT_CHAR",
    "BC98": "CAS_OUT_DIRECT",
    "BC9B": "CAS_CATALOG",
    "BC9E": "CAS_WRITE",
    "BCA1": "CAS_READ",
    "BCA4": "CAS_CHECK",
    "BCA7": "SOUND_RESET",
    "BCAA": "SOUND_QUEUE",
    "BCAD": "SOUND_CHECK",
    "BCB0": "SOUND_ARM_EVENT",
    "BCB3": "SOUND_RELEASE",
    "BCB6": "SOUND_HOLD",
    "BCB9": "SOUND_CONTINUE",
    "BCBC": "SOUND_AMPL_ENVELOPE",
    "BCBF": "SOUND_TONE_ENVELOPE",
    "BCC2": "SOUND_A_ADRESS",
    "BCC5": "SOUND_T_ADRESS",
    "BCC8": "KL_CHOKE_OFF",
    "BCCB": "KL_ROM_WALK",
    "BCCE": "KL_INIT_BACK",
    "BCD1": "KL_LOG_EXT",
    "BCD4": "KL_FIND_COMMAND",
    "BCD7": "KL_NEW_FRAME_FLY",
    "BCDA": "KL_ADD_FRAME_FLY",
    "BCDD": "KL_DEL_FRAME_FLY",
    "BCEO": "KL_NEW_FAST_TICKER",
    "BCE3": "KL_ADD_FAST_TICKER",
    "BCE6": "KL_DEL_FAST_TICKER",
    "BCE9": "KL_ADD_TICKER",
    "BCEC": "KL_DEL_TICKER",
    "BCEF": "KL_INIT_EVENT",
    "BCF2": "KL_EVENT",
    "BCF5": "KL_SYNC_RESET",
    "BCF8": "KL_DEL_SYNCHRONOUS",
    "BCFB": "KL_NEXT_SYNC",
    "BCFE": "KL_DO_SYNC",
    "BD01": "KL_DONE_SYNC",
    "BD04": "KL_EVENT_DISABLE",
    "BD07": "KL_EVENT_ENABLE",
    "BD0A": "KL_DISARM_EVENT",
    "BD0D": "KL_TIME_PLEASE",
    "BD10": "KL_TIME_SET",
    "BD13": "MC_BOOT_PROGRAM",
    "BD16": "MC_START_PROGRAM",
    "BD19": "MC_WAIT_FLYBACK",
    "BD1C": "MC_SET_MODE",
    "BD1F": "MC_SCREEN_OFFSET",
    "BD22": "MC_CLEAR_INKS",
    "BD25": "MC_SET_INKS",
    "BD28": "MC_RESET_PRINTER",
    "BD2B": "MC_PRINT_CHAR",
    "BD2E": "MC_BUSY_PRINTER",
    "BD31": "MC_SEND_PRINTER",
    "BD34": "MC_SOUND_REGISTER",
    "BD37": "JUMP_RESTORE",
    "BD3A": "KM_SET_STATE",
    "BD3D": "KM_VIDER_BUFFER",
    "BD40": "TXT_FLAG_CURSEUR_ACTUEL_VERS_ACCU",
    "BD43": "GRA_NN",
    "BD46": "GRA_SAUVER_PARAMETRES",
    "BD49": "GRA_SAUVER_PARAMETRES_MASQUE",
    "BD4C": "GRA_SAUVER_PARAMETRES_MASQUE",
    "BD4F": "GRA_CONVERTIR_COORD",
    "BD52": "GRA_FILL",
    "BD5S": "SCR_MODIFIER_DEBUT_ECRAN",
    "BD58": "MC_AFFECTATION_DE_CARACTERES"
}


def checkFirmwareVector(s):
    """
    """
    s = s.upper()
    for v in firmware_vectors.keys():
        if v in s:
            return firmware_vectors[v]
    return False
