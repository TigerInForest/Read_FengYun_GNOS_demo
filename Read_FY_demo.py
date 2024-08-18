# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:55:53 2024

@author: Zhanglinhu @ linhuzhang@whu.edu.cn

Notes:
    Read_FY_demo_py
    1. 读取一个风云GNOS文件数据中的所有变量值
    2. 
    
    风云GNOS数据格式
    Group: Channel
    Dataset: Channel/Direct_antenna_id
    Dataset: Channel/Direct_signal_noise
    Dataset: Channel/Direct_signal_snr
    Dataset: Channel/Rx_channel_status
    Group: DDM
    Dataset: DDM/Ddm_brcs_factor
    Dataset: DDM/Ddm_doppler_refer
    Dataset: DDM/Ddm_effective_area
    Dataset: DDM/Ddm_kurtosis
    Dataset: DDM/Ddm_noise_m
    Dataset: DDM/Ddm_noise_raw
    Dataset: DDM/Ddm_noise_source
    Dataset: DDM/Ddm_peak_column
    Dataset: DDM/Ddm_peak_delay
    Dataset: DDM/Ddm_peak_doppler
    Dataset: DDM/Ddm_peak_power_ratio
    Dataset: DDM/Ddm_peak_raw
    Dataset: DDM/Ddm_peak_row
    Dataset: DDM/Ddm_peak_snr
    Dataset: DDM/Ddm_power_factor
    Dataset: DDM/Ddm_quality_flag
    Dataset: DDM/Ddm_range_refer
    Dataset: DDM/Ddm_raw_data
    Dataset: DDM/Ddm_skewness
    Dataset: DDM/Ddm_sp_column
    Dataset: DDM/Ddm_sp_delay
    Dataset: DDM/Ddm_sp_dles
    Dataset: DDM/Ddm_sp_doppler
    Dataset: DDM/Ddm_sp_les
    Dataset: DDM/Ddm_sp_nbrcs
    Dataset: DDM/Ddm_sp_normalized_snr
    Dataset: DDM/Ddm_sp_raw
    Dataset: DDM/Ddm_sp_reflectivity
    Dataset: DDM/Ddm_sp_row
    Dataset: DDM/Ddm_sp_snr
    Dataset: DDM/Sp_delay_doppler_flag
    Group: Receiver
    Dataset: Receiver/Rx_alt
    Dataset: Receiver/Rx_attitude_status
    Dataset: Receiver/Rx_clk_bias
    Dataset: Receiver/Rx_clk_bias_rate
    Dataset: Receiver/Rx_fly_direction
    Dataset: Receiver/Rx_lat
    Dataset: Receiver/Rx_lon
    Dataset: Receiver/Rx_pitch
    Dataset: Receiver/Rx_pos_x
    Dataset: Receiver/Rx_pos_y
    Dataset: Receiver/Rx_pos_z
    Dataset: Receiver/Rx_roll
    Dataset: Receiver/Rx_vel_x
    Dataset: Receiver/Rx_vel_y
    Dataset: Receiver/Rx_vel_z
    Dataset: Receiver/Rx_yaw
    Group: Specular
    Dataset: Specular/Rx_sp_range
    Dataset: Specular/Sp_alt
    Dataset: Specular/Sp_antenna_gain
    Dataset: Specular/Sp_az_antenna
    Dataset: Specular/Sp_az_body
    Dataset: Specular/Sp_az_orbit
    Dataset: Specular/Sp_az_pattern
    Dataset: Specular/Sp_fresnel_coeff_square
    Dataset: Specular/Sp_inc_angle
    Dataset: Specular/Sp_lat
    Dataset: Specular/Sp_lon
    Dataset: Specular/Sp_pos_x
    Dataset: Specular/Sp_pos_y
    Dataset: Specular/Sp_pos_z
    Dataset: Specular/Sp_surface_type
    Dataset: Specular/Sp_tcg
    Dataset: Specular/Sp_theta_antenna
    Dataset: Specular/Sp_theta_body
    Dataset: Specular/Sp_theta_orbit
    Dataset: Specular/Sp_theta_pattern
    Dataset: Specular/Sp_vel_x
    Dataset: Specular/Sp_vel_y
    Dataset: Specular/Sp_vel_z
    Dataset: Specular/Tx_sp_range
    Group: Time
    Dataset: Time/Ddm_gps_second
    Dataset: Time/Ddm_gps_week
    Dataset: Time/Ddm_time_utc
    Dataset: Time/Ddm_track_id
    Dataset: Time/Sample_num
    Group: Transmitter
    Dataset: Transmitter/Gnss_block_flag
    Dataset: Transmitter/Gnss_prn_code
    Dataset: Transmitter/Gnss_svn_num
    Dataset: Transmitter/Tx_pos_x
    Dataset: Transmitter/Tx_pos_y
    Dataset: Transmitter/Tx_pos_z
    Dataset: Transmitter/Tx_vel_x
    Dataset: Transmitter/Tx_vel_y
    Dataset: Transmitter/Tx_vel_z
"""
import h5py

file_path='J:/15_FY_GNOS/03_Data/代码测试文件/A202407220036939986/FY3E_GNOSR_ORBT_L1_20230330_1411_RFLC6_V0.HDF'

# output_file = "output_FY.txt"  # 替换为你想保存的文本文件路径
# # 打开HDF5文件
# with h5py.File(file_path, "r") as hdf:
#     # 打开文本文件进行写入
#     with open(output_file, "w") as f:
#         # 定义一个函数，用于将输出写入文件而不是打印到控制台
#         def print_attrs(name, obj):
#             f.write(f"{name}\n")
#             # 输出所有属性
#             for key, val in obj.attrs.items():
#                 f.write(f"    {key}: {val}\n")
#             # 输出数据类型和大小（如果是数据集）
#             if isinstance(obj, h5py.Dataset):
#                 f.write(f"    Data Type: {obj.dtype}\n")
#                 f.write(f"    Data Size: {obj.size}\n")
#                 f.write(f"    Data Shape: {obj.shape}\n")

#         # 遍历文件中的所有对象，并将其写入文件
#         hdf.visititems(print_attrs)

# print(f"Output has been written to {output_file}")

# #显示文件中的所有文件夹或组中的变量名
# with h5py.File(file_path, "r") as hdf:
#     # 定义递归函数，遍历所有组和数据集
#     def print_datasets(name, obj):
#         if isinstance(obj, h5py.Dataset):  # 如果对象是数据集
#             print(f"Dataset: {name}")
#         elif isinstance(obj, h5py.Group):  # 如果对象是组
#             print(f"Group: {name}")

#     # 递归遍历文件中的所有对象
#     hdf.visititems(print_datasets)
 
#Get data into numpy arrays
f = h5py.File(file_path, 'r')  
##Group: Channel
Channel_Direct_antenna_id=f['/Channel/Direct_antenna_id']
#读取变量内容
Direct_antenna_id=Channel_Direct_antenna_id[:]
#读取变量的属性值
''' eg.
    Channel/Direct_antenna_id
        Description: b'The flag of the direct signal antenna. 0:foward antenna,5:backward antenna.'
        FillValue: [-2147483648]
        Intercept: [0.]
        Slope: [1.]
        band_name: b'none'
        long_name: b'Direct antenna id'
        units: b'none'
        valid_range: [0 5]
'''
Direct_antenna_id_Description=Channel_Direct_antenna_id.attrs['Description']
Direct_antenna_id_FillValue=Channel_Direct_antenna_id.attrs['FillValue']
Direct_antenna_id_Intercept=Channel_Direct_antenna_id.attrs['Intercept']
Direct_antenna_id_Slope=Channel_Direct_antenna_id.attrs['Slope']
Direct_antenna_id_band_name=Channel_Direct_antenna_id.attrs['band_name']
Direct_antenna_id_long_name=Channel_Direct_antenna_id.attrs['long_name']
Direct_antenna_id_units=Channel_Direct_antenna_id.attrs['units']
Direct_antenna_id_valid_range=Channel_Direct_antenna_id.attrs['valid_range']

Channel_Direct_signal_noise=f['/Channel/Direct_signal_noise']
Channel_Direct_signal_snr=f['/Channel/Direct_signal_snr']
Channel_Rx_channel_status=f['/Channel/Rx_channel_status']
##Group: DDM
DDM_Ddm_brcs_factor=f['/DDM/Ddm_brcs_factor']
DDM_brcs_factor=DDM_Ddm_brcs_factor[:]
DDM_Ddm_doppler_refer=f['/DDM/Ddm_doppler_refer']
DDM_Ddm_effective_area=f['/DDM/Ddm_effective_area']
DDM_Ddm_kurtosis=f['/DDM/Ddm_kurtosis']
DDM_Ddm_noise_m=f['/DDM/Ddm_noise_m']
DDM_Ddm_noise_raw=f['/DDM/Ddm_noise_raw']
DDM_Ddm_noise_source=f['/DDM/Ddm_noise_source']
DDM_Ddm_peak_column=f['/DDM/Ddm_peak_column']
DDM_Ddm_peak_delay=f['/DDM/Ddm_peak_delay']
DDM_Ddm_peak_doppler=f['/DDM/Ddm_peak_doppler']
DDM_Ddm_peak_power_ratio=f['/DDM/Ddm_peak_power_ratio']
DDM_Ddm_peak_raw=f['/DDM/Ddm_peak_raw']
DDM_Ddm_peak_row=f['/DDM/Ddm_peak_row']
DDM_Ddm_peak_snr=f['/DDM/Ddm_peak_snr']
DDM_Ddm_power_factor=f['/DDM/Ddm_power_factor']
DDM_Ddm_quality_flag=f['/DDM/Ddm_quality_flag']
DDM_Ddm_range_refer=f['/DDM/Ddm_range_refer']
DDM_Ddm_raw_data=f['/DDM/Ddm_raw_data']
DDM_Ddm_skewness=f['/DDM/Ddm_skewness']
DDM_Ddm_sp_column=f['/DDM/Ddm_sp_column']
DDM_Ddm_sp_delay=f['/DDM/Ddm_sp_delay']
DDM_Ddm_sp_dles=f['/DDM/Ddm_sp_dles']
DDM_Ddm_sp_doppler=f['/DDM/Ddm_sp_doppler']
DDM_Ddm_sp_les=f['/DDM/Ddm_sp_les']
DDM_Ddm_sp_nbrcs=f['/DDM/Ddm_sp_nbrcs']
DDM_Ddm_sp_normalized_snr=f['/DDM/Ddm_sp_normalized_snr']
DDM_Ddm_sp_raw=f['/DDM/Ddm_sp_raw']
DDM_Ddm_sp_reflectivity=f['/DDM/Ddm_sp_reflectivity']
DDM_Ddm_sp_row=f['/DDM/Ddm_sp_row']
DDM_Ddm_sp_snr=f['/DDM/Ddm_sp_snr']
DDM_Sp_delay_doppler_flag=f['/DDM/Sp_delay_doppler_flag']
##Group:Reciever
Receiver_Rx_alt=f['/Receiver/Rx_alt']
Receiver_Rx_attitude_status=f['/Receiver/Rx_attitude_status']
Receiver_Rx_clk_bias=f['/Receiver/Rx_clk_bias']
Receiver_Rx_clk_bias_rate=f['/Receiver/Rx_clk_bias_rate']
Receiver_Rx_fly_direction=f['/Receiver/Rx_fly_direction']
Receiver_Rx_lat=f['/Receiver/Rx_lat']
Receiver_Rx_lon=f['/Receiver/Rx_lon']
Receiver_Rx_pitch=f['/Receiver/Rx_pitch']
Receiver_Rx_pos_x=f['/Receiver/Rx_pos_x']
Receiver_Rx_pos_y=f['/Receiver/Rx_pos_y']
Receiver_Rx_pos_z=f['/Receiver/Rx_pos_z']
Receiver_Rx_roll=f['/Receiver/Rx_roll']
Receiver_Rx_vel_x=f['/Receiver/Rx_vel_x']
Receiver_Rx_vel_y=f['/Receiver/Rx_vel_y']
Receiver_Rx_vel_z=f['/Receiver/Rx_vel_z']
Receiver_Rx_yaw=f['/Receiver/Rx_yaw']
##Group:Specular
Specular_Sp_alt=f['/Specular/Sp_alt']
Specular_Sp_antenna_gain=f['/Specular/Sp_antenna_gain']
Specular_Sp_az_antenna=f['/Specular/Sp_az_antenna']
Specular_Sp_az_body=f['/Specular/Sp_az_body']
Specular_Sp_az_orbit=f['/Specular/Sp_az_orbit']
Specular_Sp_az_pattern=f['/Specular/Sp_az_pattern']
Specular_Sp_dist_to_coastline=f['/Specular/Sp_dist_to_coastline']
Specular_Sp_fresnel_coeff_square=f['/Specular/Sp_fresnel_coeff_square']
Specular_Sp_inc_angle=f['/Specular/Sp_inc_angle']
Specular_Sp_land_sea_mask=f['/Specular/Sp_land_sea_mask']
Specular_Sp_lat=f['/Specular/Sp_lat']
Specular_Sp_lon=f['/Specular/Sp_lon']
Specular_Sp_pos_x=f['/Specular/Sp_pos_x']
Specular_Sp_pos_y=f['/Specular/Sp_pos_y']
Specular_Sp_pos_z=f['/Specular/Sp_pos_z']
Specular_Sp_surface_type=f['/Specular/Sp_surface_type']
Specular_Sp_tcg=f['/Specular/Sp_tcg']
Specular_Sp_theta_antenna=f['/Specular/Sp_theta_antenna']
Specular_Sp_theta_body=f['/Specular/Sp_theta_body']
Specular_Sp_theta_orbit=f['/Specular/Sp_theta_orbit']
Specular_Sp_theta_pattern=f['/Specular/Sp_theta_pattern']
Specular_Sp_vel_x=f['/Specular/Sp_vel_x']
Specular_Sp_vel_y=f['/Specular/Sp_vel_y']
Specular_Sp_vel_z=f['/Specular/Sp_vel_z']
##Group:Time
Time_Ddm_gps_second=f['/Time/Ddm_gps_second']
Time_Ddm_gps_week=f['/Time/Ddm_gps_week']
Time_Ddm_time_utc=f['/Time/Ddm_time_utc']
Time_Ddm_track_id=f['/Time/Ddm_track_id']
Time_Sample_num=f['/Time/Sample_num']
#Group:Transmitter
Transmitter_Gnss_block_flag=f['/Transmitter/Gnss_block_flag']
Transmitter_Gnss_prn_code=f['/Transmitter/Gnss_prn_code']
Transmitter_Gnss_svn_num=f['/Transmitter/Gnss_svn_num']
Transmitter_Tx_pos_x=f['/Transmitter/Tx_pos_x']
Transmitter_Tx_pos_y=f['/Transmitter/Tx_pos_y']
Transmitter_Tx_pos_z=f['/Transmitter/Tx_pos_z']
Transmitter_Tx_vel_x=f['/Transmitter/Tx_vel_x']
Transmitter_Tx_vel_y=f['/Transmitter/Tx_vel_y']
Transmitter_Tx_vel_z=f['/Transmitter/Tx_vel_z']












