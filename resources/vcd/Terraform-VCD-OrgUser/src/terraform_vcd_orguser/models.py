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
    DeployedVmQuota: Optional[float]
    Description: Optional[str]
    EmailAddress: Optional[str]
    Enabled: Optional[bool]
    FullName: Optional[str]
    InstantMessaging: Optional[str]
    IsGroupRole: Optional[bool]
    IsLocked: Optional[bool]
    Name: Optional[str]
    Org: Optional[str]
    Password: Optional[str]
    PasswordFile: Optional[str]
    ProviderType: Optional[str]
    Role: Optional[str]
    StoredVmQuota: Optional[float]
    TakeOwnership: Optional[bool]
    Telephone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeployedVmQuota=json_data.get("DeployedVmQuota"),
            Description=json_data.get("Description"),
            EmailAddress=json_data.get("EmailAddress"),
            Enabled=json_data.get("Enabled"),
            FullName=json_data.get("FullName"),
            InstantMessaging=json_data.get("InstantMessaging"),
            IsGroupRole=json_data.get("IsGroupRole"),
            IsLocked=json_data.get("IsLocked"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            Password=json_data.get("Password"),
            PasswordFile=json_data.get("PasswordFile"),
            ProviderType=json_data.get("ProviderType"),
            Role=json_data.get("Role"),
            StoredVmQuota=json_data.get("StoredVmQuota"),
            TakeOwnership=json_data.get("TakeOwnership"),
            Telephone=json_data.get("Telephone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


