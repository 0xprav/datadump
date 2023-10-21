import streamlit as st

import seaborn as sns

import bittensor as bt



st.title("subnet 4")


# print thinking while this loads
neurons = bt.metagraph(netuid=4).neurons

st.write(neurons)



# Iterate over the neurons and add their coldkeys to the set
unique_coldkeys = list(set(neuron.coldkey for neuron in neurons if (
    neuron.validator_trust == 0 and neuron.total_stake < 400
)))
st.write(unique_coldkeys, len(unique_coldkeys))# Correcting the keys method call and converting the generator to a list before passing to st.write


# st.write(neurons)