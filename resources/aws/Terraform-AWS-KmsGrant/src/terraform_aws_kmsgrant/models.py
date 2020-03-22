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
    GrantCreationTokens: Optional[Sequence[str]]
    GrantId: Optional[str]
    GrantToken: Optional[str]
    GranteePrincipal: Optional[str]
    Id: Optional[str]
    KeyId: Optional[str]
    Name: Optional[str]
    Operations: Optional[Sequence[str]]
    RetireOnDelete: Optional[bool]
    RetiringPrincipal: Optional[str]
    Constraints: Optional[Sequence["_Constraints"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            GrantCreationTokens=json_data.get("GrantCreationTokens"),
            GrantId=json_data.get("GrantId"),
            GrantToken=json_data.get("GrantToken"),
            GranteePrincipal=json_data.get("GranteePrincipal"),
            Id=json_data.get("Id"),
            KeyId=json_data.get("KeyId"),
            Name=json_data.get("Name"),
            Operations=json_data.get("Operations"),
            RetireOnDelete=json_data.get("RetireOnDelete"),
            RetiringPrincipal=json_data.get("RetiringPrincipal"),
            Constraints=json_data.get("Constraints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Constraints:
    EncryptionContextEquals: Optional[Sequence["_EncryptionContextEquals"]]
    EncryptionContextSubset: Optional[Sequence["_EncryptionContextSubset"]]

    @classmethod
    def _deserialize(
        cls: Type["_Constraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Constraints"]:
        if not json_data:
            return None
        return cls(
            EncryptionContextEquals=json_data.get("EncryptionContextEquals"),
            EncryptionContextSubset=json_data.get("EncryptionContextSubset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Constraints = Constraints


@dataclass
class EncryptionContextEquals:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionContextEquals"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionContextEquals"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionContextEquals = EncryptionContextEquals


@dataclass
class EncryptionContextSubset:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionContextSubset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionContextSubset"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionContextSubset = EncryptionContextSubset


