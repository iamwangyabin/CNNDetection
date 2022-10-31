from util import mkdir


# directory to store the results
results_dir = './results/'
mkdir(results_dir)

# root to the testsets
dataroot = '~/workspace/datasets/aiart/output2/sd'
# dataroot = '~/workspace/datasets/aiart/output2/dalle'
# dataroot = '~/workspace/datasets/aiart/output2/imagen'
# dataroot = '~/workspace/datasets/aiart/output2/mj'
# dataroot = '~/workspace/datasets/aiart/output2/parti'

# list of synthesis algorithms
vals = ['val']

# indicates if corresponding testset has multiple classes
multiclass = [0]

# model
# model_path = '/home/wangyabin/workspace/CDDDet/checkpoints/vit_sd_blur_jpg_prob0.5/model_epoch_best.pth'
# model_path = '/home/wangyabin/workspace/CDDDet/checkpoints/vit_sd_blur_jpg_prob0.5/model_epoch_best.pth'
# model_path = '/home/wangyabin/workspace/CDDDet/checkpoints/resnet_sd_blur_jpg_prob0.1/model_epoch_best.pth'
# model_path = '/home/wangyabin/workspace/CDDDet/checkpoints/resnet_sd_blur_jpg_prob0.5/model_epoch_best.pth'
# model_path = '/home/wangyabin/workspace/CDDDet/weights/blur_jpg_prob0.1.pth'
model_path = '/home/wangyabin/workspace/CDDDet/weights/blur_jpg_prob0.5.pth'
