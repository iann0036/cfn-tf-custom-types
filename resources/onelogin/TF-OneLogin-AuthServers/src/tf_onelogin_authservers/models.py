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
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]

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
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConfigurationDefinition(BaseModel):
    AccessTokenExpirationMinutes: Optional[float]
    Audiences: Optional[Sequence[str]]
    RefreshTokenExpirationMinutes: Optional[float]
    ResourceIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessTokenExpirationMinutes=json_data.get("AccessTokenExpirationMinutes"),
            Audiences=json_data.get("Audiences"),
            RefreshTokenExpirationMinutes=json_data.get("RefreshTokenExpirationMinutes"),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


