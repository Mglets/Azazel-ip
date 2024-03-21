
import requests

print("مرحبًا بك في الأداة! قم بإدخال عنوان IP للحصول على المعلومات.")

ip = input("عنوان IP: ")

try:
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()

    # استخراج المعلومات التي ترغب في عرضها من الاستجابة
    country = data["country"]
    city = data["city"]
    isp = data["isp"]

    # عرض المعلومات
    print(f"الدولة: {country}")
    print(f"المدينة: {city}")
    print(f"مزود الخدمة: {isp}")
except:
    print("حدث خطأ أثناء إرسال عنوان IP. يرجى التأكد من صحة عنوان IP وإعادة المحاولة.")
