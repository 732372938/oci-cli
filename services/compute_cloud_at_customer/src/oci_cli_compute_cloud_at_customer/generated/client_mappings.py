# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221208

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.compute_cloud_at_customer import ComputeCloudAtCustomerClient

MODULE_TO_TYPE_MAPPINGS["compute_cloud_at_customer"] = oci.compute_cloud_at_customer.models.compute_cloud_at_customer_type_mapping
if CLIENT_MAP.get("compute_cloud_at_customer") is None:
    CLIENT_MAP["compute_cloud_at_customer"] = {}
CLIENT_MAP["compute_cloud_at_customer"]["compute_cloud_at_customer"] = ComputeCloudAtCustomerClient
