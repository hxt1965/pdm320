import pandas

from models.device import Device


class DeviceController:
    def __init__(self, file_name, database):
        self.df = pandas.read_csv(file_name)
        self.rows = self.df.shape[0]
        self.database = database

    def init_table_values(self):
        num_to_internet_service = {
            1: 'Dial-up',
            2: 'Higher-speed',
            3: 'Both Slow-speed/Dial-up and Higher-speed/Broadband',
            4: 'Access internet only using cell phone or tablet',
            5: 'No home internet access',
            8: 'Don\'t know',
            9: 'Refused'
        }

        Device.drop_table(self.database)
        Device.create_table(self.database)

        for i in range(self.rows):
            response_id = int(self.df['respid'][i])
            device = Device(self.database, response_id)

            internet_subscription = self.df['home4nw'][i]
            if (not pandas.isna(internet_subscription) and int(internet_subscription) == 1):
                internet_service = self.df['bbhome1'][i]
                if (not pandas.isna(internet_service)):
                    internet_service = int(internet_service)
                    if (internet_service == 1):
                        confirm_internet_service = self.df['bbhome2'][i]
                        if (not pandas.isna(confirm_internet_service)):
                            confirm_internet_service = int(confirm_internet_service)
                            device.internet_service = num_to_internet_service[confirm_internet_service]
                    else:
                        device.internet_service = num_to_internet_service[internet_service]

            has_cell_phone = self.df['device1a'][i]
            if (not pandas.isna(has_cell_phone)):
                device.has_cell_phone = int(has_cell_phone)
                phone_type = self.df['smart2'][i]
                if (device.has_cell_phone == 1 and not pandas.isna(phone_type)):
                    device.phone_type = int(phone_type)

            has_tablet = self.df['device1b'][i]
            if (not pandas.isna(has_tablet)):
                device.has_tablet = int(has_tablet)

            has_computer = self.df['device1c'][i]
            if (not pandas.isna(has_computer)):
                device.has_computer = int(has_computer)

            has_console = self.df['device1d'][i]
            if (not pandas.isna(has_console)):
                device.has_console = int(has_console)

            device.save()
