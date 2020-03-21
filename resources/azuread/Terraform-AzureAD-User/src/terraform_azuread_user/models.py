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
    AccountEnabled: Optional[bool]
    DisplayName: Optional[str]
    ForcePasswordChange: Optional[bool]
    ImmutableId: Optional[str]
    Mail: Optional[str]
    MailNickname: Optional[str]
    ObjectId: Optional[str]
    OnpremisesSamAccountName: Optional[str]
    OnpremisesUserPrincipalName: Optional[str]
    Password: Optional[str]
    UsageLocation: Optional[str]
    UserPrincipalName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountEnabled=json_data.get("AccountEnabled"),
            DisplayName=json_data.get("DisplayName"),
            ForcePasswordChange=json_data.get("ForcePasswordChange"),
            ImmutableId=json_data.get("ImmutableId"),
            Mail=json_data.get("Mail"),
            MailNickname=json_data.get("MailNickname"),
            ObjectId=json_data.get("ObjectId"),
            OnpremisesSamAccountName=json_data.get("OnpremisesSamAccountName"),
            OnpremisesUserPrincipalName=json_data.get("OnpremisesUserPrincipalName"),
            Password=json_data.get("Password"),
            UsageLocation=json_data.get("UsageLocation"),
            UserPrincipalName=json_data.get("UserPrincipalName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


