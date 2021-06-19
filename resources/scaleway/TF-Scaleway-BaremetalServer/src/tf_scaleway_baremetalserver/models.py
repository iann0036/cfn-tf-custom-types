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
    Domain: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Ips: Optional[Sequence["_IpsDefinition"]]
    Name: Optional[str]
    Offer: Optional[str]
    OfferId: Optional[str]
    OrganizationId: Optional[str]
    Os: Optional[str]
    OsId: Optional[str]
    ProjectId: Optional[str]
    SshKeyIds: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    Zone: Optional[str]
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
            Domain=json_data.get("Domain"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Ips=deserialize_list(json_data.get("Ips"), IpsDefinition),
            Name=json_data.get("Name"),
            Offer=json_data.get("Offer"),
            OfferId=json_data.get("OfferId"),
            OrganizationId=json_data.get("OrganizationId"),
            Os=json_data.get("Os"),
            OsId=json_data.get("OsId"),
            ProjectId=json_data.get("ProjectId"),
            SshKeyIds=json_data.get("SshKeyIds"),
            Tags=json_data.get("Tags"),
            Zone=json_data.get("Zone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpsDefinition(BaseModel):
    Address: Optional[str]
    Id: Optional[str]
    Reverse: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Id=json_data.get("Id"),
            Reverse=json_data.get("Reverse"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsDefinition = IpsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


