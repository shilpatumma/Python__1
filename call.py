# (4). Telecommunication System
# Call Hierarchy:
# Base class Call with attributes like caller, callee, start_time, end_time.
# Subclasses: VoiceCall, VideoCall, ConferenceCall, etc., 
# with specific attributes (e.g., video_quality, participants) 
# and methods (e.g., calculate_duration, record_call).

# Customer Hierarchy:
# Base class Customer with attributes like customer_id, name, address.
# Subclasses: IndividualCustomer, CorporateCustomer, etc., with specific attributes (e.g., company_name, tax_id) and methods (e.g., generate_bill).

# Ans...

class Call:
    def __init__(self, caller, callee, start_time, end_time):
        self.caller = caller
        self.callee = callee
        self.start_time = start_time
        self.end_time = end_time

    def calculate_duration(self):
        duration = self.end_time - self.start_time
        return duration


class VoiceCall(Call):
    def __init__(self, caller, callee, start_time, end_time):
        super().__init__(caller, callee, start_time, end_time)

    def record_call(self):
        print(f"Recording voice call : from {self.caller} to {self.callee}")


class VideoCall(Call):
    def __init__(self, caller, callee, start_time, end_time, video_quality):
        super().__init__(caller, callee, start_time, end_time)
        self.video_quality = video_quality

    def record_call(self):
        print(f"Recording video call : from {self.caller} to {self.callee} at {self.video_quality}")


class ConferenceCall(Call):
    def __init__(self, caller, participants, start_time, end_time):
        super().__init__(caller, participants, start_time, end_time)
        self.participants = participants

    def record_call(self):
        print(f"Recording Conference call with participants : {', '.join(self.participants)}")


class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def generate_bill(self):
        return f"\nBill for {self.name} & ID : {self.customer_id}"


class IndividualCustomer(Customer):
    def __init__(self, customer_id, name, address, phone_number):
        super().__init__(customer_id, name, address)
        self.phone_number = phone_number

    def generate_bill(self, charge):
        customer_bill = super().generate_bill()
        self.charge = charge
        return f"{customer_bill} \nPhone Number : {self.phone_number} \nCharge : {self.charge}"


class CorporateCustomer(Customer):
    def __init__(self, customer_id, name, address, company_name, tax_id):
        super().__init__(customer_id, name, address)
        self.company_name = company_name
        self.tax_id = tax_id

    def generate_bill(self, charge):
        customer_bill = super().generate_bill()
        self.charge = charge
        return f"{customer_bill} \nCompany Name : {self.company_name} & Tax ID : {self.tax_id} \ncharge : {self.charge}"

if __name__ == "__main__":
    print("\n************ Telecommunication System ************")

    individual = IndividualCustomer(101, "Priya", "45, new bunglow, Mumbai.", 1234567890)
    corporate = CorporateCustomer(201, "Sunidhi", "78, shine complex, Delhi.", "ABC Tech company", 12345)

    voice_call = VoiceCall("Priya", "Fenil", 0, 240)
    video_call = VideoCall("Priya", "Vivek", 0, 300, "720p")
    conference_call = ConferenceCall("Sunidhi", ["riya", "Kevin", "Jenish"], 0, 360)

    print(f"\nvoice call duration : {voice_call.calculate_duration()} seconds.")
    voice_call.record_call()

    print(f"\nvideo call duration : {video_call.calculate_duration()} seconds.")
    video_call.record_call()

    print(f"\nconference call duration : {conference_call.calculate_duration()} seconds.")
    conference_call.record_call()

    print(individual.generate_bill(150))
    print(corporate.generate_bill(250))
