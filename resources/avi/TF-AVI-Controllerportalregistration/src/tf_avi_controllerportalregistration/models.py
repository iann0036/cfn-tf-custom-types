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
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Asset: Optional[Sequence["_AssetDefinition"]]
    PortalAuth: Optional[Sequence["_PortalAuthDefinition"]]

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
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Asset=deserialize_list(json_data.get("Asset"), AssetDefinition),
            PortalAuth=deserialize_list(json_data.get("PortalAuth"), PortalAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AssetDefinition(BaseModel):
    AssetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetDefinition"]:
        if not json_data:
            return None
        return cls(
            AssetId=json_data.get("AssetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetDefinition = AssetDefinition


@dataclass
class PortalAuthDefinition(BaseModel):
    AccessToken: Optional[str]
    InstanceUrl: Optional[str]
    JwtToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortalAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortalAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessToken=json_data.get("AccessToken"),
            InstanceUrl=json_data.get("InstanceUrl"),
            JwtToken=json_data.get("JwtToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortalAuthDefinition = PortalAuthDefinition


