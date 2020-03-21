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
    AllowPlaintextBackup: Optional[bool]
    Backend: Optional[str]
    ConvergentEncryption: Optional[bool]
    DeletionAllowed: Optional[bool]
    Derived: Optional[bool]
    Exportable: Optional[bool]
    Id: Optional[str]
    Keys: Optional[Sequence[Sequence["_Keys"]]]
    LatestVersion: Optional[float]
    MinAvailableVersion: Optional[float]
    MinDecryptionVersion: Optional[float]
    MinEncryptionVersion: Optional[float]
    Name: Optional[str]
    SupportsDecryption: Optional[bool]
    SupportsDerivation: Optional[bool]
    SupportsEncryption: Optional[bool]
    SupportsSigning: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowPlaintextBackup=json_data.get("AllowPlaintextBackup"),
            Backend=json_data.get("Backend"),
            ConvergentEncryption=json_data.get("ConvergentEncryption"),
            DeletionAllowed=json_data.get("DeletionAllowed"),
            Derived=json_data.get("Derived"),
            Exportable=json_data.get("Exportable"),
            Id=json_data.get("Id"),
            Keys=json_data.get("Keys"),
            LatestVersion=json_data.get("LatestVersion"),
            MinAvailableVersion=json_data.get("MinAvailableVersion"),
            MinDecryptionVersion=json_data.get("MinDecryptionVersion"),
            MinEncryptionVersion=json_data.get("MinEncryptionVersion"),
            Name=json_data.get("Name"),
            SupportsDecryption=json_data.get("SupportsDecryption"),
            SupportsDerivation=json_data.get("SupportsDerivation"),
            SupportsEncryption=json_data.get("SupportsEncryption"),
            SupportsSigning=json_data.get("SupportsSigning"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Keys:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Keys"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Keys"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Keys = Keys


