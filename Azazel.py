
import requests

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# مثال على استخدام الدالة
ip_address = "8.8.8.8"
ip_info = get_ip_info(ip_address)
if ip_info:
    print(f"معلومات عنوان IP {ip_address}:")
    print(f"الدولة: {ip_info[ country ]}")
    print(f"المنطقة: {ip_info[ regionName ]}")
    print(f"المدينة: {ip_info[ city ]}")
    # ومعلومات أخرى يمكن الوصول إليها
else:
    print(f"تعذر الحصول على معلومات عنوان IP {ip_address}")
