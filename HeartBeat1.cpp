#include <iostream>
#include <thread>
#include <chrono>

// Function to clear the console screen
void clearScreen() {
#ifdef _WIN32
    std::system("cls");
#else
    std::system("clear");
#endif
}

// Function to display the heart at different sizes
void displayHeart(int size) {
    if (size == 1) {
        std::cout << "  **   **  \n";
        std::cout << " ****** ** \n";
        std::cout << "  ******   \n";
        std::cout << "   ****    \n";
        std::cout << "    **     \n";
    } else {
        std::cout << "   **     **   \n";
        std::cout << " ****** ****** \n";
        std::cout << "**************\n";
        std::cout << " ************ \n";
        std::cout << "  **********  \n";
        std::cout << "    ******    \n";
        std::cout << "     ****     \n";
        std::cout << "      **      \n";
    }
}

// Function to simulate the beating heart
void beatHeart() {
    while (true) {
        clearScreen();
        displayHeart(1);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));

        clearScreen();
        displayHeart(2);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}

int main() {
    beatHeart();
    return 0;
}
