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
    Cert: Optional[str]
    EntityId: Optional[str]
    GroupName: Optional[str]
    Id: Optional[str]
    IdpCert: Optional[str]
    IdpEntityId: Optional[str]
    IdpSingleLogoutUrl: Optional[str]
    IdpSingleSignOnUrl: Optional[str]
    Name: Optional[str]
    SingleLogoutUrl: Optional[str]
    SingleSignOnUrl: Optional[str]
    UserName: Optional[str]
    Vdomparam: Optional[str]

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
            Cert=json_data.get("Cert"),
            EntityId=json_data.get("EntityId"),
            GroupName=json_data.get("GroupName"),
            Id=json_data.get("Id"),
            IdpCert=json_data.get("IdpCert"),
            IdpEntityId=json_data.get("IdpEntityId"),
            IdpSingleLogoutUrl=json_data.get("IdpSingleLogoutUrl"),
            IdpSingleSignOnUrl=json_data.get("IdpSingleSignOnUrl"),
            Name=json_data.get("Name"),
            SingleLogoutUrl=json_data.get("SingleLogoutUrl"),
            SingleSignOnUrl=json_data.get("SingleSignOnUrl"),
            UserName=json_data.get("UserName"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


