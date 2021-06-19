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
    Datacenter: Optional[str]
    Id: Optional[str]
    Namespace: Optional[str]
    PathPrefix: Optional[str]
    Subkeys: Optional[Sequence["_SubkeysDefinition"]]
    Token: Optional[str]
    Subkey: Optional[Sequence["_SubkeyDefinition"]]

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
            Datacenter=json_data.get("Datacenter"),
            Id=json_data.get("Id"),
            Namespace=json_data.get("Namespace"),
            PathPrefix=json_data.get("PathPrefix"),
            Subkeys=deserialize_list(json_data.get("Subkeys"), SubkeysDefinition),
            Token=json_data.get("Token"),
            Subkey=deserialize_list(json_data.get("Subkey"), SubkeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SubkeysDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubkeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubkeysDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubkeysDefinition = SubkeysDefinition


@dataclass
class SubkeyDefinition(BaseModel):
    Flags: Optional[float]
    Path: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubkeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubkeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Flags=json_data.get("Flags"),
            Path=json_data.get("Path"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubkeyDefinition = SubkeyDefinition


