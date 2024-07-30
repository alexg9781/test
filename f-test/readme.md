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

7. **To run the ftest.py file or enter the following code in the terminal:**
'''
python ftest.py
'''

8. **If the following result appears, then the execution is successful.**
Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv
Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv
Processing real_data
Columns in real_data: Index(['Unnamed: 0', 'Admn001_ID', 'Demo001_Gender', 'Demo002_Age',
       'Demo003_ReAd', 'Vitl001_GCS', 'Vitl002_HR', 'Vitl003_SysBP',
       'Vitl004_MeanBP', 'Vitl005_DiaBP', 'Vitl006_RR', 'Vitl007_SpO2',
       'Vitl008_Temp', 'Labs001_K', 'Labs002_Na', 'Labs003_Cl',
       'Labs004_Glucose', 'Labs005_BUN', 'Labs006_Creatinine', 'Labs007_Mg',
       'Labs008_Ca', 'Labs009_IonisedCa', 'Labs010_CO2', 'Labs011_SGOT',
       'Labs012_SGPT', 'Labs013_TotalBili', 'Labs014_Albumin', 'Labs015_Hb',
       'Labs016_WbcCount', 'Labs017_PlateletsCount', 'Labs018_PTT',
       'Labs019_PT', 'Labs020_INR', 'Labs021_pH', 'Labs022_PaO2',
       'Labs023_PaCO2', 'Labs024_BE', 'Labs025_HCO3', 'Labs026_Lactate',
       'Vent001_Mech', 'Vent002_FiO2', 'Flud001_InputTotal', 'Flud002_Input4H',
       'Flud003_MaxVaso', 'Flud004_OutputTotal', 'Flud005_Output4H',
       'Devr001_SOFA', 'Devr002_SIRS', 'Devr003_ShockIndex',
       'Devr004_PaFiRatio', 'Devr005_FluidBalance'],
      dtype='object')
   Unnamed: 0  Admn001_ID  Demo001_Gender   Demo002_Age  Demo003_ReAd  ...  Devr001_SOFA  Devr002_SIRS  Devr003_ShockIndex  Devr004_PaFiRatio  Devr005_FluidBalance
0   17.348774   17.597944             inf  5.418081e+01  2.985876e+01  ...      4.888063      5.069649            7.029627          14.934811              2.717342
1    0.000031    0.000027             0.0  1.887744e-13  4.693368e-08  ...      0.027052      0.024357            0.008022           0.000112              0.099276