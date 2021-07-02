# The effect of shape and illumination on material perception: model and applications
Code for Siggraph 2021 paper: The effect of shape and illumination on material perception: model and applications.
<div align="center">  
  
# A Similarity Measure for Material Appearance   
[![Project page](https://img.shields.io/badge/-Project%20page-blue)](http://mig.mpi-inf.mpg.de/)
[![Paper](https://img.shields.io/badge/Paper-PDF-red)]()
[![Conference](https://img.shields.io/badge/SIGGRAPH-2021-green)]()
[![Journal](https://img.shields.io/badge/TOG-2021-green)]()

</div>

![alt text][teaser]

[teaser]: https://github.com/Hans1984/material-illumination-geometry/blob/main/images/teaser.png "Robots teaser"

## Abstract   
Material appearance hinges on material reflectance properties but also surface geometry and illumination. The unlimited number of potential combinations between these factors makes understanding and predicting material appearance a very challenging task. In this work, we collect a large-scale dataset of perceptual ratings of appearance attributes with more than 215,680 responses for 42,120 distinct combinations of material, shape, and illumination. The goal of this dataset is twofold. First, we analyze for the first time the effects of illumination and geometry in material perception across such a large collection of varied appearances. We connect our findings to those of the literature, discussing how previous knowledge generalizes across very diverse materials, shapes, and illuminations. Second, we use the collected dataset to train a deep learning architecture for predicting perceptual attributes that correlate with human judgments. We demonstrate the consistent and robust behavior of our predictor in various challenging scenarios, which, for the first time, enables estimating perceived material attributes from general 2D images. Since the predictor relies on the final appearance in an image, it can compare appearance properties across different geometries and illumination conditions. Finally, we demonstrate several applications that use our predictor, including appearance reproduction using 3D printing, BRDF editing by integrating our predictor in a differentiable renderer, illumination design, or material recommendations for scene design.

## Setting it up   
_Note that this has been tested using python 3.7_

### Dependencies
First, clone and install dependencies   
```bash
# clone project   
git clone https://github.com/mlagunas/material-appearance-similarity.git   

cd material-appearance-similarity 
pip install scipy numpy matplotlib umap-learn Pillow
# install pytorch/torchvision (https://pytorch.org)
 ```   

Get model pretrained weights
- download model [weights](https://drive.google.com/file/d/1lAkmIRTLgFXjgO5PQ7NNOCYQeNh0JH-N/view?usp=sharing)
- _(optional)_ download [all images](https://drive.google.com/file/d/1v7hQHIrLZYocn-rW9kalVQP8wYQ6Kg3x/view?usp=sharing)

## How to run the code  

### Training a new model

Make sure that you have downloaded all the [training images](https://drive.google.com/file/d/1v7hQHIrLZYocn-rW9kalVQP8wYQ6Kg3x/view?usp=sharing)
Also, make sure that you have users' judgements on material similarity. Those
 are two _json_ files inside `./data`, namely `answers_processed_train.json
 `, and `answers_processed_test.json`.
Also make sure that you have the uncropped images of each material with
 Havran geometry (`./data/havran1_ennis_298x298_LDR`).
 
Then, set up those arguments in the trianing script and run it:
```bash
python train.py --train-dir data/split_dataset --test-dir data
/havran1_ennis_298x298_LDR
```
Using the default values in the script, the trained model yields an agreement of
 81.99% with users' answers.
 


### Getting image feature vectors

Next, get the feature vectors for some images. First, modify paths inside `get_embs.py`.
```python
...
weights_path = 'data/model_best.pth.tar'
imgs_path = 'data/havran1_stpeters_256x256_LDR'
embs_path = 'data/embs.mat' # we will store the obtained feature vectors in this path
...
```

Then, get the feature vectors for the downloaded images
```bash
python3 get_embs.py    
```

### Get similar images
We can obtain similar images to a given reference using the previously computed feature vectors. First, set the path and necesary variables in `plot_similar.py`. This will store the 5 more similar images to the reference according to our metric in the path `data/nickel`.
```python
...
embs_path = 'data/embs.mat'  # /mat file with the embeddings
n_close_elems = 5  # number of close elements to find
reference_img = 'data/havran1_stpeters_256x256_LDR/nickel.png'
do_unit_norm = False # normalize feature vectors to have unit norm
...
```
<div align="center">  
<img src="__media__/similar.png">
</div>

### Generate UMAP plot

We can visualize the feature vectors generated for the images using dimensionality reduction algorithms like UMAP. 
First we set the path of the feature vectors inside `plot_umap.py`. 
```python
...
embs_path = 'data/embs.mat'
do_unit_norm = False # normalize feature vectors to have unit norm
...
```
To generate the plot we run:
```bash
python3 plot_umap.py
```
<div align="center">  
<img src="__media__/umap.png" >
</div>

## Citation   
If you found this code useful please cite our work as:
```
@article{lagunas2019similarity,
    author = {Lagunas, Manuel and Malpica, Sandra and Serrano, Ana and
    Garces, Elena and Gutierrez, Diego and Masia, Belen},
    title = {A Similarity Measure for Material Appearance},
    journal = {ACM Transactions on Graphics (SIGGRAPH 2019)},
    volume = {38},
    number = {4},
    year = {2019}
}
```   
