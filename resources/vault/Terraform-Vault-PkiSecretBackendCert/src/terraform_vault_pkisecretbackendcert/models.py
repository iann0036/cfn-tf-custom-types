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
    AltNames: Optional[Sequence[str]]
    AutoRenew: Optional[bool]
    Backend: Optional[str]
    CaChain: Optional[str]
    Certificate: Optional[str]
    CommonName: Optional[str]
    ExcludeCnFromSans: Optional[bool]
    Expiration: Optional[float]
    Format: Optional[str]
    IpSans: Optional[Sequence[str]]
    IssuingCa: Optional[str]
    MinSecondsRemaining: Optional[float]
    Name: Optional[str]
    OtherSans: Optional[Sequence[str]]
    PrivateKey: Optional[str]
    PrivateKeyFormat: Optional[str]
    PrivateKeyType: Optional[str]
    SerialNumber: Optional[str]
    Ttl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AltNames=json_data.get("AltNames"),
            AutoRenew=json_data.get("AutoRenew"),
            Backend=json_data.get("Backend"),
            CaChain=json_data.get("CaChain"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            ExcludeCnFromSans=json_data.get("ExcludeCnFromSans"),
            Expiration=json_data.get("Expiration"),
            Format=json_data.get("Format"),
            IpSans=json_data.get("IpSans"),
            IssuingCa=json_data.get("IssuingCa"),
            MinSecondsRemaining=json_data.get("MinSecondsRemaining"),
            Name=json_data.get("Name"),
            OtherSans=json_data.get("OtherSans"),
            PrivateKey=json_data.get("PrivateKey"),
            PrivateKeyFormat=json_data.get("PrivateKeyFormat"),
            PrivateKeyType=json_data.get("PrivateKeyType"),
            SerialNumber=json_data.get("SerialNumber"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


