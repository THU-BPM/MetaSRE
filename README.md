# Semi-supervised Relation Extraction via Incremental Meta Self-Training

This project provides tools for "Semi-supervised Relation Extraction via Incremental Meta Self-Training." 

Details about SRE are in the paper and the implementation is based on the PyTorch library. 

## Quick Links
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Acknowledgements](#acknowledgements)

## Installation

For training, a GPU is recommended to accelerate the training speed. 

### PyTroch

The code is based on PyTorch 1.2. You can find tutorials [here](https://pytorch.org/tutorials/).

### Dependencies

The code is written in Python 3.5. Its dependencies are summarized in the file ```requirements.txt```. 

torch==1.2.0
numpy==1.18.3
scikit_learn==0.21.3
transformers==2.5.1

You can install these dependencies like this:
```
pip3 install -r requirements.txt
```
## Usage
* Run the full model on SemEval dataset with default hyperparameter settings<br>

```python3 src/train.py```<br>

 
 
## Data
### Format
Each dataset is a folder under the ```./data``` folder:
```
./data
└── SemEval
    ├── train_sentence.json
    ├── train_label_id.json
    ├── dev_sentence.json
    ├── dev_label_id.json
    ├── test_sentence.json
    └── test_label_id.json

```
### Download

* SemEval: SemEval 2010 Task 8 data (included in ```data/SemEval```)<br>
* TACRED: The TAC Relation Extraction Dataset ([download](https://catalog.ldc.upenn.edu/LDC2018T24))<br>

Then use the scripts from ```data/data_prepare.py``` to further preprocess the data. For SemEval, the script split the original training data into two sets. For TACRED, the script first perform some preprocessing to ensure the same format as SemEval.
 
 
## Acknowledgements
https://github.com/huggingface/transformers

https://github.com/INK-USC/DualRE

## Contact

If you have any problem about our code, feel free to contact: hxm19@mails.tsinghua.edu.cn
