-- مهارات وtasks (بدون كلمة local لكي يراها بايثون)
create_robot = {
     {1, 2, 3},
     {4, 5, 6},
     {7, 8, 9}
}

create_app = {
     {1, 2, 3},
     {4, 5, 6},
     {7, 8, 9}
}

create_file = {
     {1, 2, 3},
     {4, 5, 6},
     {7, 8, 9}
}

create_dsighen = {
     {1, 2, 3},
     {4, 5, 6},
     {7, 8, 9}
}

-- الشروط الأصلية الخاصة بك (تترك كما هي)
if create_robot[2][3] == 6 then print("create_robot") else print("error") end
if create_app[2][3] == 6 then print("create_app") else print("error") end
if create_file[2][3] == 6 then print("create_file") else print("error") end
if create_dsighen[2][3] == 6 then print("create_dsighen") else print("error") end

-- السطر الأهم: إرجاع البيانات في جدول لتراها مكتبة بايثون
return {
    create_robot = create_robot,
    create_app = create_app,
    create_file = create_file,
    create_dsighen = create_dsighen
}
