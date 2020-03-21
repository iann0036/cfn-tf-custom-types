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
    AllowedUses: Optional[Sequence[str]]
    CaCertPem: Optional[str]
    CaKeyAlgorithm: Optional[str]
    CaPrivateKeyPem: Optional[str]
    CertPem: Optional[str]
    CertRequestPem: Optional[str]
    EarlyRenewalHours: Optional[float]
    IsCaCertificate: Optional[bool]
    ReadyForRenewal: Optional[bool]
    SetSubjectKeyId: Optional[bool]
    ValidityEndTime: Optional[str]
    ValidityPeriodHours: Optional[float]
    ValidityStartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowedUses=json_data.get("AllowedUses"),
            CaCertPem=json_data.get("CaCertPem"),
            CaKeyAlgorithm=json_data.get("CaKeyAlgorithm"),
            CaPrivateKeyPem=json_data.get("CaPrivateKeyPem"),
            CertPem=json_data.get("CertPem"),
            CertRequestPem=json_data.get("CertRequestPem"),
            EarlyRenewalHours=json_data.get("EarlyRenewalHours"),
            IsCaCertificate=json_data.get("IsCaCertificate"),
            ReadyForRenewal=json_data.get("ReadyForRenewal"),
            SetSubjectKeyId=json_data.get("SetSubjectKeyId"),
            ValidityEndTime=json_data.get("ValidityEndTime"),
            ValidityPeriodHours=json_data.get("ValidityPeriodHours"),
            ValidityStartTime=json_data.get("ValidityStartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


