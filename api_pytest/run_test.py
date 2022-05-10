from common.do_config import *

from common.do_log import log
from common.do_contants import *
import sys
config = ReadConfig()

log.info('----------------用例执行开始--------------------')
# python -m run_test "test0"
env = sys.argv[-1]
WriteConfig().write(value=env)


log.info('----------------用例执行结束--------------------')

