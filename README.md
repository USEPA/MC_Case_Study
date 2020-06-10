# MC Case Study

This code was written to support the case study for *Methylene Chloride* for the paper named ***Data engineering for tracking chemicals and releases at industrial end-of-life activities***.

## Requirements

The following Python libraries are required for running the code:

1. numpy (https://pypi.org/project/numpy/)
2. plotly (https://pypi.org/project/plotly/)
3. pandas (https://pypi.org/project/pandas/)

## Use

The Python Script requires the EoL_database_for_MC.csv to run the case study for Methylene Chloride. The EoL_database_for_MC.csv is composed by the following data entries according to Table S2 in the Supporting Information:

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

<a name="myfootnote1">1</a>: The data entries of float type are in **kg**
