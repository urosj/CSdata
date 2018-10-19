# Install virtualenv
$ pip3 install --user --upgrade virtualenv

## Create virtualenv
$ virtualenv -p python3 $name
$ source ./$name/bin/activate

# Install packages
pip install --upgrade jupyter matplotlib numpy pandas scipy scikit-learn
pip install --upgrade requests

## Check installation 
python -c "import jupyter, matplotlib, numpy, pandas, scipy, sklearn"

jupyter notebook
