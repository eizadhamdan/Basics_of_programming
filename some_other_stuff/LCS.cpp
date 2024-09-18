#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


std::string longestCommonSubsequence(std::string text1, std::string text2);

int main() 
{
    std::cout << "Find the longest common subsequence between two strings." << std::endl;

    // std::string text1 = "abcde";
    // std::string text2 = "ace";
    std::string text1, text2;
    
    std::cout << "Enter the first string: ";
    std::cin >> text1;

    std::cout << "Enter the second string: ";
    std::cin >> text2;

    std::string subsequence = longestCommonSubsequence(text1, text2);
    std::cout << "Longest Common Subsequence: " << subsequence << std::endl;

    return 0;
}

std::string longestCommonSubsequence(std::string text1, std::string text2) 
{
    int a = text1.size();
    int b = text2.size();
    
    // Create a 2D vector initialized with zeros
    std::vector<std::vector<int>> x(a + 1, std::vector<int>(b + 1, 0));

    // Fill the DP table using bottom-up approach
    for (int i = a - 1; i >= 0; --i) 
    {
        for (int j = b - 1; j >= 0; --j) 
        {
            if (text1[i] == text2[j]) 
            {
                x[i][j] = x[i + 1][j + 1] + 1;
            } 
            else 
            {
                x[i][j] = std::max(x[i + 1][j], x[i][j + 1]);
            }
        }
    }
    
    // Reconstruct the longest common subsequence
    std::string lcs;
    int i = 0, j = 0;
    while (i < a && j < b) 
    {
        if (text1[i] == text2[j]) 
        {
            lcs += text1[i];
            i++;
            j++;
        } 
        else if (x[i + 1][j] > x[i][j + 1]) 
        {
            i++;
        } 
        else 
        {
            j++;
        }
    }
    
    return lcs;
}
