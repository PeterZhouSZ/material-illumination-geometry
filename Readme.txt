Requirements:

Tensorflow-gpu
Tensorlayer
numpy
scipy
opencv
easydict
sklearn
pandas

Train:
1. Set the config.py file
   set the log_dir to your log path
   set the ckpt_dir to your model weights path
   set the input_path to the path of your dataset folder
   set the gt_path to the path of your csv file 

2. python main.py --is_test False

Test:
1. Set the config.py file
   set the log_dir to your log path
   set the ckpt_dir to your trained model weights path
   set the input_path to the path of your dataset folder
   set the gt_path to the path of your csv file 
2. Set the test.py file
   set the saved path to your own path 
python main.py --is_test True

