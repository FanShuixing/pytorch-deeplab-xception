CUDA_VISIBLE_DEVICES=0 python train.py --backbone resnet --lr 0.007 --workers 4  --epochs 50 --batch-size 8 --gpu-ids 0 --checkname deeplab-resnet --eval-interval 1 --dataset pascal

#接着之前的训练
CUDA_VISIBLE_DEVICES=0 python train.py --backbone resnet --lr 0.007 --workers 4  --epochs 100 --batch-size 8 --gpu-ids 0 --checkname deeplab-resnet --eval-interval 1 --dataset pascal --resume /output/tf_dir/pascal/deeplab-resnet/model_best.pth.tar
