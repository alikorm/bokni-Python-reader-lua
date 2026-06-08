import os

# 1. طباعة مجلد العمل الحالي لمعرفة أين يبحث بايثون
print(f"بايثون يبحث حالياً داخل هذا المجلد العام:")
print(f"📂 {os.getcwd()}\n")

# 2. اكتب هنا المسار الكامل (الكامل) للملف على جهازك إذا لم يعمل المسار التلقائي
# مثال لو ويندوز: "C:/Users/YourName/Desktop/pkoi/config.lua"
# مثال لو موبايل/أندرويد: "/storage/emulated/0/pkoi/config.lua"
MANUAL_PATH = ""

# تحديد المسار التلقائي
folder_name = "name folder"
file_name = "name The file that will be read in Lua language "
default_path = os.path.join(folder_name, file_name)

# اختيار المسار الفعلي المتوفر
file_path = MANUAL_PATH if MANUAL_PATH else default_path

if not os.path.exists(file_path):
    print(f"❌ خطأ: لم يتم العثور على الملف في المسار: {os.path.abspath(file_path)}")
    print("💡 الحل: انسخ المسار الحقيقي للملف من جهازك وضعه في متغير MANUAL_PATH في السطر رقم 9.")
else:
    print(f"✅ تم العثور على الملف بنجاح في: {file_path}")
    
    # قراءة وتنظيف النص واستخراج المصفوفات مباشرة
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    data_dict = {}
    current_var = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith("--"):
            continue
        
        # التقاط اسم المصفوفة
        if "=" in line and "{" in line:
            var_name = line.split("=")[0].replace("local", "").strip()
            current_var = var_name
            data_dict[current_var] = []
        
        # التقاط الأرقام داخل الصفوف
        elif current_var and "{" in line and "}" in line:
            clean_num = line.replace("{", "").replace("}", "").replace(",", "")
            nums = [int(x) for x in clean_num.split() if x.isdigit()]
            if nums:
                data_dict[current_var].append(nums)
                
        if line == "}" or line == "};":
            current_var = None

    # ترتيب المتغيرات والمصفوفات داخلياً
    sorted_result = {}
    for k, v in sorted(data_dict.items()):
        if v:
            v.sort() # ترتيب الصفوف الداخلية
            sorted_result[k] = v

    print("\n📊 النتيجة بعد الترتيب التلقائي:")
    for var, matrix in sorted_result.items():
        print(f"{var} = {matrix}")
