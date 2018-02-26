import qrcode
import image


class QRCreator:

    separator = '0x1D'
    notFound = 'NULL'
    end_of_message = 'EOT'
    message_header = '[]>'
    null_check = str(-1)
    message = '[]>'
    message_block = ''

    def __init__(self, odometerRead, fuelEconomy, fuelLevel1,engineHours,fuelUsed, niin, serialNumber):
        self.odometerRead = odometerRead
        self.fuelEconomy = fuelEconomy
        self.fuelLevel1 = fuelLevel1
        self.engineHours = engineHours
        self.fuelUsed = fuelUsed
        self.niin = niin
        self.serialNumber = serialNumber
        self.data = [str(self.odometerRead),str(self.fuelEconomy),str(self.fuelLevel1), str(self.engineHours),str(self.fuelUsed),str(self.niin),str(self.serialNumber)]

    def display(self):
        print(qrcode.constants.ERROR_CORRECT_H)
        qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

        for x in range(0, 7):
            if self.data[x] == '-1':
                self.data[x] = self.notFound

        for x in range(0, 7):
            length = len(self.data[x])
            if x != 6:
                zero_count = 9 - length
                for y in range(0, zero_count):
                    self.message_block = self.message_block + '0'
                self.message_block = self.message_block + self.data[x]
            else:
                zero_count = 6 - length
                for y in range(0, zero_count):
                    self.message_block = self.message_block + '0'
                self.message_block = self.message_block + self.data[x]
            self.message = self.message + self.message_block
            if x != 6:
                self.message = self.message + self.separator
            else:
                self.message = self.message + self.end_of_message
            self.message_block = ''

        print(self.message)

        qr.add_data(self.message)
        qr.make(fit=True)

        img = qr.make_image()

        img.save("image.jpg")
        img.show()




