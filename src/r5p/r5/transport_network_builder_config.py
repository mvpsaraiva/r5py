#!/usr/bin/env python3

"""Wraps a com.conveyal.r5.point_to_point.builder.TNBuilderConfig."""

from ..util import config  # noqa: F401

import jpype
import jpype.types


__all__ = ["TransportNetworkBuilderConfig"]


@jpype._jcustomizer.JImplementationFor("com.conveyal.r5.point_to_point.builder.TNBuilderConfig")
class TransportNetworkBuilderConfig:
    """Wrap a com.conveyal.r5.point_to_point.builder.TNBuilderConfig."""
    def __init__(self, **kwargs):
        """
        Provide the configuration for loading a transport network.

        Arguments
        ---------
        **kwargs : mixed
            Parameters accepted by TNBuilderConfig. Both snake_case and
            CamelCase are accepted.
            See https://github.com/conveyal/r5/blob/v6.6/src/main/java/com/conveyal/r5/point_to_point/builder/TNBuilderConfig.java#L128
        """
        super().__init__()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattr__(self, key):
        key = TransportNetworkBuilderConfig.snake_to_camel_case(key)
        return self.config[key]

    def __setattr__(self, key, value):
        key = TransportNetworkBuilderConfig.snake_to_camel_case(key)
        self.config[key] = value
        self._config.setattr(key, value)

    def update(self, config_update={}):
        for key, value in config_update.items():
            self[key] = value

    @staticmethod
    def snake_to_camel_case(snake_case):
        return ''.join(word.title() for word in snake_case.split('_'))
