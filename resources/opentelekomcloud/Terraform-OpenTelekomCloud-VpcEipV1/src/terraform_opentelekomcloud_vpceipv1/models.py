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
    Region: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    Bandwidth: Optional[Sequence["_Bandwidth"]]
    Publicip: Optional[Sequence["_Publicip"]]
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
            Region=json_data.get("Region"),
            ValueSpecs=json_data.get("ValueSpecs"),
            Bandwidth=json_data.get("Bandwidth"),
            Publicip=json_data.get("Publicip"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValueSpecs:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class Bandwidth:
    ChargeMode: Optional[str]
    Name: Optional[str]
    ShareType: Optional[str]
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Bandwidth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bandwidth"]:
        if not json_data:
            return None
        return cls(
            ChargeMode=json_data.get("ChargeMode"),
            Name=json_data.get("Name"),
            ShareType=json_data.get("ShareType"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Bandwidth = Bandwidth


@dataclass
class Publicip:
    IpAddress: Optional[str]
    PortId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Publicip"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Publicip"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            PortId=json_data.get("PortId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Publicip = Publicip


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


