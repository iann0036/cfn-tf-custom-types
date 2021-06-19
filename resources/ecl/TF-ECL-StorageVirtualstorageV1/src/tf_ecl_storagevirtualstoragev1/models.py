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
    Description: Optional[str]
    ErrorMessage: Optional[str]
    Id: Optional[str]
    IpAddrPool: Optional[Sequence["_IpAddrPoolDefinition"]]
    Name: Optional[str]
    NetworkId: Optional[str]
    SubnetId: Optional[str]
    VolumeTypeId: Optional[str]
    VolumeTypeName: Optional[str]
    HostRoutes: Optional[Sequence["_HostRoutesDefinition"]]
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
            Description=json_data.get("Description"),
            ErrorMessage=json_data.get("ErrorMessage"),
            Id=json_data.get("Id"),
            IpAddrPool=deserialize_list(json_data.get("IpAddrPool"), IpAddrPoolDefinition),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            SubnetId=json_data.get("SubnetId"),
            VolumeTypeId=json_data.get("VolumeTypeId"),
            VolumeTypeName=json_data.get("VolumeTypeName"),
            HostRoutes=deserialize_list(json_data.get("HostRoutes"), HostRoutesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpAddrPoolDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrPoolDefinition = IpAddrPoolDefinition


@dataclass
class HostRoutesDefinition(BaseModel):
    Destination: Optional[str]
    Nexthop: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostRoutesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostRoutesDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            Nexthop=json_data.get("Nexthop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostRoutesDefinition = HostRoutesDefinition


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


