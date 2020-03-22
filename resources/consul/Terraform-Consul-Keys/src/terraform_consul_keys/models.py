# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Datacenter: Optional[str]
    Id: Optional[str]
    Token: Optional[str]
    Var: Optional[Sequence["_Var"]]
    Key: Optional[Sequence["_Key"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Datacenter=json_data.get("Datacenter"),
            Id=json_data.get("Id"),
            Token=json_data.get("Token"),
            Var=json_data.get("Var"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Var:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Var"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Var"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Var = Var


@dataclass
class Key:
    Default: Optional[str]
    Delete: Optional[bool]
    Flags: Optional[float]
    Name: Optional[str]
    Path: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Key"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Key"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Flags=json_data.get("Flags"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Key = Key


