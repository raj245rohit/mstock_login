from tradingapi_a.mconnect import MConnect
import pyotp
from config import LOGIN

mconnect_obj = MConnect()

resp1 = mconnect_obj.login(
            LOGIN["user_id"],
            LOGIN["password"]
        )

# print(resp1.json())



# Step 2 → generate TOTP
totp = pyotp.TOTP(LOGIN["totp_secret"])
otp = totp.now()



# Step 3 → generate session
resp2 = mconnect_obj.verify_totp(
    LOGIN["api_key"],
    otp
)

print(resp2.json()['status'])