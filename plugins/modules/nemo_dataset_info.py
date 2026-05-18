# -*- coding: utf-8 -*-
# Copyright (c) 2024, Steve Fulmer
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for retrieve nemo dataset details."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: nemo_dataset_info
short_description: Retrieve NeMo dataset details
description:
    - Retrieve NeMo dataset details using the NVIDIA REST API.
    - This module requires the C(requests) Python library.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    dataset_id:
        description:
            - The dataset id for the dataset.
        type: str
    name:
        description:
            - The name for the dataset.
        type: str
extends_documentation_fragment:
    - stevefulme1.nvidia_nemo.nvidia_common
requirements:
    - "python >= 3.9"
    - "requests"
"""

EXAMPLES = r"""
- name: Get dataset details
  stevefulme1.nvidia_nemo.nemo_dataset_info:
    dataset_id: "example-id"
"""

RETURN = r"""
dataset:
    description: Details of the dataset.
    returned: On success.
    type: dict
    sample:
        id: "example-id"
        name: "example-dataset"
        status: "ACTIVE"
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.stevefulme1.nvidia_nemo.plugins.module_utils.nvidia_common import (
    NVIDIA_COMMON_ARGS,
    to_dict,
)
from ansible_collections.stevefulme1.nvidia_nemo.plugins.module_utils.nvidia_api import (
    NvidiaApiError,
    create_api_client,
)


def get_module_args():
    module_args = dict(
        dataset_id=dict(type="str"),
        name=dict(type="str"),
    )
    module_args.update(NVIDIA_COMMON_ARGS)
    return module_args


def main():
    module = AnsibleModule(
        argument_spec=get_module_args(),
        supports_check_mode=True,
    )

    client = create_api_client(module)
    params = module.params

    if params.get("dataset_id"):
        try:
            resource = client.get(f"/v1/datasets/{params['dataset_id']}")
            module.exit_json(changed=False, dataset=to_dict(resource))
        except NvidiaApiError as exc:
            if exc.status == 404:
                module.exit_json(changed=False, dataset={})
            module.fail_json(msg=str(exc))
    else:
        try:
            result = client.get("/v1/datasets")
            items = result.get("data", result.get("items", []))
            module.exit_json(changed=False, datasets=[to_dict(i) for i in items])
        except NvidiaApiError as exc:
            module.fail_json(msg=str(exc))


if __name__ == "__main__":
    main()
