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
    CreatedBy: Optional[str]
    Description: Optional[str]
    EnforceLabelGroup: Optional[bool]
    Id: Optional[str]
    LabelGroupRefs: Optional[Sequence[str]]
    Local: Optional[bool]
    Name: Optional[str]
    Uuid: Optional[str]
    ConfigSettings: Optional[Sequence["_ConfigSettingsDefinition"]]

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
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            EnforceLabelGroup=json_data.get("EnforceLabelGroup"),
            Id=json_data.get("Id"),
            LabelGroupRefs=json_data.get("LabelGroupRefs"),
            Local=json_data.get("Local"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
            ConfigSettings=deserialize_list(json_data.get("ConfigSettings"), ConfigSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigSettingsDefinition(BaseModel):
    SeInProviderContext: Optional[bool]
    TenantAccessToProviderSe: Optional[bool]
    TenantVrf: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            SeInProviderContext=json_data.get("SeInProviderContext"),
            TenantAccessToProviderSe=json_data.get("TenantAccessToProviderSe"),
            TenantVrf=json_data.get("TenantVrf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigSettingsDefinition = ConfigSettingsDefinition


