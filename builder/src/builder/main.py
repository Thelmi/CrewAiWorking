#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from builder.crew import Builder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        "description": "A sustainable fashion offering eco-freindly clothing",
        "market": "Global fashion industry"
    }
    
    try:
        Builder().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# run()