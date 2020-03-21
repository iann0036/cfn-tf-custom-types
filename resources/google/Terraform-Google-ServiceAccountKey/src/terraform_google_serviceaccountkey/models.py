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
    KeyAlgorithm: Optional[str]
    Name: Optional[str]
    PgpKey: Optional[str]
    PrivateKey: Optional[str]
    PrivateKeyEncrypted: Optional[str]
    PrivateKeyFingerprint: Optional[str]
    PrivateKeyType: Optional[str]
    PublicKey: Optional[str]
    PublicKeyType: Optional[str]
    ServiceAccountId: Optional[str]
    ValidAfter: Optional[str]
    ValidBefore: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            KeyAlgorithm=json_data.get("KeyAlgorithm"),
            Name=json_data.get("Name"),
            PgpKey=json_data.get("PgpKey"),
            PrivateKey=json_data.get("PrivateKey"),
            PrivateKeyEncrypted=json_data.get("PrivateKeyEncrypted"),
            PrivateKeyFingerprint=json_data.get("PrivateKeyFingerprint"),
            PrivateKeyType=json_data.get("PrivateKeyType"),
            PublicKey=json_data.get("PublicKey"),
            PublicKeyType=json_data.get("PublicKeyType"),
            ServiceAccountId=json_data.get("ServiceAccountId"),
            ValidAfter=json_data.get("ValidAfter"),
            ValidBefore=json_data.get("ValidBefore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


