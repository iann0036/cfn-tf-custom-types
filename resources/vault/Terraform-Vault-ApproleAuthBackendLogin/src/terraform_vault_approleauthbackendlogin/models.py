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
    Accessor: Optional[str]
    Backend: Optional[str]
    ClientToken: Optional[str]
    Id: Optional[str]
    LeaseDuration: Optional[float]
    LeaseStarted: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Policies: Optional[Sequence[str]]
    Renewable: Optional[bool]
    RoleId: Optional[str]
    SecretId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Accessor=json_data.get("Accessor"),
            Backend=json_data.get("Backend"),
            ClientToken=json_data.get("ClientToken"),
            Id=json_data.get("Id"),
            LeaseDuration=json_data.get("LeaseDuration"),
            LeaseStarted=json_data.get("LeaseStarted"),
            Metadata=json_data.get("Metadata"),
            Policies=json_data.get("Policies"),
            Renewable=json_data.get("Renewable"),
            RoleId=json_data.get("RoleId"),
            SecretId=json_data.get("SecretId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


