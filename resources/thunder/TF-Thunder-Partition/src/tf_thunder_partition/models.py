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
    ApplicationType: Optional[str]
    Id: Optional[str]
    Id1: Optional[float]
    PartitionName: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    SharedVlan: Optional[Sequence["_SharedVlanDefinition"]]
    Template: Optional[Sequence["_TemplateDefinition"]]

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
            ApplicationType=json_data.get("ApplicationType"),
            Id=json_data.get("Id"),
            Id1=json_data.get("Id1"),
            PartitionName=json_data.get("PartitionName"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            SharedVlan=deserialize_list(json_data.get("SharedVlan"), SharedVlanDefinition),
            Template=deserialize_list(json_data.get("Template"), TemplateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SharedVlanDefinition(BaseModel):
    MgmtFloatingIpAddress: Optional[str]
    Uuid: Optional[str]
    Vlan: Optional[float]
    Vrid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SharedVlanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharedVlanDefinition"]:
        if not json_data:
            return None
        return cls(
            MgmtFloatingIpAddress=json_data.get("MgmtFloatingIpAddress"),
            Uuid=json_data.get("Uuid"),
            Vlan=json_data.get("Vlan"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharedVlanDefinition = SharedVlanDefinition


@dataclass
class TemplateDefinition(BaseModel):
    ResourceAccounting: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceAccounting=json_data.get("ResourceAccounting"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


