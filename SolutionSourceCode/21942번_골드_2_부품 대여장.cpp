#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <map>
#include <sstream>
#include <iomanip>

struct BurrowItem {
    long long borrow_time;
    std::string user;

    BurrowItem(long long time, const std::string& user_name)
        : borrow_time(time), user(user_name) {}
};

int getMonthDays(int month) {
    static const int days_in_month[] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
    return days_in_month[month - 1];
}

long long convertToMinutes(const std::string& date_str, const std::string& time_str) {
    int year = 2021, month, day, hour, minute;
    char sep;

    // 날짜 파싱
    std::istringstream date_ss(date_str);
    date_ss >> year >> sep >> month >> sep >> day;

    // 시간 파싱
    std::istringstream time_ss(time_str);
    time_ss >> hour >> sep >> minute;

    // 날짜를 총 일수로 변환
    int total_days = 0;
    for (int m = 1; m < month; ++m) {
        total_days += getMonthDays(m);
    }
    total_days += day - 1; // 현재 일 제외

    // 총 분 계산
    long long total_minutes = static_cast<long long>(total_days) * 24 * 60
                            + hour * 60 + minute;

    return total_minutes;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N, F;
    char sep;

    long long L;
    int days, hours, minutes;

    std::string L_str;
    std::cin >> N >> L_str >> F;

    // 대여 기간 파싱 (DDD/hh:mm)
    {
        std::replace(L_str.begin(), L_str.end(), '/', ' ');
        std::replace(L_str.begin(), L_str.end(), ':', ' ');
        std::istringstream L_ss(L_str);
        L_ss >> days >> hours >> minutes;
    }

    L = static_cast<long long>(days) * 24 * 60 + hours * 60 + minutes;

    std::unordered_map<std::string, BurrowItem> items;
    std::map<std::string, long long> user_fine_ledge;

    for (int i = 0; i < N; ++i) {
        std::string date_info, time_info, item_name, user_name;
        std::cin >> date_info >> time_info >> item_name >> user_name;

        long long current_time = convertToMinutes(date_info, time_info);

        auto it = items.find(item_name + "_" + user_name);
        if (it == items.end()) {
            // 대여
            items.emplace(item_name + "_" + user_name, BurrowItem(current_time, user_name));
        } else {
            // 반납
            long long borrow_time = it->second.borrow_time;
            long long elapsed_minutes = current_time - borrow_time;

            if (elapsed_minutes > L) {
                long long fine = (elapsed_minutes - L) * F;
                user_fine_ledge[it->second.user] += fine;
            }

            items.erase(it);
        }
    }

    if (!user_fine_ledge.empty()) {
        for (const auto& [user, fine] : user_fine_ledge) {
            std::cout << user << " " << fine << '\n';
        }
    } else {
        std::cout << -1 << '\n';
    }

    return 0;
}
