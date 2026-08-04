import torch
# 查看torch版本
print(torch.__version__)
# 判断GPU是否可用
print("GPU可用：", torch.cuda.is_available())
# 有显卡会输出True，无显卡输出False