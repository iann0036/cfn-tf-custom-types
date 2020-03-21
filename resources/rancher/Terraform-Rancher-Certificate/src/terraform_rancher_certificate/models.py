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
    Cert: Optional[str]
    CertChain: Optional[str]
    CertFingerprint: Optional[str]
    Cn: Optional[str]
    Description: Optional[str]
    EnvironmentId: Optional[str]
    ExpiresAt: Optional[str]
    Id: Optional[str]
    IssuedAt: Optional[str]
    Issuer: Optional[str]
    Key: Optional[str]
    KeySize: Optional[str]
    Name: Optional[str]
    SerialNumber: Optional[str]
    SubjectAlternativeNames: Optional[Sequence[str]]
    Version: Optional[str]

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
            Cert=json_data.get("Cert"),
            CertChain=json_data.get("CertChain"),
            CertFingerprint=json_data.get("CertFingerprint"),
            Cn=json_data.get("Cn"),
            Description=json_data.get("Description"),
            EnvironmentId=json_data.get("EnvironmentId"),
            ExpiresAt=json_data.get("ExpiresAt"),
            Id=json_data.get("Id"),
            IssuedAt=json_data.get("IssuedAt"),
            Issuer=json_data.get("Issuer"),
            Key=json_data.get("Key"),
            KeySize=json_data.get("KeySize"),
            Name=json_data.get("Name"),
            SerialNumber=json_data.get("SerialNumber"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


