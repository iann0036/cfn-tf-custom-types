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
    BackendId: Optional[str]
    CertificateId: Optional[str]
    Id: Optional[str]
    InboundPort: Optional[float]
    LbId: Optional[str]
    Name: Optional[str]
    TimeoutClient: Optional[str]
    Acl: Optional[Sequence["_AclDefinition"]]
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
            BackendId=json_data.get("BackendId"),
            CertificateId=json_data.get("CertificateId"),
            Id=json_data.get("Id"),
            InboundPort=json_data.get("InboundPort"),
            LbId=json_data.get("LbId"),
            Name=json_data.get("Name"),
            TimeoutClient=json_data.get("TimeoutClient"),
            Acl=deserialize_list(json_data.get("Acl"), AclDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AclDefinition(BaseModel):
    Name: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclDefinition = AclDefinition


@dataclass
class ActionDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class MatchDefinition(BaseModel):
    HttpFilter: Optional[str]
    HttpFilterValue: Optional[Sequence[str]]
    Invert: Optional[bool]
    IpSubnet: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpFilter=json_data.get("HttpFilter"),
            HttpFilterValue=json_data.get("HttpFilterValue"),
            Invert=json_data.get("Invert"),
            IpSubnet=json_data.get("IpSubnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


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


