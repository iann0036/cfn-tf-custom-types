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
    CustomDnsConfigs: Optional[Sequence["_CustomDnsConfigsDefinition"]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrivateDnsZoneConfigs: Optional[Sequence["_PrivateDnsZoneConfigsDefinition2"]]
    ResourceGroupName: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    PrivateDnsZoneGroup: Optional[Sequence["_PrivateDnsZoneGroupDefinition"]]
    PrivateServiceConnection: Optional[Sequence["_PrivateServiceConnectionDefinition"]]
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
            CustomDnsConfigs=deserialize_list(json_data.get("CustomDnsConfigs"), CustomDnsConfigsDefinition),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrivateDnsZoneConfigs=deserialize_list(json_data.get("PrivateDnsZoneConfigs"), PrivateDnsZoneConfigsDefinition2),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            PrivateDnsZoneGroup=deserialize_list(json_data.get("PrivateDnsZoneGroup"), PrivateDnsZoneGroupDefinition),
            PrivateServiceConnection=deserialize_list(json_data.get("PrivateServiceConnection"), PrivateServiceConnectionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomDnsConfigsDefinition(BaseModel):
    Fqdn: Optional[str]
    IpAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDnsConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDnsConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            Fqdn=json_data.get("Fqdn"),
            IpAddresses=json_data.get("IpAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDnsConfigsDefinition = CustomDnsConfigsDefinition


@dataclass
class PrivateDnsZoneConfigsDefinition2(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    PrivateDnsZoneId: Optional[str]
    RecordSets: Optional[Sequence["_PrivateDnsZoneConfigsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateDnsZoneConfigsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateDnsZoneConfigsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrivateDnsZoneId=json_data.get("PrivateDnsZoneId"),
            RecordSets=deserialize_list(json_data.get("RecordSets"), PrivateDnsZoneConfigsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateDnsZoneConfigsDefinition2 = PrivateDnsZoneConfigsDefinition2


@dataclass
class PrivateDnsZoneConfigsDefinition(BaseModel):
    Fqdn: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    Name: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateDnsZoneConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateDnsZoneConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            Fqdn=json_data.get("Fqdn"),
            IpAddresses=json_data.get("IpAddresses"),
            Name=json_data.get("Name"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateDnsZoneConfigsDefinition = PrivateDnsZoneConfigsDefinition


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
class PrivateDnsZoneGroupDefinition(BaseModel):
    Name: Optional[str]
    PrivateDnsZoneIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateDnsZoneGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateDnsZoneGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateDnsZoneIds=json_data.get("PrivateDnsZoneIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateDnsZoneGroupDefinition = PrivateDnsZoneGroupDefinition


@dataclass
class PrivateServiceConnectionDefinition(BaseModel):
    IsManualConnection: Optional[bool]
    Name: Optional[str]
    PrivateConnectionResourceAlias: Optional[str]
    PrivateConnectionResourceId: Optional[str]
    RequestMessage: Optional[str]
    SubresourceNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateServiceConnectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateServiceConnectionDefinition"]:
        if not json_data:
            return None
        return cls(
            IsManualConnection=json_data.get("IsManualConnection"),
            Name=json_data.get("Name"),
            PrivateConnectionResourceAlias=json_data.get("PrivateConnectionResourceAlias"),
            PrivateConnectionResourceId=json_data.get("PrivateConnectionResourceId"),
            RequestMessage=json_data.get("RequestMessage"),
            SubresourceNames=json_data.get("SubresourceNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateServiceConnectionDefinition = PrivateServiceConnectionDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


