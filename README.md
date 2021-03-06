# MC Case Study

This code was written to support the case study for *Methylene Chloride* for the paper named [***Data engineering for tracking chemicals and releases at industrial end-of-life activities***](https://www.sciencedirect.com/science/article/abs/pii/S0304389420322603). 

<sup>[1](#myfootnote1)</sup>

<p align="center">
  <img src=https://github.com/jodhernandezbe/MC_Case_Study/blob/master/Tracking_chemical_flows_at_industrial_end-of-use_stage.png width="80%">
</p>


## Requirements

This code was written using Python 3.x, Anaconda 3, and operating system Ubuntu 18.04. The following Python libraries are required for running the code:

1. numpy (https://pypi.org/project/numpy/)
2. plotly (https://pypi.org/project/plotly/)
3. pandas (https://pypi.org/project/pandas/)
4. psutil (https://pypi.org/project/psutil/)
5. requests (https://pypi.org/project/requests/)
6. plotly-orca (https://anaconda.org/plotly/plotly-orca)

## How to use

The Python Script requires the EoL_dataset_for_MC.csv, which is in the folder output, to run the case study for Methylene Chloride. The EoL_dataset_for_MC.csv is composed of the following data entries according to Table S2 in the Supporting Information for the abovementioned journal paper:

| Data name | Data type<sup>[2](#myfootnote2)</sup> |
| ------------- | ------------- |
| Generator primary NAICS name  | Alphanumeric  |
| SRS chemical ID  | Integer  |
| Generator condition of use  | Alphanumeric  |
| Quantity transferred by generator  | Float  |
| EoL activity category under TSCA  | Alphanumeric |
| EoL activity category under waste management hierarchy | Alphanumeric |
| RETDF TRIF ID | Alphanumeric |
| RETDF primary NAICS name | Alphanumeric |
| Maximum amount of chemical present at RETDF | Integer |
| Total chemical generated as waste by RETDF | Float |
| Environmental compartment | Alphanumeric |
| RETDF chemical flow releases to the compartment | Float |
| RETDF total chemical release | Float |

To run the Python script, you need to navigate to the directory containing main.py. Then, you execute the following command either on Windows CMD or Unix terminal:

```
python main.py
```
  
## Outputs

After running the Python script you obtain an output folder with the following files:

| File name | Description |
| ------------- | ------------- |
| Sankey_5306.pdf | 6-level Sankey diagram  for the case study, Figure 6  |
| Box_5306.pdf  | Box plot for the case study, Figure 7  |
| Histogram_5306.pdf  | Histogram for the case study, Figure 8  |
| Label_names_5306_#.csv<sup>[3](#myfootnote3)</sup> | Label names for the levels in the Sankey diagram |
| Percentages_5306_#.csv<sup>[4](#myfootnote4)</sup> | Percentages/fractions for the levels in the Sankey diagram |

## Disclaimer

The views expressed in this article are those of the authors and do not necessarily represent the views or policies of
the U.S. Environmental Protection Agency. Any mention of trade names, products, or services does not imply an endorsement by the U.S.
Government or the U.S. Environmental Protection Agency. The U.S. Environmental Protection Agency does not endorse any commercial products, service, or enterprises.

## Acknowledgement

This research was supported in by an appointment for Jose D. Hernandez-Betancur to the Research Participation
Program at the Center for Environmental Solutions and Emergency Response, Office of Research and Development,
U.S. Environmental Protection Agency, administered by the Oak Ridge Institute for Science and Education through an Interagency Agreement No. DW-89-92433001 between the U.S. Department of Energy and the U.S. Environmental Protection Agency. The authors express their sincere gratitude and appreciation to Sandra D. Gaona, Mitchell Sumner and Steve DeVito of the USEPA???s Toxics Release Inventory Program, for their critical review of draft versions of our manuscripts, their recommendations, and insightful discussions.

-----------------------------------------------------------------------------------------------------------------------------

<a name="myfootnote1">1</a>: Recycling, energy recovery, treatment & disposal facility (RETDF).

<a name="myfootnote2">2</a>: The data entries of float type are in **kg/yr**.

<a name="myfootnote3">3</a>: They are 7 files.

<a name="myfootnote4">4</a>: They are 6 files.
