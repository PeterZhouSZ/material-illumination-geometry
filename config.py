from easydict import EasyDict as edict
import json

config = edict()
config.TRAIN = edict()
config.TEST = edict()

# TRAIN ===============================================================
config.TRAIN.batch_size = 4
config.TRAIN.patch_size = 512
config.TRAIN.lr = 1e-5
config.TRAIN.beta_1 = 0.9
config.TRAIN.lr_decay = 0.8
config.TRAIN.decay_every = 20
config.TRAIN.epoch = 400
config.TRAIN.ckpt_ep = 1
config.TRAIN.log_dir = '/HPS/BRDF2/work/attributes/network_chao/log_train_polish'
config.TRAIN.ckpt_dir = '/HPS/BRDF2/work/attributes/network_chao/ckpt_train_polish'
config.TRAIN.re_train = False
config.TRAIN.pre_vgg = False
config.TRAIN.pretrained_model = '/HPS/BRDF2/work/attributes/network_chao/ckpt_train_vgg_exclude_bunny_mse_agu_restore_new/epoch_9.npz'#'/HPS/BRDF/work/attributes/network_chao/ckpt_train_large_resnobn_newlr_exclude_final/epoch_31.npz'#'/HPS/BRDF/work/attributes/network_chao/ckpt_train_large_resnobn_newlr_exclude_new_restore/epoch_31.npz'
config.TRAIN.vgg16_parameters = ''

# Loss coefficient
config.TRAIN.lambda_mae = 1e-3
config.TRAIN.lambda_mse = 1e-3

# Train dataset path
config.TRAIN.input_path = '/HPS/BRDF/work/rendering/results/v1/color_chnl/'#'/HPS/BRDF/work/dataset/serrano2016/all-renders_400_tonemappedExpGamma_rename'
config.TRAIN.gt_path = '/HPS/BRDF/work/attributes/network_chao/20201219_DataTable_MedianRating.csv'#'/HPS/BRDF/work/dataset/serrano2016/MaterialAppearance_SiggAsia2016_code/surveydata_and_training/data_Mturks/_final_ans_mtx.mat'


# TEST ================================================================
# Test dataset path
config.TEST.patch_size = 512
config.TEST.log_dir = './log/'
config.TEST.ckpt_dir = './weights/'#'/HPS/BRDF2/work/attributes/network_chao/ckpt_train_vgg_exclude_bunny_msle_agu_restore_new/'#'/HPS/BRDF2/work/attributes/network_chao/ckpt_train_resnobn_exclude_bunny_mse_agu_restore_new'#'/HPS/BRDF/work/attributes/network_chao/ckpt_train_resnobn_exclude_bunny_msle_restore/'#'/HPS/BRDF/work/attributes/network_chao/ckpt_train_large_resnobn_newlr_exclude_final_restore/'#'/HPS/BRDF/work/attributes/network_chao/ckpt_train_large_resnobn_newlr_exclude_final_restore/'##'/HPS/BRDF/work/attributes/network_chao/ckpt_train_large_resnobn_newlr_exclude_final/'
config.TEST.input_path = './test/imgs/'#'/HPS/BRDF/work/rendering/code/color_chnl_2'#'/HPS/BRDF/work/rendering/results/new_test_set_3/color_chnl'#'/HPS/BRDF/work/attributes/network_chao/all/'#'/HPS/BRDF/work/rendering/results/geo_complex_test/color_chnl/'#'/HPS/BRDF/work/rendering/results/envmap_blur/gaussian_r30/color_chnl/'#'/HPS/BRDF/work/attributes/network_chao/all/'#'/HPS/BRDF/work/attributes/network_chao/all/'#'/HPS/BRDF/work/rendering/results/v1/color_chnl/'#'/HPS/BRDF/work/rendering/results/geo_complex_test'#'/HPS/BRDF/work/attributes/network_chao/all/'#'/HPS/BRDF/work/rendering/results/v1/color_chnl/'#'/HPS/BRDF/work/attributes/network_chao/all/'#'/HPS/BRDF/work/rendering/results/v1/color_chnl/'##'/HPS/BRDF/work/validation_set/20-RotatedGeoms/'#'/HPS/BRDF/work/rendering/results/validation/edited/color_chnl/'#'/HPS/BRDF/work/rendering/results/validation/analytic/color_chnl/'#'/HPS/BRDF/work/rendering/results/pov/p30/color_chnl'#'/HPS/BRDF/work/rendering/results/v1/color_chnl/'#'/HPS/BRDF/work/attributes/network_chao/printing_obj/'#'/HPS/BRDF/work/rendering/results/v1/color_chnl/'
config.TEST.gt_path = './test/names.csv'#'/HPS/BRDF/work/attributes/network_chao/validation_all.csv'#'/HPS/BRDF/work/attributes/network_chao/validation_all.csv'#'/HPS/BRDF/work/attributes/network_chao/20201219_DataTable_MedianRating.csv'#'/HPS/BRDF/work/attributes/network_chao/20201219_DataTable_MedianRating.csv'#'/HPS/BRDF/work/attributes/network_chao/20201229_DataTable_MedianRating_val.csv'#'/HPS/BRDF/work/attributes/network_chao/20201219_DataTable_MedianRating.csv'#
#config.TEST.f_name_path = '/HPS/BRDF/work/dataset/serrano2016/MaterialAppearance_SiggAsia2016_code/surveydata_and_training/data_Mturks/names.txt'


ATTRB_NUM = 6