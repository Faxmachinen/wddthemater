from pathlib import Path
from getpass import getuser
import json
import os

AUTHOR = getuser()
FILENAME_TEMPLATE = "{name}_{number}.jpg"

def remove_folder_if_empty(folder):
	try:
		folder.rmdir()
	except OSError:
		print(f'Warning: "{str(folder)}" contains unrecognized files.')

def move_images(target_dir, name, images):
	for i in range(len(images)):
		target_file = target_dir / FILENAME_TEMPLATE.format(name=name, number=i)
		if target_file.is_file() or target_file.is_dir():
			print('Error: Cannot move "{images[i]}" to "{target_file}" because the file already exists.')
			return False
	for i, image in enumerate(images):
		target_file = target_dir / FILENAME_TEMPLATE.format(name=name, number=i)
		image.rename(target_file)
	return True

def get_images(folder):
	result = folder.glob("*.jpg")
	return sorted(result, key=str)

def make_json_in_dir(root):
	day_images = get_images(root / 'day')
	night_images = get_images(root / 'night')
	day_count = len(day_images)
	night_count = len(night_images)
	if not day_images and not night_images:
		print(f'Warning: Skipping "{str(root)}" as it has no images in "day" and "night" folders.')
		return
	jobj = {}
	jobj['displayName'] = root.name
	jobj['imageFilename'] = FILENAME_TEMPLATE.format(name=jobj['displayName'], number='*')
	jobj['imageCredits'] = AUTHOR
	jobj['dayImageList'] = [i for i in range(day_count)]
	jobj['nightImageList'] = [i for i in range(day_count, day_count+night_count)]
	jobj['sunriseImageList'] = [0]
	jobj['sunsetImageList'] = [day_count - 1]
	with open(root / f"{jobj['displayName']}.json", 'w') as fh:
		fh.write(json.dumps(jobj, indent='\t'))
	if not move_images(root, jobj['displayName'], day_images + night_images):
		return
	remove_folder_if_empty(root / 'day')
	remove_folder_if_empty(root / 'night')
	print(f'Processed "{str(root)}" successfully.')

def make_jsons_in_all_dirs():
	for item in Path('.').iterdir():
		if not item.is_dir():
			continue
		make_json_in_dir(item)
	print('Done.')

if __name__ == '__main__':
	make_jsons_in_all_dirs()
