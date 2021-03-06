#!/usr/bin/env python3
#
# Author: Wade Wells github/Pack3tL0ss

from pathlib import Path
from typing import Any
import yaml
import json
import os


class Config:
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path(__file__).parent.parent.parent
        self.dir = self.base_dir.joinpath("config")
        self.file = self.dir.joinpath("config.yaml")
        for ext in ["yml", "json"]:
            if self.dir.joinpath(f"config.{ext}").exists():
                self.file = self.dir.joinpath(f"config.{ext}")
                break
        self.bulk_edit_file = self.dir.joinpath("bulkedit.csv")
        self.stored_tasks_file = self.dir.joinpath("stored-tasks.yaml")
        self.cache_file = self.dir.joinpath(".cache", "cache.yaml")
        self.cache_dir = self.cache_file.parent
        self.data = self.get_config_data(self.file) or {}
        self.DEBUG = self.data.get("debug", os.getenv("DEBUG", False))

    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    @staticmethod
    def get_config_data(config_file: Path) -> dict:
        '''Return dict from yaml file.'''
        if config_file.exists() and config_file.stat().st_size > 0:
            with config_file.open() as f:
                try:
                    if config_file.suffix == ".json":
                        return json.loads(f.read())
                    elif config_file.suffix in [".yaml", ".yml"]:
                        return yaml.load(f, Loader=yaml.SafeLoader)
                    else:
                        raise UserWarning("Provide valid file with"
                                          "format/extension [.json/.yaml/.yml]!")
                except Exception as e:
                    raise UserWarning(f'Unable to load configuration from {config_file}\n{e.__class__}\n\n{e}')
