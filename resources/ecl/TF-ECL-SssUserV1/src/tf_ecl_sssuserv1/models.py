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
    BrandId: Optional[str]
    ContractId: Optional[str]
    ContractOwner: Optional[bool]
    ExternalReferenceId: Optional[str]
    Id: Optional[str]
    KeystoneEndpoint: Optional[str]
    KeystoneName: Optional[str]
    KeystonePassword: Optional[str]
    LoginId: Optional[str]
    LoginIntegration: Optional[str]
    MailAddress: Optional[str]
    NotifyPassword: Optional[str]
    Password: Optional[str]
    SssEndpoint: Optional[str]
    StartTime: Optional[str]
    UserId: Optional[str]

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
            BrandId=json_data.get("BrandId"),
            ContractId=json_data.get("ContractId"),
            ContractOwner=json_data.get("ContractOwner"),
            ExternalReferenceId=json_data.get("ExternalReferenceId"),
            Id=json_data.get("Id"),
            KeystoneEndpoint=json_data.get("KeystoneEndpoint"),
            KeystoneName=json_data.get("KeystoneName"),
            KeystonePassword=json_data.get("KeystonePassword"),
            LoginId=json_data.get("LoginId"),
            LoginIntegration=json_data.get("LoginIntegration"),
            MailAddress=json_data.get("MailAddress"),
            NotifyPassword=json_data.get("NotifyPassword"),
            Password=json_data.get("Password"),
            SssEndpoint=json_data.get("SssEndpoint"),
            StartTime=json_data.get("StartTime"),
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


