# Sediment Grain Size Analysis (Sedimentology lab)
A simple python script I wrote for sediment grain size analysis used in sieve analysis in sedimentology lab.

---

Here is a breif introduction on sediment grain size analysis.

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

The CSV file consists of two columns: one is for the grain size measured in millimeter (mm), and the other is for the weight of each size in gram (g). The script will convert the size (mm) to the Phi unit. The CSV file should be in same directory as the **GSA.py** script. 


![Example of the CSV file with data]()

## Porcess

The script will read the CSV file you provide, and start first with converting the grain size from ***millimeter*** to ***Phi***, second it will calculate the weight percentage for each row, and calculate the cumulcative weight percentage. Once done it will populate a table and print in on screen for you (sorry I did not know how to make it fancy!). 

The final processes involves the script to plot the a ***table***, a ***histogram***, and a ***cumulicative curve***, and then save them as separate ***PDF*** files in the same directory. The also will be saved as ***PDF*** file, but as I mentioned above, it is not fancy, and I will be happy if anyone suggest a way to do so. 




---


# LICENSE

Copyright (c) 2023 Majed Turkistani.

Permission is hereby granted, free of charge, to any person obtaining a copy of this script and associated documentation files, to deal in the Software without restriction for non-commercial purposes, including without limitation the rights to use, copy, modify, merge, publish, and distribute, and to permit persons to whom the script is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


