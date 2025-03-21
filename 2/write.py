import numpy as np
import pandas as pd
import streamlit as st

st.write(
    '実戦での見習い魔法使いの死亡率は知っているでしょ．',
    ['一般攻撃魔法','服が透けて見える魔法','服の汚れをきれいさっぱり落とす魔法'],
    pd.DataFrame(np.random.rand(2,3))
)