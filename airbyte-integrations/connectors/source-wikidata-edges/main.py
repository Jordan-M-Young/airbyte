#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_wikidata_edges import SourceWikidataEdges

if __name__ == "__main__":
    source = SourceWikidataEdges()
    launch(source, sys.argv[1:])
