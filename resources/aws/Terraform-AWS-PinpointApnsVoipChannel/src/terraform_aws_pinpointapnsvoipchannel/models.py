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
    ApplicationId: Optional[str]
    BundleId: Optional[str]
    Certificate: Optional[str]
    DefaultAuthenticationMethod: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    PrivateKey: Optional[str]
    TeamId: Optional[str]
    TokenKey: Optional[str]
    TokenKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationId=json_data.get("ApplicationId"),
            BundleId=json_data.get("BundleId"),
            Certificate=json_data.get("Certificate"),
            DefaultAuthenticationMethod=json_data.get("DefaultAuthenticationMethod"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            PrivateKey=json_data.get("PrivateKey"),
            TeamId=json_data.get("TeamId"),
            TokenKey=json_data.get("TokenKey"),
            TokenKeyId=json_data.get("TokenKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


