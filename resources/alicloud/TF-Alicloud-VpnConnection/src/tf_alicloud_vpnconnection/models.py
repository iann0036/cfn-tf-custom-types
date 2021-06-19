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
    CustomerGatewayId: Optional[str]
    EffectImmediately: Optional[bool]
    Id: Optional[str]
    LocalSubnet: Optional[Sequence[str]]
    Name: Optional[str]
    RemoteSubnet: Optional[Sequence[str]]
    Status: Optional[str]
    VpnGatewayId: Optional[str]
    IkeConfig: Optional[Sequence["_IkeConfigDefinition"]]
    IpsecConfig: Optional[Sequence["_IpsecConfigDefinition"]]

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
            CustomerGatewayId=json_data.get("CustomerGatewayId"),
            EffectImmediately=json_data.get("EffectImmediately"),
            Id=json_data.get("Id"),
            LocalSubnet=json_data.get("LocalSubnet"),
            Name=json_data.get("Name"),
            RemoteSubnet=json_data.get("RemoteSubnet"),
            Status=json_data.get("Status"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
            IkeConfig=deserialize_list(json_data.get("IkeConfig"), IkeConfigDefinition),
            IpsecConfig=deserialize_list(json_data.get("IpsecConfig"), IpsecConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IkeConfigDefinition(BaseModel):
    IkeAuthAlg: Optional[str]
    IkeEncAlg: Optional[str]
    IkeLifetime: Optional[float]
    IkeLocalId: Optional[str]
    IkeMode: Optional[str]
    IkePfs: Optional[str]
    IkeRemoteId: Optional[str]
    IkeVersion: Optional[str]
    Psk: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IkeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IkeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IkeAuthAlg=json_data.get("IkeAuthAlg"),
            IkeEncAlg=json_data.get("IkeEncAlg"),
            IkeLifetime=json_data.get("IkeLifetime"),
            IkeLocalId=json_data.get("IkeLocalId"),
            IkeMode=json_data.get("IkeMode"),
            IkePfs=json_data.get("IkePfs"),
            IkeRemoteId=json_data.get("IkeRemoteId"),
            IkeVersion=json_data.get("IkeVersion"),
            Psk=json_data.get("Psk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IkeConfigDefinition = IkeConfigDefinition


@dataclass
class IpsecConfigDefinition(BaseModel):
    IpsecAuthAlg: Optional[str]
    IpsecEncAlg: Optional[str]
    IpsecLifetime: Optional[float]
    IpsecPfs: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpsecConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IpsecAuthAlg=json_data.get("IpsecAuthAlg"),
            IpsecEncAlg=json_data.get("IpsecEncAlg"),
            IpsecLifetime=json_data.get("IpsecLifetime"),
            IpsecPfs=json_data.get("IpsecPfs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsecConfigDefinition = IpsecConfigDefinition


