# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    AvailabilityZoneId: Optional[str]
    AvailabilityZoneName: Optional[str]
    CreationToken: Optional[str]
    DnsName: Optional[str]
    Encrypted: Optional[bool]
    Id: Optional[str]
    KmsKeyId: Optional[str]
    NumberOfMountTargets: Optional[float]
    OwnerId: Optional[str]
    PerformanceMode: Optional[str]
    ProvisionedThroughputInMibps: Optional[float]
    SizeInBytes: Optional[Sequence["_SizeInBytesDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ThroughputMode: Optional[str]
    LifecyclePolicy: Optional[Sequence["_LifecyclePolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AvailabilityZoneId=json_data.get("AvailabilityZoneId"),
            AvailabilityZoneName=json_data.get("AvailabilityZoneName"),
            CreationToken=json_data.get("CreationToken"),
            DnsName=json_data.get("DnsName"),
            Encrypted=json_data.get("Encrypted"),
            Id=json_data.get("Id"),
            KmsKeyId=json_data.get("KmsKeyId"),
            NumberOfMountTargets=json_data.get("NumberOfMountTargets"),
            OwnerId=json_data.get("OwnerId"),
            PerformanceMode=json_data.get("PerformanceMode"),
            ProvisionedThroughputInMibps=json_data.get("ProvisionedThroughputInMibps"),
            SizeInBytes=deserialize_list(json_data.get("SizeInBytes"), SizeInBytesDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ThroughputMode=json_data.get("ThroughputMode"),
            LifecyclePolicy=deserialize_list(json_data.get("LifecyclePolicy"), LifecyclePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SizeInBytesDefinition(BaseModel):
    Value: Optional[float]
    ValueInIa: Optional[float]
    ValueInStandard: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SizeInBytesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SizeInBytesDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            ValueInIa=json_data.get("ValueInIa"),
            ValueInStandard=json_data.get("ValueInStandard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SizeInBytesDefinition = SizeInBytesDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class LifecyclePolicyDefinition(BaseModel):
    TransitionToIa: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecyclePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecyclePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            TransitionToIa=json_data.get("TransitionToIa"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecyclePolicyDefinition = LifecyclePolicyDefinition


