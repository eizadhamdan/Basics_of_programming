/*
 * This program is a GUI-based solution for the Knapsack problem, including both
 * the 0/1 Knapsack problem and the Fractional Knapsack problem. It uses Swing for
 * the user interface. Users can input the number of items, their weights, and values.
 * The program then calculates the maximum profit that can be obtained given a knapsack
 * with a specific capacity. The 0/1 Knapsack problem is solved using dynamic programming,
 * while the Fractional Knapsack problem is solved using a greedy algorithm. The steps
 * to reach the solution are displayed in a text area within the GUI.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

// Class representing an item with a weight and value (profit)
class Item {
    int weight;
    int value;

    // Constructor to initialize an item's weight and value
    Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }

    // Overriding the toString method to display item information
    @Override
    public String toString() {
        return "Weight: " + weight + ", Profit: " + value;
    }
}

// Class for solving the 0/1 Knapsack problem using dynamic programming
class Knapsack {
    private int n; // Number of items
    private int capacity; // Maximum capacity of the knapsack
    private ArrayList<Item> items; // List to store items
    private int[][] dp; // DP table to store maximum profit for subproblems

    // Constructor to initialize the knapsack with given capacity and number of items
    Knapsack(int capacity, int n) {
        this.capacity = capacity;
        this.n = n;
        this.items = new ArrayList<>();
        this.dp = new int[n][capacity + 1];
        // Initialize DP table with -1 (indicating uncomputed subproblems)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= capacity; j++) {
                dp[i][j] = -1;
            }
        }
    }

    // Method to add an item to the knapsack
    void addItem(int weight, int value) {
        items.add(new Item(weight, value));
    }

    // Recursive method to compute the maximum profit using dynamic programming
    int getMaxProfit(int cap, int index, JTextArea stepsArea) {
        if (index < 0)
            return 0; // Base case: no items left
        if (dp[index][cap] != -1)
            return dp[index][cap]; // Return precomputed result if available

        // Case 1: Do not select the current item
        int select = getMaxProfit(cap, index - 1, stepsArea);
        int notSelect = Integer.MIN_VALUE;

        // Case 2: Select the current item (only if it fits in the knapsack)
        if (cap >= items.get(index).weight) {
            notSelect = items.get(index).value + getMaxProfit(cap - items.get(index).weight, index - 1, stepsArea);
        }

        // Store the result in the DP table
        dp[index][cap] = Math.max(select, notSelect);

        // Log the steps for solving
        stepsArea.append("Considering item " + (index + 1) + ": Weight = " + items.get(index).weight + ", Profit = " + items.get(index).value + "\n");
        stepsArea.append("Maximum profit at capacity " + cap + " is " + dp[index][cap] + "\n\n");

        return dp[index][cap];
    }

    // Method to calculate the maximum profit for the entire knapsack
    int profitCalculator(JTextArea stepsArea) {
        if (n == 1) {
            // Special case: only one item
            if (capacity >= items.get(0).weight) {
                return items.get(0).value;
            } else {
                return 0;
            }
        }
        return getMaxProfit(capacity, n - 1, stepsArea); // Compute profit starting from the last item
    }

    // Method to get the list of items in the knapsack
    ArrayList<Item> getItems() {
        return items;
    }
}

// Class for solving the Fractional Knapsack problem using a greedy algorithm
class FractionalKnapsack {
    public static double getMaxValue(Item[] arr, int capacity, JTextArea stepsArea) {
        // Sort items by value-to-weight ratio in descending order
        Arrays.sort(arr, new Comparator<Item>() {
            @Override
            public int compare(Item item1, Item item2) {
                double cpr1 = (double) item1.value / (double) item1.weight;
                double cpr2 = (double) item2.value / (double) item2.weight;

                if (cpr1 < cpr2)
                    return 1;
                else
                    return -1;
            }
        });

        // Log the sorted items
        stepsArea.append("Items sorted by profit-to-weight ratio:\n");
        for (Item i : arr) {
            stepsArea.append("Item: Weight = " + i.weight + ", Profit = " + i.value + ", Ratio = " + (double) i.value / i.weight + "\n");
        }
        stepsArea.append("\n");

        double totalValue = 0d; // Total value of items in the knapsack

        // Iterate through the sorted items and add them to the knapsack
        for (Item i : arr) {
            int curWt = (int) i.weight;
            int curVal = (int) i.value;

            if (capacity - curWt >= 0) {
                // If the entire item can be added, add it
                capacity = capacity - curWt;
                totalValue += curVal;

                stepsArea.append("Added entire item: Weight = " + curWt + ", Profit = " + curVal + "\n");
                stepsArea.append("Remaining capacity = " + capacity + ", Total profit = " + totalValue + "\n\n");
            } else {
                // If only part of the item can be added, add a fraction of it
                double fraction = ((double) capacity / (double) curWt);
                totalValue += (curVal * fraction);

                stepsArea.append("Added fraction of item: Weight = " + curWt + ", Fraction = " + fraction + ", Profit added = " + (curVal * fraction) + "\n");
                stepsArea.append("Knapsack is now full. Total profit = " + totalValue + "\n");

                break; // Knapsack is full, break out of the loop
            }
        }
        return totalValue;
    }
}

// Main class to create the GUI and handle user interactions
public class KnapsackGUI {
    private JFrame frame;
    private JTextField nInput;
    private JTextField capacityInput;
    private JTextField weightInput;
    private JTextField valueInput;
    private JScrollPane itemsScrollPane;
    private JScrollPane stepsScrollPane;
    private Knapsack knapsack;
    private int itemCount = 0; // Counter for the number of items added

    public static void main(String[] args) {
        SwingUtilities.invokeLater(KnapsackGUI::new); // Start the GUI in the Event Dispatch Thread
    }

    public KnapsackGUI() {
        // Create and set up the main frame for the GUI
        frame = new JFrame("Solve the Knapsack Problem");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        frame.setLayout(null);
        Color newColor = new Color(216, 180, 254); // Background color for the frame
        frame.getContentPane().setBackground(newColor);

        // Label and input field for the number of items
        JLabel nLabel = new JLabel("Number of items:");
        nLabel.setBounds(10, 10, 150, 25);
        frame.add(nLabel);

        nInput = new JTextField();
        nInput.setBounds(250, 10, 100, 25);
        frame.add(nInput);

        // Label and input field for the maximum capacity of the knapsack
        JLabel capacityLabel = new JLabel("Maximum capacity of knapsack:");
        capacityLabel.setBounds(10, 40, 240, 25);
        frame.add(capacityLabel);

        capacityInput = new JTextField();
        capacityInput.setBounds(250, 40, 100, 25);
        frame.add(capacityInput);

        // Label and input field for the weight of an item
        JLabel weightLabel = new JLabel("Weight:");
        weightLabel.setBounds(10, 90, 60, 25);
        frame.add(weightLabel);

        weightInput = new JTextField();
        weightInput.setBounds(70, 90, 150, 25);
        frame.add(weightInput);

        // Label and input field for the value (profit) of an item
        JLabel valueLabel = new JLabel("Profit:");
        valueLabel.setBounds(240, 90, 50, 25);
        frame.add(valueLabel);

        valueInput = new JTextField();
        valueInput.setBounds(290, 90, 150, 25);
        frame.add(valueInput);

        // Button to add an item to the knapsack
        JButton addButton = new JButton("Add the item");
        addButton.setBounds(180, 120, 170, 25);
        addButton.setBackground(Color.LIGHT_GRAY);
        addButton.setForeground(Color.BLACK);
        frame.add(addButton);

        // Button to calculate the maximum profit using the 0/1 Knapsack algorithm
        JButton calculateButton = new JButton("0/1 Knapsack");
        calculateButton.setBounds(10, 170, 180, 25);
        calculateButton.setBackground(Color.BLUE);
        calculateButton.setForeground(Color.WHITE);
        frame.add(calculateButton);

        // Button to calculate the maximum profit using the Fractional Knapsack algorithm
        JButton calculateFractionalButton = new JButton("Fractional Knapsack");
        calculateFractionalButton.setBounds(200, 170, 180, 25);
        calculateFractionalButton.setBackground(Color.BLUE);
        calculateFractionalButton.setForeground(Color.WHITE);
        frame.add(calculateFractionalButton);

        // Text area to display the items added by the user
        JLabel itemsAreaLabel = new JLabel("Items available");
        itemsAreaLabel.setBounds(10, 210, 150, 25);
        frame.add(itemsAreaLabel);

        JTextArea itemsArea = new JTextArea();
        itemsArea.setEditable(false);
        itemsScrollPane = new JScrollPane(itemsArea);
        itemsScrollPane.setBounds(10, 235, 350, 100);
        frame.add(itemsScrollPane);

        // Text area to display the steps to solve the knapsack problem
        JLabel stepsAreaLabel = new JLabel("Steps to solve");
        stepsAreaLabel.setBounds(10, 340, 150, 25);
        frame.add(stepsAreaLabel);

        JTextArea stepsArea = new JTextArea();
        stepsArea.setEditable(false);
        stepsScrollPane = new JScrollPane(stepsArea);
        stepsScrollPane.setBounds(10, 365, 550, 150);
        frame.add(stepsScrollPane);

        // Event listener for the "Add the item" button
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (knapsack == null) {
                    // Initialize the knapsack when the first item is added
                    int n = Integer.parseInt(nInput.getText());
                    int capacity = Integer.parseInt(capacityInput.getText());
                    knapsack = new Knapsack(capacity, n);
                }

                // Get the weight and value from the input fields and add the item
                int weight = Integer.parseInt(weightInput.getText());
                int value = Integer.parseInt(valueInput.getText());
                knapsack.addItem(weight, value);
                itemCount++;

                // Clear the input fields after adding the item
                weightInput.setText("");
                valueInput.setText("");

                // Display the added item in the items area
                itemsArea.append("Item " + itemCount + ": Weight = " + weight + ", Profit = " + value + "\n");

                // Disable the add button when all items have been added
                if (itemCount == Integer.parseInt(nInput.getText())) {
                    addButton.setEnabled(false);
                }
            }
        });

        // Event listener for the "0/1 Knapsack" button
        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (knapsack != null) {
                    stepsArea.setText(""); // Clear previous steps
                    int maxProfit = knapsack.profitCalculator(stepsArea); // Calculate the maximum profit
                    stepsArea.append("Maximum Profit (0/1 knapsack): " + maxProfit + "\n");
                }
            }
        });

        // Event listener for the "Fractional Knapsack" button
        calculateFractionalButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (knapsack != null) {
                    stepsArea.setText(""); // Clear previous steps
                    Item[] itemsArray = new Item[knapsack.getItems().size()];
                    itemsArray = knapsack.getItems().toArray(itemsArray); // Convert items list to array
                    double maxValue = FractionalKnapsack.getMaxValue(itemsArray, Integer.parseInt(capacityInput.getText()), stepsArea); // Calculate the maximum value
                    stepsArea.append("Maximum Profit (Fractional Knapsack): " + maxValue + "\n");
                }
            }
        });

        frame.setVisible(true); // Display the GUI
    }
}
