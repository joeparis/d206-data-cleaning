#!/usr/bin/env python3

from pathlib import Path

import pandas as pd
import recordlinkage

restaurants = pd.read_csv(Path.cwd() / "data/restaurants_L2.csv")
restaurants_new = pd.read_csv(Path.cwd() / "data/restaurants_new.csv")

indexer = recordlinkage.Index()

indexer.block("cuisine_type")

pairs = indexer.index(restaurants, restaurants_new)

comp_cl = recordlinkage.Compare()

comp_cl.exact("city", "city", label="city")
comp_cl.exact("cuisine_type", "cuisine_type", label="cuisine_type")
comp_cl.string("rest_name", "rest_name", label="rest_name")

potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)

print(potential_matches)
