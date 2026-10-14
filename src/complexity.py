def algorithm_complexities():
    return {
        "Merge Sort": {
            "Time": "O(n log n)",
            "Space": "O(n)",
            "Amortized": "Not applicable",
            "Expected": "O(n log n)"
        },
        "Greedy Selection": {
            "Time": "O(n log n)",
            "Space": "O(n)",
            "Amortized": "Not applicable",
            "Expected": "O(n log n)"
        },
        "Dynamic Programming": {
            "Time": "O(n × M)",
            "Space": "O(M)",
            "Amortized": "Not applicable",
            "Expected": "O(n × M)"
        },
        "Backtracking": {
            "Time": "O(2^n)",
            "Space": "O(n)",
            "Amortized": "Not applicable",
            "Expected": "Depends on pruning"
        },
        "Branch and Bound": {
            "Time": "O(2^n) worst case",
            "Space": "O(n)",
            "Amortized": "Not applicable",
            "Expected": "Usually lower with pruning"
        }
    }