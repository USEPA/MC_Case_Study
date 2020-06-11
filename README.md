# MC Case Study

This code was written to support the case study for *Methylene Chloride* for the paper named ***Data engineering for tracking chemicals and releases at industrial end-of-life activities***.

## Requirements

The following Python libraries are required for running the code:

1. numpy (https://pypi.org/project/numpy/)
2. plotly (https://pypi.org/project/plotly/)
3. pandas (https://pypi.org/project/pandas/)

## How to use

The Python Script requires the EoL_database_for_MC.csv to run the case study for Methylene Chloride. The EoL_database_for_MC.csv is composed of the following data entries according to Table S2 in the Supporting Information:

| Data name | Data type<sup>[1](#myfootnote1)</sup> |
| ------------- | ------------- |
| Generator primary NAICS name  | Alphanumeric  |
| SRS chemical ID  | Integer  |
| Generator condition of use  | Alphanumeric  |
| Quantity transferred by generator  | Float  |
| EoL activity category under TSCA  | Alphanumeric |
| EoL activity category under TSCA  | Alphanumeric |
| EoL activity category under waste management hierarchy | Alphanumeric |
| RETDF TRIF ID | Alphanumeric |
| RETDF primary NAICS name | Alphanumeric |
| Maximum amount of chemical present at RETDF | Integer |
| Total chemical generated as waste by RETDF | Float |
| Environmental compartment | Alphanumeric |
| RETDF chemical flow releases to the compartment | Float |
| RETDF total chemical release | Float |

To run the Python script, you need to navigate to the directory containing the .py and .csv files. Then, you execute the following command either on Windows CMD or Unix terminal:

```
python MC_Case_Study.py
```

## Outputs

After running the Python script you obtain the following files:

| File name | Description |
| ------------- | ------------- |
| Sankey_5306.pdf | 6-level Sankey diagram  for the case study, Figure 6  |
| Box_5306.pdf  | Box plot for the case study, Figure 7  |
| Histogram_5306.pdf  | Histogram for the case study, Figure 8  |
| Label_names_5306_#.csv<sup>[2](#myfootnote2)</sup> | Label names for the levels in the Sankey diagram |
| Percentages_5306_#.csv<sup>[3](#myfootnote3)</sup> | Percentages/fractions for the levels in the Sankey diagram |

## Disclaimer

The views expressed in this article are those of the authors and do not necessarily represent the views or policies of
the USEPA. Any mention of trade names, products, or services does not imply an endorsement by the U.S.
Government or the USEPA. The USEPA does not endorse any commercial products, service, or enterprises.

## Acknowledgement

This research was supported in by an appointment for Jose D. Hernandez-Betancur to the Research Participation
Program at the Center for Environmental Solutions and Emergency Response, Office of Research and Development,
USEPA, administered by the Oak Ridge Institute for Science and Education through an Interagency Agreement
between the U.S. Department of Energy and the USEPA.

#### ------------------------------------------------------------------------------------------------------------------------

<a name="myfootnote1">1</a>: The data entries of float type are in **kg**.

<a name="myfootnote2">2</a>: They are 7 files.

<a name="myfootnote3">3</a>: They are 6 files.

