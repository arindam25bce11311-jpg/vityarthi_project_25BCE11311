# vityarthi_project_25BCE11311
VITYARTHI PROJECT ON HARVEST SCHEDULER 
Harvest Planner
A lightweight, Python-based command-line application designed to assist farmers in managing crop cycles. This tool replaces paper logs with a digital system to track planting dates, harvest targets, and production quantities, ensuring critical agricultural data is never lost.

Key Features -
Crop Registration: Easily log new crops with details including name, planting date, harvest date, and quantity.

Persistent Storage: Automatically saves all data to a local CSV file (crops_sched.csv), ensuring data survives program restarts.

Schedule Management: View a consolidated list of all active crops.

Data Safety: Includes error handling to prevent crashes from invalid inputs and "safe delete" logic to ensure the correct crop is removed.

Offline Capable: Runs entirely locally without the need for an internet connection.

Technologies Used -
Language: Python 3.x

Libraries: csv (Data handling), os (File checks), datetime (Date logic)

Architecture: Modular CLI with Layered Architecture
