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
    Description: Optional[str]
    Email: Optional[str]
    Id: Optional[str]
    Masters: Optional[Sequence[str]]
    Name: Optional[str]
    Region: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    Router: Optional[Sequence["_Router"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
            Masters=json_data.get("Masters"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            ValueSpecs=json_data.get("ValueSpecs"),
            Router=json_data.get("Router"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValueSpecs:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class Router:
    RouterId: Optional[str]
    RouterRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Router"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Router"]:
        if not json_data:
            return None
        return cls(
            RouterId=json_data.get("RouterId"),
            RouterRegion=json_data.get("RouterRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Router = Router


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


