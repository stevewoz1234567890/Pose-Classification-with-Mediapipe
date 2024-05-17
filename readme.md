# Mediapipe

## Python Version
We use python 3.8.0.

## Install
```
pip install -r requirements.txt
```

## Run
```
python main.py --path <video path> --pose <pose type>
```

## Instruction

### Directory Help

You must make those directories in project before running app.

* fitness_poses_images_in
Directory for sample pose images

```
      pushups_up/
        image_001.jpg
        image_002.jpg
        ...
      pushups_down/
        image_001.jpg
        image_002.jpg
        ...
```

Name of subdirectory: Name of pose type
You should collect sample images of every pose in that directory.
This is manual work.
You can use video2frame.py to produce frames of the video.
```
python video2frame.py --path <video path>
```
Frames of video produced by video2frame.py are in frame directory.

* frame
Directory for frames
You can select suitable frames and move to 'fitness_poses_images_in' directory.

* fitness_pose_images_out
Directory for output images with mediapipe landmarks of sample images.
Output images are automatically produced while running.

* fitness_poses_csvs_out
Directory for CSV files.
Those files contain mediapipe landmarks and are automatically produced while running.

### Result
main.py produces the video with landmarks and count of pose.


### How to Collect image samples
1. Collect videos of every type of pose.
2. Obtain frames using video2frame.py.
3. Select suitable frames and move to fitness_poses_images_in.