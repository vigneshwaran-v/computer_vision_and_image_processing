# Stereo Vision

1. Disparity estimation using block matching:

Left disparity map – using 3x3 block:

![output_ldmap_3x3](outputs/left_depth_map_3x3.png)

Right disparity map- using 3x3 block:

![output_rdmap_3x3](outputs/right_depth_map_3x3.png)

Left disparity map – using 9x9 block:

![output_ldmap_9x9](outputs/left_depth_map_9x9.png)

Right disparity map- using 9x9 block:

![output_rdmap_9x9](outputs/right_depth_map_9x9.png)

Left disparity map – using 3x3 block – consistency checked:

![output_ldmap_3x3_cc](outputs/left_consistency_3x3.png)

Right disparity map- using 3x3 block – consistency checked:

![output_rdmap_3x3_cc](outputs/right_consistency_3x3.png)

Left disparity map – using 9x9 block – consistency checked:

![output_ldmap_9x9_cc](outputs/left_consistency_9x9.png)

Right disparity map - using 9x9 block – consistency checked:

![output_rdmap_9x9_cc](outputs/right_consistency_9x9.png)


Calculated MSE values:

Left depth map 3x3 MSE= 437.3528573930302

Left depth map 9x9 MSE= 441.9508493374584

Right depth map 3x3 MSE= 344.985044655887

Right depth map 9x9 MSE= 335.8602766913782

Left consistency checked depth map 3x3 MSE= 116.59487683983502

Left cosnistency checked depth map 9x9 MSE= 54.172589908001115

Right cosnistency checked depth map 3x3 MSE= 119.98259487683984

Right cosnistency checked depth map 9x9 MSE= 57.0862001672707


2. Disparity estimation using Dynamic Programming:

Left disparity map:

![output_ldmap_dp](outputs/left_depth_map_dynamic.jpg)

Right disparity map:

![output_rdmap_dp](outputs/right_depth_map_dynamic.jpg)


3.View Synthesis:

Synthesized view: (view3):

![synthesized_view](outputs/synthesized_image(view3).png)

