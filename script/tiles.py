#################################################
#                                               #
#  This tiles script was taken from SquadLanes  #
#         and edited to run on Windows.         #
#                                               #
#################################################

import concurrent.futures
import os
import subprocess
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from pprint import pprint

from tqdm import tqdm

the_path = "CHANGE/TO/INPUT/PATH"
the_other_path = "CHANGE/TO/OUTPUT/PATH"


def tiles():
    os.makedirs(the_other_path, exist_ok=True)


    # limit workers. each worker is going to spawn 16 processes anyway
    # todo: use MAX_PARALLEL_TASKS / 16 * 2
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []

        for name in os.listdir(the_path):
            # ignore non-tga files
            if not name.endswith(".TGA"):
                continue

            # remove extension
            name, _, _ = name.rpartition(".TGA")

            # We need to create a new user and group inside the Docker container,
            # otherwise the generated files will be owned by root on our host system,
            # which is annoying.
            # generate-map-tiles.sh takes care of that
            command = [
                f"docker",
                f"run",
                f"--mount",
                f"type=bind,source={os.path.abspath(the_path)},target=/mnt/map-fullsize",
                f"--mount",
                f"type=bind,source={os.path.abspath(the_other_path)},target=/mnt/map-tiles",
                f"--mount",
                f"type=bind,source={os.getcwd()},target=/mnt/cwd",
                f"osgeo/gdal",
                f"sh",
                f"/mnt/cwd/generate-map-tiles.sh",
                f"{os.getpid()}",
                f"{os.getpid()}",
                f"{name}",
            ]

            pprint(command)
            sys.stdout.flush()
            stdout = sys.stdout
            stderr = sys.stderr

            futures.append(executor.submit(extract_minimap, command, stdout, stderr))

        with tqdm(total=len(futures)) as pbar:
            for _ in concurrent.futures.as_completed(futures):
                pbar.update(1)


def extract_minimap(command: str, stdout, stderr):
    subprocess.call(command, stdout=stdout, stderr=stderr)

if __name__ == "__main__":
    tiles()