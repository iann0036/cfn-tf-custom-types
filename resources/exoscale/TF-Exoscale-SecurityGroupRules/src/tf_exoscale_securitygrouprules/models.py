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
    Id: Optional[str]
    SecurityGroup: Optional[str]
    SecurityGroupId: Optional[str]
    Egress: Optional[Sequence["_EgressDefinition"]]
    Ingress: Optional[Sequence["_IngressDefinition"]]
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
            Id=json_data.get("Id"),
            SecurityGroup=json_data.get("SecurityGroup"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Egress=deserialize_list(json_data.get("Egress"), EgressDefinition),
            Ingress=deserialize_list(json_data.get("Ingress"), IngressDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EgressDefinition(BaseModel):
    CidrList: Optional[Sequence[str]]
    Description: Optional[str]
    IcmpCode: Optional[float]
    IcmpType: Optional[float]
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]
    UserSecurityGroupList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EgressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrList=json_data.get("CidrList"),
            Description=json_data.get("Description"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
            UserSecurityGroupList=json_data.get("UserSecurityGroupList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressDefinition = EgressDefinition


@dataclass
class IngressDefinition(BaseModel):
    CidrList: Optional[Sequence[str]]
    Description: Optional[str]
    IcmpCode: Optional[float]
    IcmpType: Optional[float]
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]
    UserSecurityGroupList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrList=json_data.get("CidrList"),
            Description=json_data.get("Description"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
            UserSecurityGroupList=json_data.get("UserSecurityGroupList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressDefinition = IngressDefinition


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


