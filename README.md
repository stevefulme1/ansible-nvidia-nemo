> **EXPERIMENTAL** - This collection is a proof of concept and is not production ready.
> Modules may use placeholder API endpoints and have not been validated against real infrastructure.
> Do not use in production environments.

    # stevefulme1.nvidia_nemo

    Ansible Collection for NVIDIA NeMo (AI Training Framework). Provides modules for managing training jobs, fine-tuning, guardrails, evaluators, retrievers, and customizations.

    ## Requirements

    - Ansible >= 2.16
    - Python >= 3.9
    - `requests` Python library

    ## Modules

    - `stevefulme1.nvidia_nemo.nemo_training_job` - Manage NeMo training jobs
- `stevefulme1.nvidia_nemo.nemo_training_job_info` - Retrieve NeMo training job details
- `stevefulme1.nvidia_nemo.nemo_fine_tune` - Manage NeMo fine-tuning jobs
- `stevefulme1.nvidia_nemo.nemo_fine_tune_info` - Retrieve NeMo fine-tuning job details
- `stevefulme1.nvidia_nemo.nemo_model` - Manage NeMo models
- `stevefulme1.nvidia_nemo.nemo_model_info` - Retrieve NeMo model details
- `stevefulme1.nvidia_nemo.nemo_dataset` - Manage NeMo datasets
- `stevefulme1.nvidia_nemo.nemo_dataset_info` - Retrieve NeMo dataset details
- `stevefulme1.nvidia_nemo.nemo_guardrail` - Manage NeMo guardrails
- `stevefulme1.nvidia_nemo.nemo_guardrail_info` - Retrieve NeMo guardrail details
- `stevefulme1.nvidia_nemo.nemo_guardrail_config` - Manage NeMo guardrail configurations
- `stevefulme1.nvidia_nemo.nemo_evaluator` - Manage NeMo evaluators
- `stevefulme1.nvidia_nemo.nemo_evaluator_info` - Retrieve NeMo evaluator details
- `stevefulme1.nvidia_nemo.nemo_retriever` - Manage NeMo retrievers
- `stevefulme1.nvidia_nemo.nemo_retriever_info` - Retrieve NeMo retriever details
- `stevefulme1.nvidia_nemo.nemo_retriever_pipeline` - Manage NeMo retriever pipelines
- `stevefulme1.nvidia_nemo.nemo_customization` - Manage NeMo customizations
- `stevefulme1.nvidia_nemo.nemo_customization_info` - Retrieve NeMo customization details

    ## Roles

    - `nemo_train` - Run NVIDIA NeMo training jobs
- `nemo_guardrails_deploy` - Deploy NVIDIA NeMo guardrails
- `nemo_eval` - Run NVIDIA NeMo model evaluations

    ## EDA

    - `nemo_training_events` - Watch NeMo training jobs for completion and failure events

    ## License

    GPL-3.0-or-later
