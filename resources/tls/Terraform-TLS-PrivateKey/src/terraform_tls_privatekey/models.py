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
    EcdsaCurve: Optional[str]
    Id: Optional[str]
    PrivateKeyPem: Optional[str]
    PublicKeyFingerprintMd5: Optional[str]
    PublicKeyOpenssh: Optional[str]
    PublicKeyPem: Optional[str]
    RsaBits: Optional[float]

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
            EcdsaCurve=json_data.get("EcdsaCurve"),
            Id=json_data.get("Id"),
            PrivateKeyPem=json_data.get("PrivateKeyPem"),
            PublicKeyFingerprintMd5=json_data.get("PublicKeyFingerprintMd5"),
            PublicKeyOpenssh=json_data.get("PublicKeyOpenssh"),
            PublicKeyPem=json_data.get("PublicKeyPem"),
            RsaBits=json_data.get("RsaBits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


