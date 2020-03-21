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
    CreationToken: Optional[str]
    DnsName: Optional[str]
    Encrypted: Optional[bool]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    PerformanceMode: Optional[str]
    ProvisionedThroughputInMibps: Optional[float]
    ReferenceName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ThroughputMode: Optional[str]
    LifecyclePolicy: Optional[Sequence["_LifecyclePolicy"]]

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
            CreationToken=json_data.get("CreationToken"),
            DnsName=json_data.get("DnsName"),
            Encrypted=json_data.get("Encrypted"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            PerformanceMode=json_data.get("PerformanceMode"),
            ProvisionedThroughputInMibps=json_data.get("ProvisionedThroughputInMibps"),
            ReferenceName=json_data.get("ReferenceName"),
            Tags=json_data.get("Tags"),
            ThroughputMode=json_data.get("ThroughputMode"),
            LifecyclePolicy=json_data.get("LifecyclePolicy"),
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
class LifecyclePolicy:
    TransitionToIa: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecyclePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecyclePolicy"]:
        if not json_data:
            return None
        return cls(
            TransitionToIa=json_data.get("TransitionToIa"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecyclePolicy = LifecyclePolicy


