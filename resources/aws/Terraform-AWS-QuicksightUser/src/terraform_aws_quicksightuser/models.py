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
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    Email: Optional[str]
    IamArn: Optional[str]
    Id: Optional[str]
    IdentityType: Optional[str]
    Namespace: Optional[str]
    SessionName: Optional[str]
    UserName: Optional[str]
    UserRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            Email=json_data.get("Email"),
            IamArn=json_data.get("IamArn"),
            Id=json_data.get("Id"),
            IdentityType=json_data.get("IdentityType"),
            Namespace=json_data.get("Namespace"),
            SessionName=json_data.get("SessionName"),
            UserName=json_data.get("UserName"),
            UserRole=json_data.get("UserRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


