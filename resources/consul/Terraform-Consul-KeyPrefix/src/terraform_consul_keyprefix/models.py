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
    PathPrefix: Optional[str]
    Subkeys: Optional[Sequence["_Subkeys"]]
    Token: Optional[str]
    Subkey: Optional[Sequence["_Subkey"]]

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
            PathPrefix=json_data.get("PathPrefix"),
            Subkeys=json_data.get("Subkeys"),
            Token=json_data.get("Token"),
            Subkey=json_data.get("Subkey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Subkeys:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subkeys"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subkeys"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subkeys = Subkeys


@dataclass
class Subkey:
    Flags: Optional[float]
    Path: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subkey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subkey"]:
        if not json_data:
            return None
        return cls(
            Flags=json_data.get("Flags"),
            Path=json_data.get("Path"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subkey = Subkey


