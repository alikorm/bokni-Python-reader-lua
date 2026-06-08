#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

// دالة لتنظيف وتقسيم النصوص
vector<int> parse_row(string row_str) {
    vector<int> row;
    stringstream ss(row_str);
    int num;
    while (ss >> num) {
        row.push_back(num);
    }
    return row;
}

int main() {
    string task_name;
    // قراءة البيانات المرسلة من بايثون سطر بسطر
    while (cin >> task_name) {
        if (task_name == "END") break;

        int rows_count;
        cin >> rows_count;
        cin.ignore(); // تخطي السطر الجديد

        vector<vector<int>> matrix;
        for (int i = 0; i < rows_count; ++i) {
            string line;
            getline(cin, line);
            vector<int> row = parse_row(line);
            
            // ترتيب الأرقام داخل الصف نفسه تصاعدياً
            sort(row.begin(), row.end());
            matrix.push_back(row);
        }

        // ترتيب الصفوف بالكامل داخل المهمة حسب أول عنصر
        sort(matrix.begin(), matrix.end());

        // إرسال النتيجة المرتبة مجدداً إلى بايثون
        cout << "TASK:" << task_name << endl;
        for (const auto& row : matrix) {
            // التعديل الصحيح للسطر الذي تسبب في الخطأ
            for (size_t i = 0; i < row.size(); ++i) {
                cout << row[i] << (i == row.size() - 1 ? "" : " ");
            }
            cout << endl;
        }
        cout << "TASK_END" << endl;
    }
    return 0;
}
