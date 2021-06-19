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
    Constraints: Optional[Sequence["_ConstraintsDefinition"]]

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
            Constraints=deserialize_list(json_data.get("Constraints"), ConstraintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConstraintsDefinition(BaseModel):
    EncryptionContextEquals: Optional[Sequence["_EncryptionContextEqualsDefinition"]]
    EncryptionContextSubset: Optional[Sequence["_EncryptionContextSubsetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            EncryptionContextEquals=deserialize_list(json_data.get("EncryptionContextEquals"), EncryptionContextEqualsDefinition),
            EncryptionContextSubset=deserialize_list(json_data.get("EncryptionContextSubset"), EncryptionContextSubsetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsDefinition = ConstraintsDefinition


@dataclass
class EncryptionContextEqualsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionContextEqualsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionContextEqualsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionContextEqualsDefinition = EncryptionContextEqualsDefinition


@dataclass
class EncryptionContextSubsetDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionContextSubsetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionContextSubsetDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionContextSubsetDefinition = EncryptionContextSubsetDefinition


