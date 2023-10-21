import streamlit as st

import seaborn as sns

import bittensor as bt

from collections import defaultdict

import pandas as pd

import matplotlib.pyplot as plt

st.title("subnet 4")


# print thinking while this loads
neurons = bt.metagraph(netuid=4).neurons

st.write(neurons)



# Iterate over the neurons and add their coldkeys to the set
unique_coldkeys = list(set(neuron.coldkey for neuron in neurons if (
    neuron.validator_trust == 0 and neuron.total_stake < 400
)))

coldkey_to_uids = defaultdict(set)



for neuron in neurons:
    if neuron.coldkey in unique_coldkeys:
        # For each neuron, add the uid to the set corresponding to the coldkey
        coldkey_to_uids[neuron.coldkey].add(neuron.uid)

# Now, let's count the number of unique uids for each coldkey
coldkey_uid_counts = {coldkey: len(uids) for coldkey, uids in coldkey_to_uids.items()}


# st.write(coldkey_uid_counts)

data = pd.DataFrame(list(coldkey_uid_counts.items()), columns=['ColdKey', 'UID_Count'])
# st.write the data ordered by uid count
data = data.sort_values(by=['UID_Count'], ascending=False)

plt.figure(figsize=(10, 8))  # You might need to adjust the size depending on your preference
plt.pie(data['UID_Count'], labels=data['ColdKey'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("viridis", len(data)))
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.title('Distribution of Unique UIDs per ColdKey')



st.table(data)
st.pyplot(plt)
