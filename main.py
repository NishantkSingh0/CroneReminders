import utils as ut
import os
from dotenv import load_dotenv
load_dotenv()

ut.remindByMessage(phone_numbers=[os.getenv("TEST_NUMBERS")])