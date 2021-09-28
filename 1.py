import argparse

parser = argparse.ArgumentParser("BEiT pre-training script", add_help=False)
parser.add_argument(
    "-e",
    "--evaluate",
    dest="evaluate",
    action="store_false",
    help="evaluate model on validation set",
)
print(parser.parse_args())
