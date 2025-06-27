#(©)CodeXBotz
#recoded by @Its_Oreki_Hotarou


import pymongo
import asyncio
from config import DB_URI, DB_NAME, FORCE_CHANNEL, FORCE_CHANNEL2
from motor.motor_asyncio import AsyncIOMotorClient

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

dbclient = AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]

user_data = database['users']
admin_data = database['admins']
channel_data = database['channels']
channel_data2 = database['channels2']

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

# Function to check if a user exists
async def present_user(user_id: int):
    return await user_data.find_one({'_id': user_id}) is not None

# Function to add a new user
async def add_user(user_id: int):
    await user_data.insert_one({'_id': user_id})

# Function to retrieve all users (Fixed)
async def full_userbase():
    user_docs = await user_data.find().to_list(length=None)  # Fixed cursor issue
    return [doc['_id'] for doc in user_docs]

# Function to delete a user
async def del_user(user_id: int):
    await user_data.delete_one({'_id': user_id})

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------

# Function to check if an admin exists
async def present_admin(admin_id: int):
    found = await admin_data.find_one({'_id': admin_id})
    return bool(found)

# Function to add a new admin
async def add_admin(admin_id: int):
    await admin_data.insert_one({'_id': admin_id}) 
    return

# Function to retrieve all admins
async def full_adminbase():
    admin_docs = admin_data.find()  
    admin_ids = [doc['_id'] async for doc in admin_docs]
    return admin_ids

# Function to delete an admin
async def del_admin(admin_id: int):
    await admin_data.delete_one({'_id': admin_id})
    return

#-------------------------------------------------------------------------------------------        
#-------------------------------------------------------------------------------------------
    
# Function to check if force-subscribe channel 1 exists
async def present_channel():
    try:
        config = await channel_data.find_one({})
        if not config:
            return FORCE_CHANNEL  # Default value if no data found
        return config.get("force_sub_channel_1", FORCE_CHANNEL)
    except Exception as e:
        print(f"❌ Failed to get force subscribe channel 1: {e}")
        return FORCE_CHANNEL

async def add_1(channel1: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: channel_data.update_one({}, {'$set': {'force_sub_channel_1': channel1}}, upsert=True))
        print(f"Force subscribe channel 1 set successfully: {channel1}")
    except Exception as e:
        print(f"Failed to set force subscribe channel 1: {e}")


# Function to check if force-subscribe channel 2 exists
async def present_channel2():
    try:
        config = await channel_data2.find_one({})
        if not config:
            return FORCE_CHANNEL2  # Default value if no data found
        return config.get("force_sub_channel_2", FORCE_CHANNEL2)
    except Exception as e:
        print(f"❌ Failed to get force subscribe channel 2: {e}")
        return FORCE_CHANNEL2

async def add_2(channel2: int):
    loop = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, lambda: channel_data2.update_one({}, {'$set': {'force_sub_channel_2': channel2}}, upsert=True))
        print(f"Force subscribe channel 2 set successfully: {channel2}")
    except Exception as e:
        print(f"Failed to set force subscribe channel 2: {e}")

#--------------------------------------------------------------------------------------------------------------------------------------------    
#--------------------------------------------------------------------------------------------------------------------------------------------   
## BC Deploy karo to Credit dedena 😆
