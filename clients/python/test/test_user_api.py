# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [Changelog](/app/apiChangelog)    #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  -  ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """ UserApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.user_api.UserApi()

    def tearDown(self):
        pass

    def test_user_cancel_withdrawal(self):
        """
        Test case for user_cancel_withdrawal

        Cancel a withdrawal.
        """
        pass

    def test_user_check_referral_code(self):
        """
        Test case for user_check_referral_code

        Check if a referral code is valid.
        """
        pass

    def test_user_confirm(self):
        """
        Test case for user_confirm

        Confirm your email address with a token.
        """
        pass

    def test_user_confirm_enable_tfa(self):
        """
        Test case for user_confirm_enable_tfa

        Confirm two-factor auth for this account. If using a Yubikey, simply send a token to this endpoint.
        """
        pass

    def test_user_confirm_withdrawal(self):
        """
        Test case for user_confirm_withdrawal

        Confirm a withdrawal.
        """
        pass

    def test_user_disable_tfa(self):
        """
        Test case for user_disable_tfa

        Disable two-factor auth for this account.
        """
        pass

    def test_user_get(self):
        """
        Test case for user_get

        Get your user model.
        """
        pass

    def test_user_get_affiliate_status(self):
        """
        Test case for user_get_affiliate_status

        Get your current affiliate/referral status.
        """
        pass

    def test_user_get_commission(self):
        """
        Test case for user_get_commission

        Get your account's commission status.
        """
        pass

    def test_user_get_deposit_address(self):
        """
        Test case for user_get_deposit_address

        Get a deposit address.
        """
        pass

    def test_user_get_margin(self):
        """
        Test case for user_get_margin

        Get your account's margin status. Send a currency of \"all\" to receive an array of all supported currencies.
        """
        pass

    def test_user_get_wallet(self):
        """
        Test case for user_get_wallet

        Get your current wallet information.
        """
        pass

    def test_user_get_wallet_history(self):
        """
        Test case for user_get_wallet_history

        Get a history of all of your wallet transactions (deposits, withdrawals, PNL).
        """
        pass

    def test_user_get_wallet_summary(self):
        """
        Test case for user_get_wallet_summary

        Get a summary of all of your wallet transactions (deposits, withdrawals, PNL).
        """
        pass

    def test_user_logout(self):
        """
        Test case for user_logout

        Log out of BitMEX.
        """
        pass

    def test_user_logout_all(self):
        """
        Test case for user_logout_all

        Log all systems out of BitMEX. This will revoke all of your account's access tokens, logging you out on all devices.
        """
        pass

    def test_user_min_withdrawal_fee(self):
        """
        Test case for user_min_withdrawal_fee

        Get the minimum withdrawal fee for a currency.
        """
        pass

    def test_user_request_enable_tfa(self):
        """
        Test case for user_request_enable_tfa

        Get secret key for setting up two-factor auth.
        """
        pass

    def test_user_request_withdrawal(self):
        """
        Test case for user_request_withdrawal

        Request a withdrawal to an external wallet.
        """
        pass

    def test_user_save_preferences(self):
        """
        Test case for user_save_preferences

        Save user preferences.
        """
        pass

    def test_user_update(self):
        """
        Test case for user_update

        Update your password, name, and other attributes.
        """
        pass


if __name__ == '__main__':
    unittest.main()
