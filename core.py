import os


def run_pipeline():
    # 1. تحديد مسار ملف config.lua
    # تم تعديل المسار ليتناسب مع مجلد الصور الظاهر في جهازك
    lua_path = "/storage/emulated/0/Pictures/pkoi/config.lua"

    # إذا لم يجد المجلد هناك، سيبحث في المجلد الحالي
    if not os.path.exists(lua_path):
        lua_path = os.path.join("pkoi", "config.lua")

    if not os.path.exists(lua_path):
        print(
            f"❌ خطأ: لم يتم العثور على ملف config.lua. تأكد من وجود مجلد pkoi وبداخله الملف."
        )
        return

    # 2. قراءة واستخراج المهام من ملف الـ Lua
    tasks = {}
    with open(lua_path, "r", encoding="utf-8") as file:
        current_var = None
        for line in file:
            line = line.strip()
            if not line or line.startswith("--"):
                continue

            if "=" in line and "{" in line:
                current_var = line.split("=")[0].replace("local", "").strip()
                tasks[current_var] = []
            elif current_var and "{" in line and "}" in line:
                clean_line = (
                    line.replace("{", "").replace("}", "").replace(",", "")
                )
                nums = [int(x) for x in clean_line.split() if x.isdigit()]
                if nums:
                    tasks[current_var].append(nums)
            elif line in ["}", "};"]:
                current_var = None

    # 3. محاكاة خوارزمية C++ (ترتيب الأرقام داخلياً وترتيب الصفوف حسب الأهمية/الوقت)
    sorted_tasks = {}
    for task_name, matrix in tasks.items():
        if not matrix:
            continue

        processed_matrix = []
        for row in matrix:
            # ترتيب الأرقام داخل الصف نفسه تصاعدياً (مثل كود C++)
            sorted_row = sorted(row)
            processed_matrix.append(sorted_row)

        # ترتيب الصفوف بالكامل بناءً على أول عنصر (مثل كود C++)
        processed_matrix.sort()
        sorted_tasks[task_name] = processed_matrix

    # 4. ترتيب المتغيرات الخارجية أبجدياً
    final_output = dict(sorted(sorted_tasks.items()))

    # 5. طباعة النتيجة النهائية المنسقة في الـ Console بشكل احترافي
    print("\n" + "=" * 45)
    print("📋  قائمة المهام والواجبات المرتبة تلقائياً  📋")
    print("=" * 45)

    for name, matrix in final_output.items():
        print(f"\n🔹 المهمة: {name.upper()}")
        print("-" * 30)
        for row in matrix:
            formatted_row = " | ".join(map(str, row))
            print(f"  [ {formatted_row} ]")
        print("-" * 30)

    print("\n" + "=" * 45)


if __name__ == "__main__":
    run_pipeline()
