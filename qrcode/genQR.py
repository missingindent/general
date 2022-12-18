import configparser
import qrcode

cfg = configparser.ConfigParser()
cfg.read('config.ini')
# print(cfg['General']['Test'])

def main():
    
    # Encoding Data
    img = qrcode.make(cfg['QR']['URL'])
    
    # Saving as Image File
    img.save(cfg['QR']['File'])

if __name__ == "__main__":
    main()
