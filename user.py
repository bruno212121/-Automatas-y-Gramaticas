class User: 
    
    def __init__(self, id , user, start_conection, end_conection, session_time, mac_ap, mac_client, sent_byte, rec_byte):
        self.id = id
        self.user = user
        self.start_conection = start_conection
        self.end_conection = end_conection
        self.session_time = session_time
        self.mac_ap = mac_ap
        self.mac_client = mac_client
        self.sent_byte = sent_byte
        self.rec_byte = rec_byte

    def __repr__(self) -> str:
        return f"ID: {self.id} user: {self.user} Start Conection: {self.start_conection} End Conection: {self.end_conection} Session Time: {self.session_time} Ap Mac: {self.mac_ap} Client Mac: {self.mac_client} Bytes Sent: {self.sent_byte} Received Bytes: {self.rec_byte}"
    

    @staticmethod # Static method to read the file
    def create_object(line): # Create an object with the information of the file
        id = line[0] # Get the information of the file
        user = line[1]
        start_conection = line[2]
        end_conection = line[3]
        session_time = line[4]
        mac_ap = line[5]
        mac_client = line[6]
        sent_byte = line[7]
        rec_byte = line[8]
        info_user = User(id, user, start_conection, end_conection, session_time, mac_ap, mac_client, sent_byte, rec_byte)
        return info_user 