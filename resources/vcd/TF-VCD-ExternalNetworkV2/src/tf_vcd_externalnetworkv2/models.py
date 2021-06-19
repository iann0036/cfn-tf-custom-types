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
    Id: Optional[str]
    Name: Optional[str]
    IpScope: Optional[Sequence["_IpScopeDefinition"]]
    NsxtNetwork: Optional[Sequence["_NsxtNetworkDefinition"]]
    VsphereNetwork: Optional[Sequence["_VsphereNetworkDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            IpScope=deserialize_list(json_data.get("IpScope"), IpScopeDefinition),
            NsxtNetwork=deserialize_list(json_data.get("NsxtNetwork"), NsxtNetworkDefinition),
            VsphereNetwork=deserialize_list(json_data.get("VsphereNetwork"), VsphereNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpScopeDefinition(BaseModel):
    Dns1: Optional[str]
    Dns2: Optional[str]
    DnsSuffix: Optional[str]
    Enabled: Optional[bool]
    Gateway: Optional[str]
    PrefixLength: Optional[float]
    StaticIpPool: Optional[Sequence["_StaticIpPoolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            Dns1=json_data.get("Dns1"),
            Dns2=json_data.get("Dns2"),
            DnsSuffix=json_data.get("DnsSuffix"),
            Enabled=json_data.get("Enabled"),
            Gateway=json_data.get("Gateway"),
            PrefixLength=json_data.get("PrefixLength"),
            StaticIpPool=deserialize_list(json_data.get("StaticIpPool"), StaticIpPoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpScopeDefinition = IpScopeDefinition


@dataclass
class StaticIpPoolDefinition(BaseModel):
    EndAddress: Optional[str]
    StartAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticIpPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticIpPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            EndAddress=json_data.get("EndAddress"),
            StartAddress=json_data.get("StartAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticIpPoolDefinition = StaticIpPoolDefinition


@dataclass
class NsxtNetworkDefinition(BaseModel):
    NsxtManagerId: Optional[str]
    NsxtTier0RouterId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NsxtNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxtNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            NsxtManagerId=json_data.get("NsxtManagerId"),
            NsxtTier0RouterId=json_data.get("NsxtTier0RouterId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxtNetworkDefinition = NsxtNetworkDefinition


@dataclass
class VsphereNetworkDefinition(BaseModel):
    PortgroupId: Optional[str]
    VcenterId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VsphereNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsphereNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            PortgroupId=json_data.get("PortgroupId"),
            VcenterId=json_data.get("VcenterId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsphereNetworkDefinition = VsphereNetworkDefinition


