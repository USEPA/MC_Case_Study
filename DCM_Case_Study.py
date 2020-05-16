# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Importing libraries
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import os
import warnings
warnings.simplefilter(action = 'ignore', category = FutureWarning)
import plotly
import chart_studio.plotly as py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def Maximum_on_site(x):
    if x == 1:
        return 0.453592*np.random.uniform(0,99)
    elif x == 2:
        return 0.453592*np.random.uniform(100,999)
    elif x == 3:
        return 0.453592*np.random.uniform(1000,9999)
    elif x == 4:
        return 0.453592*np.random.uniform(10000,99999)
    elif x == 5:
        return 0.453592*np.random.uniform(100000,999999)
    elif x == 6:
        return 0.453592*np.random.uniform(1000000,9999999)
    elif x == 7:
        return 0.453592*np.random.uniform(10000000,49999999)
    elif x == 8:
        return 0.453592*np.random.uniform(50000000,99999999)
    elif x == 9:
        return 0.453592*np.random.uniform(100000000,499999999)
    elif x == 10:
        return 0.453592*np.random.uniform(500000000,999999999)
    elif x == 11:
        return 0.453592*np.random.uniform(1000000000, 10000000000)
    elif x == 12:
        return 0.001*np.random.uniform(0,0.099)
    elif x == 13:
        return 0.001*np.random.uniform(0.1,0.99)
    elif x == 14:
        return 0.001*np.random.uniform(1,9.99)
    elif x == 15:
        return 0.001*np.random.uniform(10,99)
    elif x == 16:
        return 0.001*np.random.uniform(100,999)
    elif x == 17:
        return 0.001*np.random.uniform(1000,9999)
    elif x == 18:
        return 0.001*np.random.uniform(10000,99999)
    elif x == 19:
        return 0.001*np.random.uniform(100000,999999)
    elif x == 20:
        return 0.001*np.random.uniform(1000000, 100000000)


def Cal(keys, m, w):
    results = {key: 1/(Maximum_on_site(m) + w) for key in keys}
    return results


def Release_code(x):
    if  (x < 0.5):
        return 'O'
    elif (x >= 0.5) and (x <= 10.5):
        return 'A'
    elif (x > 10.5) and (x <= 499.5):
        return 'B'
    elif (x > 499.5) and (x <= 999.5):
        return 'C'
    elif (x > 999.5):
        return 'H'


def values(x):
    if x == 'O':
        return 0
    elif x == 'A':
        return 1
    elif x == 'B':
        return 2
    elif x == 'C':
        return 3
    elif x == 'H':
        return 4


if __name__ == '__main__':

    Sample = 100
    ITN = '5306'
    dir_path = os.path.dirname(os.path.realpath(__file__)) # Current directory


    Path = dir_path + '/TRI_SRS_FRS_RCRAInfo_EPCRA_Compartments_CompTox_3a_2017_EoL.csv'
    columns = ['SENDER TRI PRIMARY NAICS TITLE', 'SRS CHEMICAL ITN',\
           'SENDER CONDITION OF USE', 'QUANTITY TRANSFER OFF-SITE', 'GENERAL WASTE MANAGEMENT', \
           'TYPE OF WASTE MANAGEMENT', 'FINAL HANDLER TRI ID', 'FINAL HANDLER PRIMARY NAICS TITLE', \
           'FINAL HANDLER MAXIMUM AMOUNT ON-SITE', 'TOTAL WASTE GENERATED', \
           'COMPARTMENT', 'FLOW TO COMPARTMENT']
    type = {'SENDER TRI PRIMARY NAICS TITLE':'str',
            'SRS CHEMICAL ITN': 'str',
            'SENDER CONDITION OF USE':'str',
            'QUANTITY TRANSFER OFF-SITE':'float',
            'GENERAL WASTE MANAGEMENT': 'str',
            'TYPE OF WASTE MANAGEMENT':'str',
            'FINAL HANDLER TRI ID':'str',
            'FINAL HANDLER PRIMARY NAICS TITLE':'str',
            'FINAL HANDLER MAXIMUM AMOUNT ON-SITE':'int',
            'TOTAL WASTE GENERATED': 'float',
            'COMPARTMENT':'str',
            'FLOW TO COMPARTMENT':'float'}
    df = pd.read_csv(Path, sep = ',', usecols = columns, low_memory = False, dtype = type, header = 0)

    df_chem = df.loc[df['SRS CHEMICAL ITN'] == ITN]

    df_sankey = df_chem[['SENDER TRI PRIMARY NAICS TITLE',
                    'SENDER CONDITION OF USE',
                    'QUANTITY TRANSFER OFF-SITE',
                    'GENERAL WASTE MANAGEMENT',
                    'TYPE OF WASTE MANAGEMENT',
                    'FINAL HANDLER TRI ID',
                    'FINAL HANDLER MAXIMUM AMOUNT ON-SITE',
                    'TOTAL WASTE GENERATED',
                    'FINAL HANDLER PRIMARY NAICS TITLE',
                    'COMPARTMENT',
                    'FLOW TO COMPARTMENT']]
    # First level (GiS -> CoU)
    df1 = df_sankey[['SENDER TRI PRIMARY NAICS TITLE', 'SENDER CONDITION OF USE', 'QUANTITY TRANSFER OFF-SITE']]
    Total_1 = df1['QUANTITY TRANSFER OFF-SITE'].sum()
    df1['Proportion'] = df1['QUANTITY TRANSFER OFF-SITE'].apply(lambda x: 100*x/Total_1)
    group1 = df1.groupby(['SENDER TRI PRIMARY NAICS TITLE', 'SENDER CONDITION OF USE'], as_index = False).sum()

    # Second level (CoU -> RETDFiS)
    df2 = df_sankey[['SENDER CONDITION OF USE', 'QUANTITY TRANSFER OFF-SITE',
                    'FINAL HANDLER PRIMARY NAICS TITLE']]
    Total_2 = df2['QUANTITY TRANSFER OFF-SITE'].sum()
    df2['Proportion'] = df2['QUANTITY TRANSFER OFF-SITE'].apply(lambda x: 100*x/Total_2)
    group2 = df2.groupby(['SENDER CONDITION OF USE', 'FINAL HANDLER PRIMARY NAICS TITLE'], as_index = False).sum()

    # Third level (RETDFiS -> WMH) and Fourth level  (RETDFiS -> EoL)
    df3 = df_sankey[['QUANTITY TRANSFER OFF-SITE', 'GENERAL WASTE MANAGEMENT',
                     'FINAL HANDLER PRIMARY NAICS TITLE']]
    Total_3 = df3['QUANTITY TRANSFER OFF-SITE'].sum()
    df3['Proportion'] = df3['QUANTITY TRANSFER OFF-SITE'].apply(lambda x: 100*x/Total_3)
    group_aux = df3.groupby(['FINAL HANDLER PRIMARY NAICS TITLE', 'GENERAL WASTE MANAGEMENT'], as_index = False).sum()
    group3 =  group_aux.loc[group_aux['GENERAL WASTE MANAGEMENT'].isin(['Energy recovery', 'Recycling'])]
    group4 =  group_aux.loc[~group_aux['GENERAL WASTE MANAGEMENT'].isin(['Energy recovery', 'Recycling'])]

    # Fifth leve (EoL -> WMH)
    df4 = df_sankey[['QUANTITY TRANSFER OFF-SITE', 'GENERAL WASTE MANAGEMENT',
                     'TYPE OF WASTE MANAGEMENT']]
    df4 =  df4.loc[~df4['GENERAL WASTE MANAGEMENT'].isin(['Energy recovery', 'Recycling'])]
    df4['Proportion'] = df4['QUANTITY TRANSFER OFF-SITE'].apply(lambda x: 100*x/Total_3)
    group5 = df4.groupby(['GENERAL WASTE MANAGEMENT', 'TYPE OF WASTE MANAGEMENT'], as_index = False).sum()

    # Sixth level (WMH -> EC)
    df5 = df_sankey[['QUANTITY TRANSFER OFF-SITE', 'TYPE OF WASTE MANAGEMENT', 'FINAL HANDLER TRI ID', 'FINAL HANDLER MAXIMUM AMOUNT ON-SITE', \
                 'TOTAL WASTE GENERATED', 'COMPARTMENT', 'FLOW TO COMPARTMENT']]
    df_handler_facility = df5[['FINAL HANDLER TRI ID', 'FINAL HANDLER MAXIMUM AMOUNT ON-SITE', \
                                'TOTAL WASTE GENERATED']] \
                            .drop_duplicates(keep = 'first')
    columns_maximum = ['INV MAXIMUM QUANTITY ON-SITE ' + str(N + 1) for N in range(Sample)]
    df_handler_facility = df_handler_facility.merge(\
                        df_handler_facility.apply(lambda s: pd.Series(Cal(columns_maximum,
                                                                          s['FINAL HANDLER MAXIMUM AMOUNT ON-SITE'],
                                                                          s['TOTAL WASTE GENERATED'])), axis = 1),
                        left_index = True, right_index = True)
    df5 = pd.merge(df5, df_handler_facility, how = 'left',
               on = ['FINAL HANDLER TRI ID', 'FINAL HANDLER MAXIMUM AMOUNT ON-SITE',
                    'TOTAL WASTE GENERATED'])
    df5_aux = df5.iloc[:,7:].multiply(df5['QUANTITY TRANSFER OFF-SITE'], axis = 'index')
    df5_aux = df5_aux.multiply(df5['FLOW TO COMPARTMENT'], axis = 'index')
    columns_flow = {'INV MAXIMUM QUANTITY ON-SITE ' + str(N + 1): \
                     'RELEASE TO COMPARTMENT ' + str(N + 1) for N in range(Sample)}
    df5_aux.rename(columns = columns_flow, inplace = True)
    df5 = pd.concat([df5.iloc[:,0:7], df5_aux], axis =  1)
    del df5_aux
    df5['STD FLOW TO COMPARTMENT'] = df5.iloc[:,7:Sample + 7].std(axis = 1)
    df5['MEAN FLOW TO COMPARTMENT'] = df5.iloc[:,7:Sample + 7].mean(axis = 1)
    df6 = df5[['TYPE OF WASTE MANAGEMENT', 'COMPARTMENT', 'MEAN FLOW TO COMPARTMENT']]
    func = {'QUANTITY TRANSFER OFF-SITE': lambda x: 0.25*x.sum(),
            'MEAN FLOW TO COMPARTMENT': lambda x: x.sum()}
    df6_aux = df5[['TYPE OF WASTE MANAGEMENT', 'QUANTITY TRANSFER OFF-SITE', 'MEAN FLOW TO COMPARTMENT']]
    df6_aux = df6_aux.groupby('TYPE OF WASTE MANAGEMENT', as_index = False).agg(func)
    df6_aux['MEAN FLOW TO COMPARTMENT'] = df6_aux.apply(lambda x: x['QUANTITY TRANSFER OFF-SITE'] - x['MEAN FLOW TO COMPARTMENT'], axis = 1)
    df6_aux['COMPARTMENT'] = None
    lb_wm = {'Recycling': 'Recycled', 'Disposal': 'Discarded', 'Treatment': 'Treated', 'Energy recovery': 'Energy'}
    for key, value in lb_wm.items():
        df6_aux.loc[df6_aux['TYPE OF WASTE MANAGEMENT'] == key, 'COMPARTMENT']  = value
    df6_aux = df6_aux[['TYPE OF WASTE MANAGEMENT', 'COMPARTMENT', 'MEAN FLOW TO COMPARTMENT']]
    df6 = pd.concat([df6, df6_aux], axis =  0, ignore_index = True)
    Total_5 = df6['MEAN FLOW TO COMPARTMENT'].sum()
    df6['Proportion'] = df6['MEAN FLOW TO COMPARTMENT'].apply(lambda x: 100*x/Total_5)
    group6 = df6.groupby(['TYPE OF WASTE MANAGEMENT', 'COMPARTMENT'], as_index = False).sum()

    # Generating labels for Sankey diagram
    GiS = {val: 'GiS-' + str(idx + 1) for idx, val \
        in enumerate(list(group1['SENDER TRI PRIMARY NAICS TITLE'].unique()))}
    CoU = {val: 'CoU-' + str(idx + 1) for idx, val \
        in enumerate(list(group1['SENDER CONDITION OF USE'].unique()))}
    RETDFiS = {val: 'RETDFiS-' + str(idx + 1) for idx, val \
        in enumerate(list(group2['FINAL HANDLER PRIMARY NAICS TITLE'].unique()))}
    EoL = {val: 'EoL-' + str(idx + 1) for idx, val \
        in enumerate(list(group4['GENERAL WASTE MANAGEMENT'].unique()))}
    WMH = {val: 'WMH-' + str(idx + 1) for idx, val \
        in enumerate(list(group6['TYPE OF WASTE MANAGEMENT'].unique()))}
    EC = {val: 'EC-' + str(idx + 1) for idx, val \
        in enumerate(list(group6['COMPARTMENT'].unique()))}

    # Saving percentages
    i = 0
    for gr in [group1, group2, group3, group4, group5, group6]:
        i = i + 1
        gr.to_csv(dir_path + '/Percentages_' + str(i) + '.csv', sep = ',', index = False)

    # Saving label names
    TRI = {'Added as a formulation component': 'TRIU. 1',
        'Used as a chemical processing aid': 'TRIU. 2',
        'Repackaging': 'TRIU. 3',
        'Ancillary or other use': 'TRIU. 4',
        'Produce the chemical': 'TRIU. 5',
        'Used as a reactant': 'TRIU. 6',
        'As a process impurity': 'TRIU. 7',
        'Used as a manufacturing aid': 'TRIU. 8',
        'Import the chemical': 'TRIU. 9',
        'Used as an article component': 'TRIU. 10'}
    CoU_aux = {}
    for key, value in CoU.items():
        CoU_aux.update({value: ' + '.join(TRI[e] for e in key.split(' + '))})
    j = 0
    for l in [GiS, TRI, CoU_aux, RETDFiS, EoL, WMH, EC]:
        j = j + 1
        df_aux = pd.DataFrame({'Col 1': list(l.keys()), 'Col 2': list(l.values())})
        df_aux.to_csv(dir_path + '/Label_names_' + str(j) + '.csv', sep = ',', index = False)

    # Levels and colors
    level_1 = list(GiS.values())
    colors_1 = ['#ff5050' for i in range(len(level_1))]
    level_2 = list(CoU.values())
    colors_2 = ['#0066cc' for i in range(len(level_2))]
    level_3 = list(RETDFiS.values())
    colors_3 = ['#009933' for i in range(len(level_3))]
    level_4 = list(EoL.values())
    colors_4 = ['#ff944d' for i in range(len(level_4))]
    level_5 = list(WMH.values())
    colors_5 = ['#ffcc66' for i in range(len(level_5))]
    level_6 = list(EC.values())
    colors_6 = ['#6666ff' for i in range(len(level_6))]
    levels = level_1 + level_2 + level_3 + level_4 + level_5 + level_6
    colors = colors_1 + colors_2 + colors_3 + colors_4 + colors_5 + colors_6

    Sources = []
    Targets = []
    Values = []

    for index, row in group1.iterrows():
        Sources.append(levels.index(GiS[row['SENDER TRI PRIMARY NAICS TITLE']]))
        Targets.append(levels.index(CoU[row['SENDER CONDITION OF USE']]))
        Values.append(row['Proportion'])

    for index, row in group2.iterrows():
        Sources.append(levels.index(CoU[row['SENDER CONDITION OF USE']]))
        Targets.append(levels.index(RETDFiS[row['FINAL HANDLER PRIMARY NAICS TITLE']]))
        Values.append(row['Proportion'])

    for index, row in group3.iterrows():
        Targets.append(levels.index(WMH[row['GENERAL WASTE MANAGEMENT']]))
        Sources.append(levels.index(RETDFiS[row['FINAL HANDLER PRIMARY NAICS TITLE']]))
        Values.append(row['Proportion'])

    for index, row in group4.iterrows():
        Sources.append(levels.index(RETDFiS[row['FINAL HANDLER PRIMARY NAICS TITLE']]))
        Targets.append(levels.index(EoL[row['GENERAL WASTE MANAGEMENT']]))
        Values.append(row['Proportion'])

    for index, row in group5.iterrows():
        Sources.append(levels.index(EoL[row['GENERAL WASTE MANAGEMENT']]))
        Targets.append(levels.index(WMH[row['TYPE OF WASTE MANAGEMENT']]))
        Values.append(row['Proportion'])

    for index, row in group6.iterrows():
        Sources.append(levels.index(WMH[row['TYPE OF WASTE MANAGEMENT']]))
        Targets.append(levels.index(EC[row['COMPARTMENT']]))
        Values.append(row['Proportion'])

    # Sankey diagram
    fig1 = go.Figure(data=[go.Sankey(
            node = dict(
                pad = 35,
                thickness = 5,
                line = dict(
                    color = "black",
                    width = 0),
                label = levels,
                color = colors
                ),
            link = dict(
                source = Sources,
                target = Targets,
                value = Values)
                )])
    fig1.update_layout(plot_bgcolor = '#e8e8e8',
                       paper_bgcolor = '#e8e8e8',
                       width=1000,
                       height=900)
    fig1.write_image(dir_path + '/Sankey_Methylene_Chloride.pdf')

    df_box = df5.iloc[:,[1,5] + list(range(7,Sample + 7))]
    EC_non_cero = list(df_box.loc[~(df_box.iloc[:,2:] == 0.0).all(axis = 1), 'COMPARTMENT'].unique())
    WMH_non_cero = list(df_box.loc[~(df_box.iloc[:,2:] == 0.0).all(axis = 1), 'TYPE OF WASTE MANAGEMENT'].unique())

    df_compartments = {}
    for compartment in EC_non_cero:
        df_compartment = pd.DataFrame(columns = ['Management', 'Flow_log', 'Flow'])
        for management in WMH_non_cero:
            df_EC_WM = df_box.loc[(df_box['COMPARTMENT'] == compartment) & \
                              (df_box['TYPE OF WASTE MANAGEMENT'] == management)]
            n_times = df_EC_WM.shape[0]*Sample
            col = [2.20462*l[0] for l in np.reshape(df_EC_WM.iloc[:,2:].to_numpy(), (n_times, 1))]
            aux = pd.DataFrame(columns = ['Management', 'Flow'])
            aux['Flow'] = pd.Series(col)
            aux['Flow_log']  = np.log(aux['Flow'])
            aux['Management'] = '<b>' + management + '</b>'
            df_compartment = pd.concat([df_compartment, aux], ignore_index = True, axis = 0)
        df_compartments.update({compartment:df_compartment})

    # Box
    color_box = ['#009933', '#ffcc66', '#ff944d', '#ff5050']
    fig2 = go.Figure()

    for idx, compartment in enumerate(EC_non_cero):
        fig2.add_trace(go.Box(
            y = list(df_compartments[compartment]['Flow_log']),
            x = list(df_compartments[compartment]['Management']),
            name = compartment.capitalize(),
            boxmean = True,
            whiskerwidth = 0.1,
            #notchwidth = 0.1,
            marker = dict(
            color = color_box[idx]
                    )
                    ))

    fig2.update_layout(xaxis = dict(title = '<b>Waste management</b>',
                                    zeroline = False),
                       yaxis = dict(title = '<b>Release, log(lb/yr)</b>',
                                    zeroline = False),
                       boxmode='group',
                       paper_bgcolor = '#f5f5f5',
                       plot_bgcolor = '#e8e8e8',
                       width = 1500,
                       height = 1000,
                       shapes = [
                       go.layout.Shape(
                                        type = 'line',
                                        x0 = -0.5,
                                        y0 = np.log(0.5),
                                        x1 = 3.5,
                                        y1 = np.log(0.5),
                                        line = dict(
                                            color = '#6666ff',
                                            width = 2,
                                            dash = 'dot',
                                        ),
                                        ),
                        go.layout.Shape(
                                         type = 'line',
                                         x0 = -0.5,
                                         y0 = np.log(10.5),
                                         x1 = 3.5,
                                         y1 = np.log(10.5),
                                         line = dict(
                                             color = '#6666ff',
                                             width = 2,
                                             dash = 'dot',
                                         ),
                                         ),
                        go.layout.Shape(
                                         type = 'line',
                                         x0 = -0.5,
                                         y0 = np.log(499.5),
                                         x1 = 3.5,
                                         y1 = np.log(499.5),
                                         line = dict(
                                             color = '#6666ff',
                                             width = 2,
                                             dash = 'dot',
                                         ),
                                         ),
                        go.layout.Shape(
                                         type = 'line',
                                         x0 = -0.5,
                                         y0 = np.log(999.5),
                                         x1 = 3.5,
                                         y1 = np.log(999.5),
                                         line = dict(
                                             color = '#6666ff',
                                             width = 2,
                                             dash = 'dot',
                                         ),
                                         )
                       ],
                        legend = go.layout.Legend(
                                        bgcolor = 'White',
                                        bordercolor = '#6666ff',
                                        borderwidth = 1
                            )
                )
    fig2.update_xaxes(title_font=dict(size=18))
    fig2.update_yaxes(title_font=dict(size=20))
    fig2.write_image(dir_path + '/Box_Methylene_Chloride.pdf')

    # Histogram
    df_histogram = pd.DataFrame(columns = ['Management', 'Flow', 'Compartment'])
    for compartment in EC_non_cero:
        df_histogram_aux = df_compartments[compartment][['Management', 'Flow']]
        df_histogram_aux['Management'] = df_histogram_aux['Management'].apply(lambda x: x.replace('<b>','').replace('</b>',''))
        df_histogram_aux['Compartment'] = compartment
        df_histogram = pd.concat([df_histogram, df_histogram_aux], axis = 0)

    df_histogram['Relese code'] = df_histogram.apply(lambda x: Release_code(x['Flow']), axis = 1)
    df_histogram['Order'] = df_histogram['Relese code'].apply(lambda x: values(x))
    df_histogram.sort_values(by=['Order'], ascending = True, inplace = True)

    color_box = ['#009933', '#ffcc66', '#ff944d', '#ff5050']
    trace = []
    for compartment in EC_non_cero:
        for idx, management in enumerate(WMH_non_cero):
            data = list(df_histogram.loc[(df_histogram['Compartment'] == compartment) & \
                                         (df_histogram['Management'] == management), 'Relese code'])
            if len(trace) < len(WMH_non_cero):
                trace.append(go.Histogram(histnorm = 'probability density',
                                        x = data,
                                        name = management,
                                        marker_color = color_box[idx],
                                        opacity = 0.75,
                                        autobinx = False))
            else:
                trace.append(go.Histogram(histnorm = 'probability density',
                                        x = data,
                                        marker_color = color_box[idx],
                                        opacity = 0.75,
                                        showlegend = False))

    n_EC = len(EC_non_cero)
    n_WMH = len(WMH_non_cero)
    titles = tuple(ec.capitalize() for ec in EC_non_cero)
    if n_EC < 4:
        fig3 = make_subplots(rows = n_EC, cols = 1,
                            shared_xaxes = True,
                            subplot_titles = titles)
        n_trace = 0
        row = 0
        for tr in trace:
            n_trace =  n_trace + 1
            if (n_trace - 1) % n_WMH == 0:
                row = row + 1
            fig3.append_trace(tr, row, 1)
    else:
        fig3 = make_subplots(rows = 2, cols = 2,
                            shared_xaxes = True,
                            subplot_titles = titles)
        n_trace = 0
        row = 1
        col = 1
        n_fig = 0
        for tr in trace:
            n_trace += 1
            if (n_trace - 1) % n_WMH == 0:
                n_fig += 1
                if n_fig == 1:
                    row = 1
                    col = 1
                elif n_fig == 2:
                    row = 1
                    col = 2
                elif n_fig == 3:
                    row = 2
                    col = 1
                else:
                    row = 2
                    col = 2
            fig3.append_trace(tr, row, col)

    fig3.update_layout(paper_bgcolor = '#f5f5f5',
                        plot_bgcolor = '#e8e8e8',
                        legend = go.layout.Legend(
                                        bgcolor = 'White',
                                        bordercolor = '#6666ff',
                                        borderwidth = 1))
    fig3.write_image(dir_path + '/Histogram_Methylene_Chloride.pdf')
