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
    BackendTransfer: Optional[bool]
    Created: Optional[str]
    Name: Optional[str]
    OrganizationId: Optional[str]
    PaymentMethodId: Optional[str]
    Updated: Optional[str]
    BgpConfig: Optional[Sequence["_BgpConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BackendTransfer=json_data.get("BackendTransfer"),
            Created=json_data.get("Created"),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            PaymentMethodId=json_data.get("PaymentMethodId"),
            Updated=json_data.get("Updated"),
            BgpConfig=json_data.get("BgpConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BgpConfig:
    Asn: Optional[float]
    DeploymentType: Optional[str]
    Md5: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpConfig"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            DeploymentType=json_data.get("DeploymentType"),
            Md5=json_data.get("Md5"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpConfig = BgpConfig


