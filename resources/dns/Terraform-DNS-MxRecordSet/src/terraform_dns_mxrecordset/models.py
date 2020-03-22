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
    Id: Optional[str]
    Name: Optional[str]
    Ttl: Optional[float]
    Zone: Optional[str]
    Mx: Optional[Sequence["_Mx"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Ttl=json_data.get("Ttl"),
            Zone=json_data.get("Zone"),
            Mx=json_data.get("Mx"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Mx:
    Exchange: Optional[str]
    Preference: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Mx"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mx"]:
        if not json_data:
            return None
        return cls(
            Exchange=json_data.get("Exchange"),
            Preference=json_data.get("Preference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mx = Mx


