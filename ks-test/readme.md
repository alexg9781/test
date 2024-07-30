1. **Download Anaconda and VSCode from the official website**
[Anaconda](https://www.anaconda.com/)
[VScode](https://code.visualstudio.com/)

2. **To create a conda virtual environment, enter the following command in the terminal:**
'''
conda create -n env_name python=3.8
conda activate env_name
'''

3. **To change the download source for Anaconda, enter the following commands in the terminal sequentially:**
'''
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
'''

4. **Download PyTorch from the official website. Enter the following command in the terminal and wait for the installation to complete. You can also download the GPU version depending on your computer's specifications.**
'''
conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 cpuonly -c pytorch
'''

5. **In the terminal, type python and press Enter. Then enter the following commands one by one. If the following result appears, it means that the CPU version of PyTorch was successfully installed. Type exit() to exit Python and return to the terminal.**
'''
>>> import torch
>>> print("PyTorch version:", torch.__version__)
PyTorch version: 2.3.0
>>> x = torch.rand(5, 3)
>>> print("Random tensor:", x)
Random tensor: tensor([[0.0039, 0.6368, 0.9655],
        [0.3554, 0.9148, 0.2935],
        [0.8078, 0.1329, 0.1267],
        [0.5031, 0.6805, 0.7101],
        [0.7396, 0.8218, 0.4764]])
>>> exit()

6. **Install the related packages**
'''
pip install -r requirements.txt
'''

7. **To run the ks_test.py file or enter the following code in the terminal:**
'''
python ks_test.py
'''
8. **If the following result appears, then the execution is successful.**
Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv
Loading file: ./数据/YB003_DS
Processing key: 40
Columns in DataFrame: RangeIndex(start=0, stop=600, step=1)
没有公共的列，无法执行检验
Processing key: 30
Columns in DataFrame: RangeIndex(start=0, stop=450, step=1)
没有公共的列，无法执行检验
Processing key: 80
Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1)
没有公共的列，无法执行检验
Processing key: 100
Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1)
没有公共的列，无法执行检验
Processing key: 90
Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1)
没有公共的列，无法执行检验
Processing key: 10
Columns in DataFrame: RangeIndex(start=0, stop=150, step=1)
没有公共的列，无法执行检验
Processing key: 70
Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1)
没有公共的列，无法执行检验
Processing key: 50
Columns in DataFrame: RangeIndex(start=0, stop=750, step=1)
没有公共的列，无法执行检验
Processing key: 20
Columns in DataFrame: RangeIndex(start=0, stop=300, step=1)
没有公共的列，无法执行检验
Processing key: 60
Columns in DataFrame: RangeIndex(start=0, stop=900, step=1)
没有公共的列，无法执行检验
{40: {}, 30: {}, 80: {}, 100: {}, 90: {}, 10: {}, 70: {}, 50: {}, 20: {}, 60: {}}