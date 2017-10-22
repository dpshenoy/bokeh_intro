"""
Module to query DB data into a Pandas DataFrame.
"""
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://readonly:readonly@localhost:5432/world')


def fill_data_frame():

    connection = engine.connect()
    query = '''
        SELECT 
            name AS country, 
            region, 
            continent, 
            governmentform AS govtform, 
            surfacearea, 
            indepyear, 
            lifeexpectancy, 
            gnp, 
            population
        FROM 
            world.country
        '''
    world = pd.read_sql(query, connection)
    connection.close()

    # convert gnp to dollars (it APPEARS to be in millions of dollars...)
    world['gnp'] *= 1.e6

    # add column for per-capital gross national product column
    world['per_cap_gnp'] = world.gnp / world.population
    world.drop(labels=['gnp','population'], axis=1, inplace=True)

    # add columns for color & alpha of points, defaulting to grey & 0.5
    world['color'] = 'grey'
    world['alpha'] = 0.25

    # extra row to have "All" values as an option
    extra = world.iloc[[-1]].copy()
    for col in extra.columns:
        if isinstance(extra[col].values[0], np.int64):
            extra[col] = 0
        elif isinstance(extra[col].values[0], np.float64):
            extra[col] = 0.
        elif isinstance(extra[col].values[0], str):
            extra[col] = 'All'
    world = pd.concat([world, extra], ignore_index=True)

    return world
