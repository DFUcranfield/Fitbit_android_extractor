import sqlite3, os

##### OUTPUT PATH #####
output_path = "C:\\Users\\Student\\Desktop\\Report"
evidence_path = "C:\\Users\\Student\\Desktop\\com.fitbit.FitbitMobile\\"


##### database_paths #####

##############################

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def connect_to_databases(database_path):

    try:
        database_connection = sqlite3.connect(database_path)
        cursor = database_connection.cursor()
    except:
        print("DATABASE ERROR: " + database_path)
    return cursor

def query_table(cursor, information):
    cursor.execute(information[2])
    query_results_list = cursor.fetchall()
    file_pointer = open((output_path + "\\log.txt"), "a")   
    file_pointer.write("************ QUERY RAN *******************\n")
    file_pointer.write("QUERY RAN\n")
    file_pointer.write(information[2] + "\n")
    file_pointer.write("Number of Results: " + str(len(query_results_list)) + "\n\n")
    if len(query_results_list) > 0:
        return query_results_list
    else:
        return []


def write_query(query_results_list, row_descriptors, save_location, db_name, db_location, sql_command):
        
    file_pointer = open(save_location, "a")
    file_pointer.write("*******************************\n")
    file_pointer.write("*******************************\n")
    file_pointer.write("Database Location : " + db_location + "\n")
    file_pointer.write("Database Name : " + db_name + "\n")
    file_pointer.write("SQL command : " + sql_command + "\n")
    file_pointer.write("*******************************\n\n")
    for each_tuple in query_results_list:

        n = 0    
        file_pointer.write("*******************************\n")

        for each_entry in each_tuple:
            line_to_write = row_descriptors[n] + " - " + str(each_entry) + "\n"
            file_pointer.write(line_to_write)
            n += 1
    file_pointer.close()

def start_log(information):
    file_pointer = open((output_path + "\\log.txt"), "a")   
    file_pointer.write("************ DATABASE OPENED *******************\n")
    file_pointer.write("Database Location : " + information[0] + "\n")
    file_pointer.write("Database Name : " + information[1] + "\n")
    file_pointer.write("SQL command : " + information[2] + "\n\n")

def extract_data(information):
    cursor = connect_to_databases(information[0])
    start_log(information)
    query_results_list = query_table(cursor, information)
    ensure_dir(information[4])
    write_query(query_results_list, information[3], information[4], information[1], information[0], information[2])


def activity_db_info():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\activity_db"
    information += [db_location]
    information += ["activity_db"]
    information += ["SELECT START_TIME, DISTANCE, DURATION, STEPS, FAT_BURN_HEART_RATE_ZONE_MINUTES,CARDIO_HEART_RATE_ZONE_MINUTES, PEAK_HEART_RATE_ZONE_MINUTES, AVERAGE_HEART_RATE, ELEVATION_GAIN FROM activity_log_entry"]
    information += [["activity_log_entry", "START_TIME", "DISTANCE", "DURATION", "STEPS",
               "FAT_BURN_HEART_RATE_ZONE_MINUTES", "CARDIO_HEART_RATE_ZONE_MINUTES",
                                  "PEAK_HEART_RATE_ZONE_MINUTES", "AVERAGE_HEART_RATE", "ELEVATION_GAIN"]]
    output = output_path + "\\activity_db\\activity_log_entry.txt"
    information += [output] 
    return information

def device_notification_db_info_1():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\device_notification.db"
    information += [db_location]
    information += ["device_notification.db"]
    information += ["SELECT source_id, app_id, data FROM notification"]
    information += [["source_id", "app_id", "data"]]
    output = output_path + "\\device_notification_db\\notification.txt"
    information += [output] 
    return information

def device_notification_db_info_2():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\device_notification.db"
    information += [db_location]
    information += ["device_notification.db"]
    information += ["SELECT notification_id FROM reply_action"]
    information += [["notification_id", "data"]]
    output = output_path + "\\device_noticiation_db\\reply_action.txt"
    information += [output] 
    return information

def family_db_info():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\family.db"
    information += [db_location]
    information += ["family.db"]
    information += ["SELECT username, display_name, role, birthday FROM FamilyMembers"]
    information += [["username", "display_name", "role", "birthday"]]
    output = output_path + "\\family_db\\FamilyMembers.txt"
    information += [output] 
    return information

def fitbit_db_info():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\fitbit_db"
    information += [db_location]
    information += ["fitbit_db"]
    information += ["SELECT UUID, LAST_SYNC_TIME, NAME, BATTERY_LEVEL, MAC FROM DEVICE"]
    information += [["UUID", "LAST_SYNC_TIME", "NAME", "BATTERY_LEVEL", "MAC"]]
    output = output_path + "\\fitbit_db\\DEVICE.txt"
    information += [output] 
    return information

def heart_rate_db_info_1():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\heart_rate_db"
    information += [db_location]
    information += ["heart_rate_db"]
    information += ["SELECT DATE_TIME, AVERAGE_HEART_RATE, RESTING_HEART_RATE FROM HEART_RATE_DAILY_SUMMARY"]
    information += [["DATE_TIME", "AVERAGE_HEART_RATE", "RESTING_HEART_RATE"]]
    output = output_path + "\\heart_rate_db\\HEART_RATE_DAILY_SUMMARY.txt"
    information += [output] 
    return information

def heart_rate_db_info_2():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\heart_rate_db"
    information += [db_location]
    information += ["heart_rate_db"]
    information += ["SELECT HIGH_VALUE, LOW_VALUE, TIME_IN_ZONE FROM HEART_RATE_ZONE"]
    information += [["HIGH_VALUE", "LOW_VALUE", "TIME_IN_ZONE"]]
    output = output_path + "\\heart_rate_db\\HEART_RATE_ZONE.txt"
    information += [output] 
    return information

def messages_db_info():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\messages_db"
    information += [db_location]
    information += ["messages_db"]
    information += ["SELECT messageID, message, timestamp, read, senderDisplayName FROM UserMessage"]
    information += [["messageID", "message", "timestamp", "read", "senderDisplayName"]]
    output = output_path + "\\messages_db\\UserMessage.txt"
    information += [output] 
    return information

def sleep_info():
    information = []
    db_location = evidence_path + "com.fitbit.FitbitMobile\\databases\\sleep"
    information += [db_location]
    information += ["sleep"]
    information += ["SELECT DATE_OF_SLEEP, DURATION, MINUTES_ASLEEP, MINUTES_AWAKE FROM SLEEP_LOG"]
    information += [["DATE_OF_SLEEP", "DURATION", "MINUTES_ASLEEP", "MINUTES_AWAKE"]]
    output = output_path + "\\sleep\\SLEEP_LOG.txt"
    information += [output] 
    return information

information = activity_db_info()
extract_data(information)

information = device_notification_db_info_1()
extract_data(information)

information = device_notification_db_info_2()
extract_data(information)

information = family_db_info()
extract_data(information)

#information = fitbit_db_info()
#extract_data(information)

information = heart_rate_db_info_1()
extract_data(information)

information = heart_rate_db_info_2()
extract_data(information)

information = messages_db_info()
extract_data(information)


