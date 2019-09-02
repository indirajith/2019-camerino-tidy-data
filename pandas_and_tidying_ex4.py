merged_data = pd.merge(sampleruns.reset_index(drop=True), mutations.reset_index(drop=True), how='left', on=['Strain ID', 'Population', 'Generation'])
