#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `chatel` package."""


import unittest
from click.testing import CliRunner

from chatel import chatel
from chatel import cli


class TestChatel(unittest.TestCase):
    """Tests for `chatel` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.greet_message = "Hey Y'all, I see you're using chatel!"

    def test_print_greetings(self):
        """Set up test to print the greeting. """
        output = chatel.greeting()
        assert(output == self.greet_message)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'chatel.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
