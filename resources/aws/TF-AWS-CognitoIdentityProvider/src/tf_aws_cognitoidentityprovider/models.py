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
    AttributeMapping: Optional[Sequence["_AttributeMappingDefinition"]]
    Id: Optional[str]
    IdpIdentifiers: Optional[Sequence[str]]
    ProviderDetails: Optional[Sequence["_ProviderDetailsDefinition"]]
    ProviderName: Optional[str]
    ProviderType: Optional[str]
    UserPoolId: Optional[str]

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
            AttributeMapping=deserialize_list(json_data.get("AttributeMapping"), AttributeMappingDefinition),
            Id=json_data.get("Id"),
            IdpIdentifiers=json_data.get("IdpIdentifiers"),
            ProviderDetails=deserialize_list(json_data.get("ProviderDetails"), ProviderDetailsDefinition),
            ProviderName=json_data.get("ProviderName"),
            ProviderType=json_data.get("ProviderType"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttributeMappingDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeMappingDefinition = AttributeMappingDefinition


@dataclass
class ProviderDetailsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProviderDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProviderDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProviderDetailsDefinition = ProviderDetailsDefinition


