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
    DnsName: Optional[str]
    Enabled: Optional[bool]
    HostedZoneId: Optional[str]
    Id: Optional[str]
    IpAddressType: Optional[str]
    IpSets: Optional[Sequence["_IpSetsDefinition"]]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Attributes: Optional[Sequence["_AttributesDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DnsName=json_data.get("DnsName"),
            Enabled=json_data.get("Enabled"),
            HostedZoneId=json_data.get("HostedZoneId"),
            Id=json_data.get("Id"),
            IpAddressType=json_data.get("IpAddressType"),
            IpSets=deserialize_list(json_data.get("IpSets"), IpSetsDefinition),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Attributes=deserialize_list(json_data.get("Attributes"), AttributesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpSetsDefinition(BaseModel):
    IpAddresses: Optional[Sequence[str]]
    IpFamily: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpSetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSetsDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddresses=json_data.get("IpAddresses"),
            IpFamily=json_data.get("IpFamily"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSetsDefinition = IpSetsDefinition


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
class AttributesDefinition(BaseModel):
    FlowLogsEnabled: Optional[bool]
    FlowLogsS3Bucket: Optional[str]
    FlowLogsS3Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            FlowLogsEnabled=json_data.get("FlowLogsEnabled"),
            FlowLogsS3Bucket=json_data.get("FlowLogsS3Bucket"),
            FlowLogsS3Prefix=json_data.get("FlowLogsS3Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributesDefinition = AttributesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


