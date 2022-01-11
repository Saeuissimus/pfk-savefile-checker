#!/usr/bin/env python3

import argparse, magic, pathlib, zipfile

parser = argparse.ArgumentParser(description="Checks corruption of Pathfinder: Kingmaker savefiles.")
parser.add_argument('savefile', type=pathlib.Path, help='path of the savefile')

args = parser.parse_args()

with zipfile.ZipFile(args.savefile, "r") as archive:
  namelist = archive.namelist()
  for filename in namelist:
    filepath = pathlib.Path(filename)
    # We ignore files without extension for now
    if len(filepath.suffixes) == 0:
      continue

    file = archive.read(filename)
    file_mime = magic.from_buffer(file, mime=True)
    file_extension = "".join(filepath.suffixes)
    if file_extension == ".json":
      if file_mime == "application/octet-stream":
        print(f"Found corrupted JSON: {filename}")
      elif file_mime != "application/json" and file_mime != "text/plain":
        print(f"Found JSON with strange mime type: {file_mime}")
    elif file_extension == ".fog.png":
      if file_mime != "image/jpeg":
        print(f"Found fog bitmask with strange mime type: {file_mime}")
    elif file_extension == ".png":
      if file_mime != "image/png":
        print(f"Found image with strange mime type: {file_mime}")
    else:
      print(f"Found unknown file extension {file_extension} with mime type: {file_mime}")

