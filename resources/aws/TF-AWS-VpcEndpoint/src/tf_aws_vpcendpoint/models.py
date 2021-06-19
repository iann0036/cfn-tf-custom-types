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
    AutoAccept: Optional[bool]
    CidrBlocks: Optional[Sequence[str]]
    DnsEntry: Optional[Sequence["_DnsEntryDefinition"]]
    Id: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
    OwnerId: Optional[str]
    Policy: Optional[str]
    PrefixListId: Optional[str]
    PrivateDnsEnabled: Optional[bool]
    RequesterManaged: Optional[bool]
    RouteTableIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    ServiceName: Optional[str]
    State: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcEndpointType: Optional[str]
    VpcId: Optional[str]
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
            Arn=json_data.get("Arn"),
            AutoAccept=json_data.get("AutoAccept"),
            CidrBlocks=json_data.get("CidrBlocks"),
            DnsEntry=deserialize_list(json_data.get("DnsEntry"), DnsEntryDefinition),
            Id=json_data.get("Id"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            OwnerId=json_data.get("OwnerId"),
            Policy=json_data.get("Policy"),
            PrefixListId=json_data.get("PrefixListId"),
            PrivateDnsEnabled=json_data.get("PrivateDnsEnabled"),
            RequesterManaged=json_data.get("RequesterManaged"),
            RouteTableIds=json_data.get("RouteTableIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            ServiceName=json_data.get("ServiceName"),
            State=json_data.get("State"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcEndpointType=json_data.get("VpcEndpointType"),
            VpcId=json_data.get("VpcId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsEntryDefinition(BaseModel):
    DnsName: Optional[str]
    HostedZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsName=json_data.get("DnsName"),
            HostedZoneId=json_data.get("HostedZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsEntryDefinition = DnsEntryDefinition


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
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


