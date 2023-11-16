import pandas as pd


def get_first_value(values):
    res = ''
    for i in values:
        if i != 0 and i != 0 and i != '0':
            res = i
            break
    return res



first_file = pd.read_excel('Attorney spreadsheet dcbar.xlsx')
sec_file = pd.read_excel('Attorney spreadsheet mdcourts (1).xlsx')
third_file = pd.read_excel('Attorney spreadsheet vsb.xlsx')
fourth_file = pd.read_csv('result.csv')
fourth_file.to_excel('result_converted.xlsx', index=False)

first_file = first_file.fillna('')
sec_file = sec_file.fillna('')
third_file = third_file.fillna('')
fourth_file = fourth_file.fillna('')

merged_df = pd.concat([fourth_file, first_file, sec_file, third_file])
grouped_df = merged_df.groupby('lawyer_name').agg({'state licensed in': lambda x: " ".join(x),
                                                   'grad_year': lambda x: get_first_value(x),
                                                   'undergrad school': lambda x: " ".join(x),
                                                   'undergrad_year': lambda x: get_first_value(x),
                                                   'current_position': lambda x: " ".join(x),
                                                   'current_employer': lambda x: " ".join(x),
                                                   'current_city': lambda x: " ".join(x),
                                                   'current_state': lambda x: " ".join(x),
                                                   'type_of_law': lambda x: " ".join(x),
                                                   'email': lambda x: " ".join(x),
                                                   'phone': lambda x: " ".join(x),
                                                   'ref_url': lambda x: " ".join(x),
                                                   'img_url': lambda x: " ".join(x),
                                                   }).reset_index()
grouped_df.drop_duplicates(subset='lawyer_name', keep=False, inplace=False)
grouped_df.to_excel('merged_file.xlsx', index=False)
