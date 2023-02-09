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
        