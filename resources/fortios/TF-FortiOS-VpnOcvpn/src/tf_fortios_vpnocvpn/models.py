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
    AutoDiscovery: Optional[str]
    DynamicSortSubtable: Optional[str]
    Eap: Optional[str]
    EapUsers: Optional[str]
    Id: Optional[str]
    IpAllocationBlock: Optional[str]
    Multipath: Optional[str]
    Nat: Optional[str]
    PollInterval: Optional[float]
    Role: Optional[str]
    Sdwan: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    ForticlientAccess: Optional[Sequence["_ForticlientAccessDefinition"]]
    Overlays: Optional[Sequence["_OverlaysDefinition"]]
    WanInterface: Optional[Sequence["_WanInterfaceDefinition"]]

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
            AutoDiscovery=json_data.get("AutoDiscovery"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Eap=json_data.get("Eap"),
            EapUsers=json_data.get("EapUsers"),
            Id=json_data.get("Id"),
            IpAllocationBlock=json_data.get("IpAllocationBlock"),
            Multipath=json_data.get("Multipath"),
            Nat=json_data.get("Nat"),
            PollInterval=json_data.get("PollInterval"),
            Role=json_data.get("Role"),
            Sdwan=json_data.get("Sdwan"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            ForticlientAccess=deserialize_list(json_data.get("ForticlientAccess"), ForticlientAccessDefinition),
            Overlays=deserialize_list(json_data.get("Overlays"), OverlaysDefinition),
            WanInterface=deserialize_list(json_data.get("WanInterface"), WanInterfaceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ForticlientAccessDefinition(BaseModel):
    Psksecret: Optional[str]
    Status: Optional[str]
    AuthGroups: Optional[Sequence["_AuthGroupsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Psksecret=json_data.get("Psksecret"),
            Status=json_data.get("Status"),
            AuthGroups=deserialize_list(json_data.get("AuthGroups"), AuthGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientAccessDefinition = ForticlientAccessDefinition


@dataclass
class AuthGroupsDefinition(BaseModel):
    AuthGroup: Optional[str]
    Name: Optional[str]
    Overlays: Optional[Sequence["_OverlaysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthGroup=json_data.get("AuthGroup"),
            Name=json_data.get("Name"),
            Overlays=deserialize_list(json_data.get("Overlays"), OverlaysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthGroupsDefinition = AuthGroupsDefinition


@dataclass
class OverlaysDefinition(BaseModel):
    OverlayName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverlaysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverlaysDefinition"]:
        if not json_data:
            return None
        return cls(
            OverlayName=json_data.get("OverlayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverlaysDefinition = OverlaysDefinition


@dataclass
class WanInterfaceDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WanInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WanInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WanInterfaceDefinition = WanInterfaceDefinition


