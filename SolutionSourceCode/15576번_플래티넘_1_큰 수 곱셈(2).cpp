#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

const double PI = std::acos(-1);

// 재귀적인 FFT 함수 정의
void fft(std::vector<std::complex<double>>& a) {
    int n = a.size();
    if (n <= 1) return;

    // 짝수 인덱스와 홀수 인덱스를 위한 벡터 생성
    std::vector<std::complex<double>> even(n / 2);
    std::vector<std::complex<double>> odd(n / 2);
    for (int i = 0; i < n / 2; ++i) {
        even[i] = a[i * 2];
        odd[i] = a[i * 2 + 1];
    }

    // 재귀적으로 FFT 수행
    fft(even);
    fft(odd);

    // 결합 과정
    double ang = 2 * PI / n;
    std::complex<double> w(1);
    std::complex<double> wn(std::cos(ang), std::sin(ang));
    for (int i = 0; i < n / 2; ++i) {
        a[i] = even[i] + w * odd[i];
        a[i + n / 2] = even[i] - w * odd[i];
        w *= wn;
    }
}

// 역 FFT 함수 정의
void ifft(std::vector<std::complex<double>>& a) {
    int n = a.size();
    if (n <= 1) return;

    // 짝수 인덱스와 홀수 인덱스를 위한 벡터 생성
    std::vector<std::complex<double>> even(n / 2);
    std::vector<std::complex<double>> odd(n / 2);
    for (int i = 0; i < n / 2; ++i) {
        even[i] = a[i * 2];
        odd[i] = a[i * 2 + 1];
    }

    // 재귀적으로 IFFT 수행
    ifft(even);
    ifft(odd);

    // 결합 과정
    double ang = -2 * PI / n;
    std::complex<double> w(1);
    std::complex<double> wn(std::cos(ang), std::sin(ang));
    for (int i = 0; i < n / 2; ++i) {
        a[i] = even[i] + w * odd[i];
        a[i + n / 2] = even[i] - w * odd[i];
        w *= wn;
    }

    // 스케일링
    if (n > 1) {
        for (auto& x : a) {
            x /= 2;
        }
    }
}

// 두 벡터를 곱하는 함수 정의 (주파수 영역에서 곱셈)
std::vector<std::complex<double>> multiply(const std::vector<std::complex<double>>& a, const std::vector<std::complex<double>>& b) {
    int N = a.size();
    std::vector<std::complex<double>> result(N);
    for (int i = 0; i < N; ++i) {
        result[i] = a[i] * b[i];
    }
    return result;
}

// 두 큰 수의 곱셈을 처리하는 함수
std::vector<int> multiplyLargeNumbers(const std::vector<int>& num1, const std::vector<int>& num2) {
    // 입력 신호를 복소수 벡터로 변환하고 크기를 맞춤
    int n1 = num1.size();
    int n2 = num2.size();
    int N = 1;
    while (N < n1 + n2) N <<= 1;

    std::vector<std::complex<double>> a(N, 0), b(N, 0);
    for (int i = 0; i < n1; ++i) a[i] = num1[n1 - 1 - i];
    for (int i = 0; i < n2; ++i) b[i] = num2[n2 - 1 - i];

    // FFT 수행
    fft(a);
    fft(b);

    // 주파수 영역에서 곱셈 수행
    std::vector<std::complex<double>> c = multiply(a, b);

    // IFFT 수행
    ifft(c);

    // 결과를 정수 벡터로 변환하고 자리올림 처리
    std::vector<int> result(N);
    int carry = 0;
    for (int i = 0; i < N; ++i) {
        int value = static_cast<int>(std::round(c[i].real())) + carry;
        result[i] = value % 10;
        carry = value / 10;
    }

    // 불필요한 앞자리 0 제거
    while (result.size() > 1 && result.back() == 0) {
        result.pop_back();
    }

    // 결과를 역순으로 반환
    std::reverse(result.begin(), result.end());
    return result;
}

void ActualProcess(std::istream& input) {
    std::string number_1, number_2;
    input >> number_1 >> number_2;

    std::vector<int> num1(number_1.size());
    std::vector<int> num2(number_2.size());

    for (size_t i = 0; i < number_1.size(); ++i) {
        num1[i] = number_1[i] - '0';
    }

    for (size_t i = 0; i < number_2.size(); ++i) {
        num2[i] = number_2[i] - '0';
    }

    // 큰 수의 곱셈 수행
    std::vector<int> result = multiplyLargeNumbers(num1, num2);

    // 결과 출력
    for (int digit : result) {
        std::cout << digit;
    }
    std::cout << std::endl;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    ActualProcess(std::cin);

    return 0;
}