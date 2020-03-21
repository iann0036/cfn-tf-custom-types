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
    Algorithm: Optional[str]
    CertificateId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpAddressId: Optional[str]
    MemberIds: Optional[Sequence[str]]
    Name: Optional[str]
    NetworkId: Optional[str]
    PrivatePort: Optional[float]
    Project: Optional[str]
    Protocol: Optional[str]
    PublicPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Algorithm=json_data.get("Algorithm"),
            CertificateId=json_data.get("CertificateId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpAddressId=json_data.get("IpAddressId"),
            MemberIds=json_data.get("MemberIds"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            PrivatePort=json_data.get("PrivatePort"),
            Project=json_data.get("Project"),
            Protocol=json_data.get("Protocol"),
            PublicPort=json_data.get("PublicPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


