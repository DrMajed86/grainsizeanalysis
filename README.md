# Sediment Grain Size Analysis (Sedimentology lab)
A simple Python script I wrote for sediment grain size analysis used in sieve analysis in the sedimentology lab.

---

Here is a brief introduction to sediment grain size analysis.

---

## Introduction to Sediment Grain Size Analysis

**Sediment grain size analysis** is a fundamental technique in sedimentology that plays a crucial role in unraveling the history and conditions of Earth's past environments. This method involves the characterization of sediment particles based on their size, shape, and composition. It provides valuable insights into ancient environments, such as depositional processes, energy conditions, and environmental changes over time. By examining grain sizes, sedimentologists can infer information about paleoenvironments, including:

1. **Depositional Environments:** Grain size analysis helps us identify whether sediments were deposited in high-energy environments (e.g., riverbeds or coastal areas) or low-energy settings (e.g., lakes or deep-sea basins). This knowledge is vital for reconstructing past landscapes.

2. **Climatic Conditions:** Changes in grain size can be indicative of variations in climate, including temperature, precipitation, and erosion rates. Coarser sediments may suggest more vigorous transport under arid conditions, while finer sediments may indicate quiet periods with increased sediment settling.

3. **Sea Level Fluctuations:** By examining sediment grain sizes in different stratigraphic layers, researchers can discern shifts in sea level, which have profound implications for paleogeography and paleoclimate reconstructions.

4. **Paleoecology:** Sediment grain size analysis can shed light on the ecosystems that existed in ancient environments. Different grain sizes can influence the habitats and niches available to organisms.


---


# Instructions

## CSV File:

The CSV file consists of two columns: one is for the grain size measured in millimeters (mm), and the other is for the weight of each size in grams (g). The script will convert the size (mm) to the Phi unit. The CSV file should be in the same directory as the **GSA.py** script. 


#### This is an example of working Data for the GSA

| Grain Size (mm) | Weight (g) |
| :-------------: | :--------: |
| 2               | 12.31      |
| 1               | 18.65      |
| 0.5             | 25.25      |
| 0.25            | 37.63      |
| 0.125           | 5.63       |
| 0.063           | 80.94      |
| 0.031           | 45.25      |


## Porcess

The script will read the CSV file you provide, and start first with converting the grain size from ***millimeter*** to ***Phi***, second it will calculate the weight percentage for each row, and calculate the cumulative weight percentage. Once done it will populate a table and print it on screen for you (sorry I did not know how to make it fancy!). 

The final process involves the script to plot the ***table***, a ***histogram***, and a *** cumulative curve***, and then save them as separate ***PDF*** files in the same directory. They also will be saved as ***PDF*** files, but as I mentioned above, it is not fancy, and I will be happy if anyone suggests a way to do so. 

![Example of a printed Table](https://github.com/DrMajed86/grainsizeanalysis/blob/d54c1b3e791d2ab5c2f0580955d6bdc85ade0ab1/grain_size_calculation.jpg)

![Example of a printed Histogram](https://github.com/DrMajed86/grainsizeanalysis/blob/d54c1b3e791d2ab5c2f0580955d6bdc85ade0ab1/grain_size_distribution.jpg)

![Example of a printed Cumulative Curve](https://github.com/DrMajed86/grainsizeanalysis/blob/d54c1b3e791d2ab5c2f0580955d6bdc85ade0ab1/cumulative_grain_size_distribution.jpg)


---


# LICENSE

Copyright (c) 2023 Majed Turkistani.

Permission is hereby granted, free of charge, to any person obtaining a copy of this script and associated documentation files, to deal in the Software without restriction for non-commercial purposes, including without limitation the rights to use, copy, modify, merge, publish, and distribute, and to permit persons to whom the script is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


