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
    Config: Optional[Sequence["_ConfigDefinition"]]
    ConfigJson: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    MaxTokenTtl: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    TokenLocality: Optional[str]
    Type: Optional[str]
    NamespaceRule: Optional[Sequence["_NamespaceRuleDefinition"]]

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
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            ConfigJson=json_data.get("ConfigJson"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MaxTokenTtl=json_data.get("MaxTokenTtl"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            TokenLocality=json_data.get("TokenLocality"),
            Type=json_data.get("Type"),
            NamespaceRule=deserialize_list(json_data.get("NamespaceRule"), NamespaceRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class NamespaceRuleDefinition(BaseModel):
    BindNamespace: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NamespaceRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamespaceRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            BindNamespace=json_data.get("BindNamespace"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamespaceRuleDefinition = NamespaceRuleDefinition


