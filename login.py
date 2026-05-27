from tradingapi_a.mconnect import MConnect
import pyotp
from config import LOGIN

mconnect_obj = MConnect()

resp1 = mconnect_obj.login(
            LOGIN["user_id"],
            LOGIN["password"]
        )

print(resp1.json())