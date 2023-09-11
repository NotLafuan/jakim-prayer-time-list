import requests

zone_list = {
    "Johor": {
        "JHR01": "Pulau Aur dan Pulau Pemanggil ",
        "JHR02": "Johor Bahru, Kota Tinggi, Mersing",
        "JHR03": "Kluang, Pontian",
        "JHR04": "Batu Pahat, Muar, Segamat, Gemas Johor"
    },
    "Kedah": {
        "KDH01": "Kota Setar, Kubang Pasu, Pokok Sena (Daerah Kecil)",
        "KDH02": "Kuala Muda, Yan, Pendang",
        "KDH03": "Padang Terap, Sik",
        "KDH04": "Baling",
        "KDH05": "Bandar Baharu, Kulim",
        "KDH06": "Langkawi",
        "KDH07": "Puncak Gunung Jerai"
    },
    "Kelantan": {
        "KTN01": "Bachok, Kota Bharu, Machang, Pasir Mas, Pasir Puteh, Tanah Merah, Tumpat, Kuala Krai, Mukim Chiku",
        "KTN03": "Gua Musang (Daerah Galas Dan Bertam), Jeli"
    },
    "Melaka": {
        "MLK01": "SELURUH NEGERI MELAKA"
    },
    "Negeri Sembilan": {
        "NGS01": "Tampin, Jempol",
        "NGS02": "Jelebu, Kuala Pilah, Port Dickson, Rembau, Seremban"
    },
    "Pahang": {
        "PHG01": "Pulau Tioman",
        "PHG02": "Kuantan, Pekan, Rompin, Muadzam Shah",
        "PHG03": "Jerantut, Temerloh, Maran, Bera, Chenor, Jengka",
        "PHG04": "Bentong, Lipis, Raub",
        "PHG05": "Genting Sempah, Janda Baik, Bukit Tinggi",
        "PHG06": "Cameron Highlands, Genting Higlands, Bukit Fraser"
    },
    "Perlis": {
        "PLS01": "Kangar, Padang Besar, Arau"
    },
    "Pulau Pinang": {
        "PNG01": "Seluruh Negeri Pulau Pinang"
    },
    "Perak": {
        "PRK01": "Tapah, Slim River, Tanjung Malim",
        "PRK02": "Kuala Kangsar, Sg. Siput (Daerah Kecil), Ipoh, Batu Gajah, Kampar",
        "PRK03": "Lenggong, Pengkalan Hulu, Grik",
        "PRK04": "Temengor, Belum",
        "PRK05": "Kg Gajah, Teluk Intan, Bagan Datuk, Seri Iskandar, Beruas, Parit, Lumut, Sitiawan, Pulau Pangkor",
        "PRK06": "Selama, Taiping, Bagan Serai, Parit Buntar",
        "PRK07": "Bukit Larut"
    },
    "Sabah": {
        "SBH01": "Bahagian Sandakan (Timur), Bukit Garam, Semawang, Temanggong, Tambisan, Bandar Sandakan, Sukau",
        "SBH02": "Beluran, Telupid, Pinangah, Terusan, Kuamut, Bahagian Sandakan (Barat)",
        "SBH03": "Lahad Datu, Silabukan, Kunak, Sahabat, Semporna, Tungku, Bahagian Tawau  (Timur)",
        "SBH04": "Bandar Tawau, Balong, Merotai, Kalabakan, Bahagian Tawau (Barat)",
        "SBH05": "Kudat, Kota Marudu, Pitas, Pulau Banggi, Bahagian Kudat",
        "SBH06": "Gunung Kinabalu",
        "SBH07": "Kota Kinabalu, Ranau, Kota Belud, Tuaran, Penampang, Papar, Putatan, Bahagian Pantai Barat",
        "SBH08": "Pensiangan, Keningau, Tambunan, Nabawan, Bahagian Pendalaman (Atas)",
        "SBH09": "Beaufort, Kuala Penyu, Sipitang, Tenom, Long Pa Sia, Membakut, Weston, Bahagian Pendalaman (Bawah)"
    },
    "Selangor": {
        "SGR01": "Gombak, Petaling, Sepang, Hulu Langat, Hulu Selangor, S.Alam",
        "SGR02": "Kuala Selangor, Sabak Bernam",
        "SGR03": "Klang, Kuala Langat"
    },
    "Sarawak": {
        "SWK01": "Limbang, Lawas, Sundar, Trusan",
        "SWK02": "Miri, Niah, Bekenu, Sibuti, Marudi",
        "SWK03": "Pandan, Belaga, Suai, Tatau, Sebauh, Bintulu",
        "SWK04": "Sibu, Mukah, Dalat, Song, Igan, Oya, Balingian, Kanowit, Kapit",
        "SWK05": "Sarikei, Matu, Julau, Rajang, Daro, Bintangor, Belawai",
        "SWK06": "Lubok Antu, Sri Aman, Roban, Debak, Kabong, Lingga, Engkelili, Betong, Spaoh, Pusa, Saratok",
        "SWK07": "Serian, Simunjan, Samarahan, Sebuyau, Meludam",
        "SWK08": "Kuching, Bau, Lundu, Sematan",
        "SWK09": "Zon Khas (Kampung Patarikan)"
    },
    "Terengganu": {
        "TRG01": "Kuala Terengganu, Marang, Kuala Nerus",
        "TRG02": "Besut, Setiu",
        "TRG03": "Hulu Terengganu",
        "TRG04": "Dungun, Kemaman"
    },
    "Wilayah Persekutuan": {
        "WLY01": "Kuala Lumpur, Putrajaya",
        "WLY02": "Labuan"
    }
}

date_dict = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}


def get_data(zone) -> dict[str, list[dict[str, str]]]:
    url = 'https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=year&zone={}'
    data = requests.get(url.format(zone))
    return data.json()


def get_location(_zone):
    for state in zone_list:
        for zone in zone_list[state]:
            if zone == _zone:
                return (zone_list[state][zone])
    return False


def date2number(date: str):
    for name, number in date_dict.items():
        date = date.replace(name, number)
    return date


def read_json(zone: str):
    text = f'{zone} - {get_location(zone)}'
    text += '\nTarikh\tImsak\tSubuh\tSyuruk\tZohor\tAsar\tMaghrib\tIsyak\n'
    prayerTimes = ['imsak', 'fajr', 'syuruk',
                   'dhuhr', 'asr', 'maghrib', 'isha']
    data = get_data(zone=zone)
    for day in data['prayerTime']:
        date = date2number(day['date'])
        text += date+'\t'
        for prayerTime in prayerTimes:
            text += day[prayerTime][:-3] + '\t'
        text = text.strip()+'\n'
    return text


if __name__ == '__main__':
    print('https://gist.github.com/lomotech/b25cde7118adf5e7a1fea4ce6cfce259#file-esolat-md')
    zone = input('Enter your zone: ')
    text = read_json(zone)
    with open(f'{zone}.txt', "w+") as f:
        f.write(text)
