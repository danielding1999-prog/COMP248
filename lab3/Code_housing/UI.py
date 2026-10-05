#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 22:16:00 2025

@author: Vaishali Siddeshwar
"""

class TerminalUI:
    def __init__(self, controller):
        self.controller = controller

    def start(self):
        """Starts the interactive terminal screen loop."""
        print("==========================================")
        print("   CALIFORNIA HOUSING PRICE PREDICTOR     ")
        print("==========================================")
        
        while True:
            print("\nPlease enter housing details for prediction:")
            
            try:
                # 1. Collect inputs and bundle into a dictionary (Going down)
                sample_data = {
                    "longitude": float(input("  Longitude (e.g., -122.23): ")),
                    "latitude": float(input("  Latitude (e.g., 37.88): ")),
                    "housing_median_age": float(input("  Housing Median Age (e.g., 41.0): ")),
                    "total_rooms": float(input("  Total Rooms (e.g., 880.0): ")),
                    "total_bedrooms": float(input("  Total Bedrooms (e.g., 129.0): ")),
                    "population": float(input("  Population (e.g., 322.0): ")),
                    "households": float(input("  Households (e.g., 126.0): ")),
                    "median_income": float(input("  Median Income (e.g., 8.3252): ")),
                    "ocean_proximity": input("  Ocean Proximity (NEAR BAY, <1H OCEAN, INLAND, NEAR OCEAN, ISLAND): ").strip().upper()
                }

                # 2. Pass to controller and receive output price (Two-way street)
                predicted_price = self.controller.predict_single_instance(sample_data)
                
                # 3. Display result back on screen (Coming back up)
                print("\n------------------------------------------")
                print(f"  PREDICTED HOUSE VALUE: ${predicted_price:,.2f}")
                print("------------------------------------------")

            except ValueError:
                print("\n[Error] Invalid input format. Please enter numerical values for numeric fields.")

            choice = input("\nWould you like to predict another house? (y/n): ").strip().lower()
            if choice != 'y':
                print("Exiting Housing Price Predictor. Goodbye!")
                break