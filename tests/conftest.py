"""Define the pytest configuration for fixture reuse."""
import os
from typing import Any, Generator

import boto3
import pytest
from moto import mock_eks, mock_sts


@pytest.fixture
def aws_creds() -> None:
    """Mock the AWS credentials to use for testing."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testaccesskeyid"  # nosec
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testsecretaccesskey"  # nosec
    os.environ["AWS_SECURITY_TOKEN"] = "testsecuritytoken"  # nosec
    os.environ["AWS_SESSION_TOKEN"] = "testsessiontoken"  # nosec


@pytest.fixture
def region() -> str:
    """Define the region fixture for reuse."""
    return "us-east-1"


@pytest.fixture
def sts_client(aws_creds, region) -> Generator[Any, None, None]:
    """Mock the STS boto client."""
    with mock_sts():
        client = boto3.client("sts", region_name=region)
        yield client


@pytest.fixture
def eks_client(aws_creds, region) -> Generator[Any, None, None]:
    """Mock the EKS boto client."""
    with mock_eks():
        client = boto3.client("eks", region_name=region)
        yield client