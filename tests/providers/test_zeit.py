# Test for one implementation of the interface
from unittest import TestCase

import pytest
from integration_tests import IntegrationTests
from lexicon.providers.zeit import Provider


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests


class ZeitProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'zeit'
    domain = 'fullm3tal.tech'

    def _filter_headers(self):
        return ['Authorization']

    @pytest.mark.skip(reason="Records TTL are not supported by Zeit DNS")
    def test_Provider_when_calling_list_records_after_setting_ttl(self):
        return
