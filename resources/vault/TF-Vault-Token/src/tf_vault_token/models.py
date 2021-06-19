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
    ClientToken: Optional[str]
    DisplayName: Optional[str]
    EncryptedClientToken: Optional[str]
    ExplicitMaxTtl: Optional[str]
    Id: Optional[str]
    LeaseDuration: Optional[float]
    LeaseStarted: Optional[str]
    NoDefaultPolicy: Optional[bool]
    NoParent: Optional[bool]
    NumUses: Optional[float]
    Period: Optional[str]
    PgpKey: Optional[str]
    Policies: Optional[Sequence[str]]
    RenewIncrement: Optional[float]
    RenewMinLease: Optional[float]
    Renewable: Optional[bool]
    RoleName: Optional[str]
    Ttl: Optional[str]
    WrappedToken: Optional[str]
    WrappingAccessor: Optional[str]
    WrappingTtl: Optional[str]

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
            ClientToken=json_data.get("ClientToken"),
            DisplayName=json_data.get("DisplayName"),
            EncryptedClientToken=json_data.get("EncryptedClientToken"),
            ExplicitMaxTtl=json_data.get("ExplicitMaxTtl"),
            Id=json_data.get("Id"),
            LeaseDuration=json_data.get("LeaseDuration"),
            LeaseStarted=json_data.get("LeaseStarted"),
            NoDefaultPolicy=json_data.get("NoDefaultPolicy"),
            NoParent=json_data.get("NoParent"),
            NumUses=json_data.get("NumUses"),
            Period=json_data.get("Period"),
            PgpKey=json_data.get("PgpKey"),
            Policies=json_data.get("Policies"),
            RenewIncrement=json_data.get("RenewIncrement"),
            RenewMinLease=json_data.get("RenewMinLease"),
            Renewable=json_data.get("Renewable"),
            RoleName=json_data.get("RoleName"),
            Ttl=json_data.get("Ttl"),
            WrappedToken=json_data.get("WrappedToken"),
            WrappingAccessor=json_data.get("WrappingAccessor"),
            WrappingTtl=json_data.get("WrappingTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


