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
    DedicateExternalNetwork: Optional[bool]
    Description: Optional[str]
    EdgeClusterId: Optional[str]
    ExternalNetworkId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    PrimaryIp: Optional[str]
    Vdc: Optional[str]
    Subnet: Optional[Sequence["_SubnetDefinition"]]

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
            DedicateExternalNetwork=json_data.get("DedicateExternalNetwork"),
            Description=json_data.get("Description"),
            EdgeClusterId=json_data.get("EdgeClusterId"),
            ExternalNetworkId=json_data.get("ExternalNetworkId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            PrimaryIp=json_data.get("PrimaryIp"),
            Vdc=json_data.get("Vdc"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SubnetDefinition(BaseModel):
    Gateway: Optional[str]
    PrefixLength: Optional[float]
    PrimaryIp: Optional[str]
    AllocatedIps: Optional[Sequence["_AllocatedIpsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Gateway=json_data.get("Gateway"),
            PrefixLength=json_data.get("PrefixLength"),
            PrimaryIp=json_data.get("PrimaryIp"),
            AllocatedIps=deserialize_list(json_data.get("AllocatedIps"), AllocatedIpsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


@dataclass
class AllocatedIpsDefinition(BaseModel):
    EndAddress: Optional[str]
    StartAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllocatedIpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllocatedIpsDefinition"]:
        if not json_data:
            return None
        return cls(
            EndAddress=json_data.get("EndAddress"),
            StartAddress=json_data.get("StartAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllocatedIpsDefinition = AllocatedIpsDefinition


