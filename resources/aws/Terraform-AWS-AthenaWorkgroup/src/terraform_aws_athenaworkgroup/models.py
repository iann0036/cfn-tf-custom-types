# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Configuration: Optional[Sequence["_Configuration"]]
    ResultConfiguration: Optional[Sequence["_ResultConfiguration"]]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            Configuration=json_data.get("Configuration"),
            ResultConfiguration=json_data.get("ResultConfiguration"),
            EncryptionConfiguration=json_data.get("EncryptionConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Configuration:
    BytesScannedCutoffPerQuery: Optional[float]
    EnforceWorkgroupConfiguration: Optional[bool]
    PublishCloudwatchMetricsEnabled: Optional[bool]
    ResultConfiguration: Optional[Sequence["_ResultConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            BytesScannedCutoffPerQuery=json_data.get("BytesScannedCutoffPerQuery"),
            EnforceWorkgroupConfiguration=json_data.get("EnforceWorkgroupConfiguration"),
            PublishCloudwatchMetricsEnabled=json_data.get("PublishCloudwatchMetricsEnabled"),
            ResultConfiguration=json_data.get("ResultConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


@dataclass
class ResultConfiguration:
    OutputLocation: Optional[str]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResultConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResultConfiguration"]:
        if not json_data:
            return None
        return cls(
            OutputLocation=json_data.get("OutputLocation"),
            EncryptionConfiguration=json_data.get("EncryptionConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResultConfiguration = ResultConfiguration


@dataclass
class EncryptionConfiguration:
    EncryptionOption: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            EncryptionOption=json_data.get("EncryptionOption"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


