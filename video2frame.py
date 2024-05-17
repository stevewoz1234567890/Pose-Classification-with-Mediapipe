import cv2, argparse

if __name__ == '__main__':
  # Create ArgumentParser object
  parser = argparse.ArgumentParser()

  # Add argument
  parser.add_argument("--path", help="Path argument")

  # Parse the command-line arguments
  args = parser.parse_args()


  # Access the value of the argument
  if args.path:
      print("Video Path:", args.path)
      video_path = args.path
  else:
      print("Video Path not provided.")
        
  vidcap = cv2.VideoCapture(video_path)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite("frame\\image_%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1