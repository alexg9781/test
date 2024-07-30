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

​       or

​       pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0

​      '''

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
    python calculate_euclidean_distances.py
    '''

8. **If the following result appears, then the execution is successful.**

  [[     0.          11436.11267685   5523.41425002 ...  32786.29385924
    149033.54055248  51266.32091459]
   [ 11436.11267685      0.          15202.80175711 ...  43128.04830739
    138355.0315513   40472.23208718]
   [  5523.41425002  15202.80175711      0.         ...  29286.29176064
    152742.21034724  55014.65092303]
   ...
   [ 32786.29385924  43128.04830739  29286.29176064 ...      0.
    181483.01270955  83600.08291104]
   [149033.54055248 138355.0315513  152742.21034724 ... 181483.01270955
         0.          97883.03151523]
   [ 51266.32091459  40472.23208718  55014.65092303 ...  83600.08291104
     97883.03151523      0.        ]]
  Euclidean Distances Calculated