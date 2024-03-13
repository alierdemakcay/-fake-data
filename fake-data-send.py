import requests

def send_data_to_site(url, data_size, repeat):
    for i in range(repeat):
        data = b'0' * data_size  # Gönderilecek veri, istenilen byte sayısı kadar sıfır byte'ından oluşur
        headers = {'Content-Type': 'application/octet-stream'}  # Veri türünü belirtmek için başlık

        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            print("{}. veri başarıyla gönderildi!".format(i + 1))
        else:
            print("{}. veri gönderilirken bir hata oluştu. Durum kodu: {}".format(i + 1, response.status_code))

# Örnek kullanım:
target_url = 'http://example.com'  # Hedef site adresi
byte_count = 6500000  # Gönderilecek her bir verinin boyutu
repeat_count = 100000  # Kaç kere gönderileceği

send_data_to_site(target_url, byte_count, repeat_count)
