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
    Account: Optional[Sequence["_AccountDefinition"]]
    Id: Optional[str]
    KeystoreDir: Optional[str]
    KeystoreDirAbs: Optional[str]
    UseLightWeightKdf: Optional[bool]

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
            Account=deserialize_list(json_data.get("Account"), AccountDefinition),
            Id=json_data.get("Id"),
            KeystoreDir=json_data.get("KeystoreDir"),
            KeystoreDirAbs=json_data.get("KeystoreDirAbs"),
            UseLightWeightKdf=json_data.get("UseLightWeightKdf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountDefinition(BaseModel):
    AccountUrl: Optional[str]
    Address: Optional[str]
    Balance: Optional[str]
    Passphrase: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountUrl=json_data.get("AccountUrl"),
            Address=json_data.get("Address"),
            Balance=json_data.get("Balance"),
            Passphrase=json_data.get("Passphrase"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountDefinition = AccountDefinition

