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
    AuthAlgorithm: Optional[str]
    Description: Optional[str]
    EncapsulationMode: Optional[str]
    EncryptionAlgorithm: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Pfs: Optional[str]
    Region: Optional[str]
    TenantId: Optional[str]
    TransformProtocol: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    Lifetime: Optional[Sequence["_Lifetime"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthAlgorithm=json_data.get("AuthAlgorithm"),
            Description=json_data.get("Description"),
            EncapsulationMode=json_data.get("EncapsulationMode"),
            EncryptionAlgorithm=json_data.get("EncryptionAlgorithm"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Pfs=json_data.get("Pfs"),
            Region=json_data.get("Region"),
            TenantId=json_data.get("TenantId"),
            TransformProtocol=json_data.get("TransformProtocol"),
            ValueSpecs=json_data.get("ValueSpecs"),
            Lifetime=json_data.get("Lifetime"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValueSpecs:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class Lifetime:
    Units: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Lifetime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lifetime"]:
        if not json_data:
            return None
        return cls(
            Units=json_data.get("Units"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lifetime = Lifetime


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


