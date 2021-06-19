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
    HubNetwork: Optional[Sequence["_HubNetworkDefinition"]]
    HubNetworkEnable: Optional[bool]
    Id: Optional[str]
    RegionName: Optional[str]
    SchemaId: Optional[str]
    SiteId: Optional[str]
    TemplateName: Optional[str]
    VpnGateway: Optional[bool]
    VrfName: Optional[str]
    Cidr: Optional[Sequence["_CidrDefinition"]]

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
            HubNetwork=deserialize_list(json_data.get("HubNetwork"), HubNetworkDefinition),
            HubNetworkEnable=json_data.get("HubNetworkEnable"),
            Id=json_data.get("Id"),
            RegionName=json_data.get("RegionName"),
            SchemaId=json_data.get("SchemaId"),
            SiteId=json_data.get("SiteId"),
            TemplateName=json_data.get("TemplateName"),
            VpnGateway=json_data.get("VpnGateway"),
            VrfName=json_data.get("VrfName"),
            Cidr=deserialize_list(json_data.get("Cidr"), CidrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HubNetworkDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HubNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HubNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HubNetworkDefinition = HubNetworkDefinition


@dataclass
class CidrDefinition(BaseModel):
    CidrIp: Optional[str]
    Primary: Optional[bool]
    Subnet: Optional[Sequence["_SubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CidrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CidrDefinition"]:
        if not json_data:
            return None
        return cls(
            CidrIp=json_data.get("CidrIp"),
            Primary=json_data.get("Primary"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CidrDefinition = CidrDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Ip: Optional[str]
    Usage: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Usage=json_data.get("Usage"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


