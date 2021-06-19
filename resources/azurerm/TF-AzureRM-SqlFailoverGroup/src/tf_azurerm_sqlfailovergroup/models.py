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
    Databases: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Role: Optional[str]
    ServerName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    PartnerServers: Optional[Sequence["_PartnerServersDefinition"]]
    ReadWriteEndpointFailoverPolicy: Optional[Sequence["_ReadWriteEndpointFailoverPolicyDefinition"]]
    ReadonlyEndpointFailoverPolicy: Optional[Sequence["_ReadonlyEndpointFailoverPolicyDefinition"]]
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
            Databases=json_data.get("Databases"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Role=json_data.get("Role"),
            ServerName=json_data.get("ServerName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            PartnerServers=deserialize_list(json_data.get("PartnerServers"), PartnerServersDefinition),
            ReadWriteEndpointFailoverPolicy=deserialize_list(json_data.get("ReadWriteEndpointFailoverPolicy"), ReadWriteEndpointFailoverPolicyDefinition),
            ReadonlyEndpointFailoverPolicy=deserialize_list(json_data.get("ReadonlyEndpointFailoverPolicy"), ReadonlyEndpointFailoverPolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class PartnerServersDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartnerServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartnerServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartnerServersDefinition = PartnerServersDefinition


@dataclass
class ReadWriteEndpointFailoverPolicyDefinition(BaseModel):
    GraceMinutes: Optional[float]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadWriteEndpointFailoverPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadWriteEndpointFailoverPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            GraceMinutes=json_data.get("GraceMinutes"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadWriteEndpointFailoverPolicyDefinition = ReadWriteEndpointFailoverPolicyDefinition


@dataclass
class ReadonlyEndpointFailoverPolicyDefinition(BaseModel):
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadonlyEndpointFailoverPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadonlyEndpointFailoverPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadonlyEndpointFailoverPolicyDefinition = ReadonlyEndpointFailoverPolicyDefinition


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


