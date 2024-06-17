import os
import cv2
import numpy as np
import shutil

sdir = 'tmp'
# videos = [
#     [
#         'a_DSLR_photo_of_a_piglet_sitting_in_a_teacup', 
#         'a_red_panda', 'a_DSLR_photo_of_a_shiba_inu_playing_golf_wearing_tartan_golf_clothes_and_hat', 'a_DSLR_photo_of_a_cocker_spaniel_wearing_a_crown'
#     ], 
#     [
#         'a_zoomed_out_DSLR_photo_of_a_corgi_wearing_a_top_hat', 'a_DSLR_photo_of_a_squirrel_dressed_like_a_clown', 'a_zoomed_out_DSLR_photo_of_a_kingfisher_bird', 'a_DSLR_photo_of_a_mandarin_duck_swimming_in_a_pond'
#     ],
#     [
#         'a_plush_toy_of_a_corgi_nurse', 
#         'a_plush_dragon_toy', 'a_DSLR_photo_of_a_hippo_wearing_a_sweater', 'a_zoomed_out_DSLR_photo_of_a_lion\'s_mane_jellyfish'
#     ], 
#     ['a_DSLR_photo_of_a_robot_dinosaur', 'a_DSLR_photo_of_a_shiny_silver_robot_cat', 'a_zoomed_out_DSLR_photo_of_a_hippo_made_out_of_chocolate', 'a_zoomed_out_DSLR_photo_of_an_origami_hippo_in_a_river'], ['an_airplane_made_out_of_wood', 'A_Panther_De_Ville_car', 'a_DSLR_photo_of_a_steam_engine_train,_high_resolution', 'a_zoomed_out_DSLR_photo_of_an_amigurumi_motorcycle'], ['a_DSLR_photo_of_a_delicious_chocolate_brownie_dessert_with_ice_cream_on_the_side', 'a_DSLR_photo_of_an_ice_cream_sundae', 'a_DSLR_photo_of_a_steaming_hot_plate_piled_high_with_spaghetti_and_meatballs', 'a_wide_angle_zoomed_out_DSLR_photo_of_zoomed_out_view_of_Tower_Bridge_made_out_of_gingerbread_and_candy'], ['a_20-sided_die_made_out_of_glass', 'a_DSLR_photo_of_a_football_helmet', 'a_DSLR_photo_of_the_leaning_tower_of_Pisa,_aerial_view', 'an_erupting_volcano,_aerial_view']
# ]

videos = [['a_DSLR_photo_of_a_corgi_puppy', 'a_DSLR_photo_of_a_cat', 'a_red_panda', 'a_panda']]

for i, video_list in enumerate(videos):
    for idx, video in enumerate(video_list):
        pfx = chr(ord('A') + idx)
        os.makedirs(os.path.join(sdir, pfx), exist_ok=True)
        os.system(f'ffmpeg -i {video}.mp4 {sdir}/{pfx}/%4d.png')
    
    imgnames = list(sorted(os.listdir(os.path.join(sdir, d))) for d in sorted(os.listdir(sdir)))
    pfxs = [chr(ord('A') + j) for j in range(idx + 1)]

    for k in zip(*imgnames):
        img = np.hstack([cv2.imread(os.path.join(sdir, pfxs[j], k[j])) for j in range(len(k))])
        cv2.imwrite(os.path.join(sdir, k[0]), img)

    os.system(f'ffmpeg -i {sdir}/%4d.png -pix_fmt yuv420p {i}.mp4 -y')
    shutil.rmtree(sdir)