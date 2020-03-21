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
    Action: Optional[str]
    Description: Optional[str]
    DestinationIpAddress: Optional[str]
    DestinationPort: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IpVersion: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]
    Region: Optional[str]
    SourceIpAddress: Optional[str]
    SourcePort: Optional[str]
    TenantId: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            DestinationIpAddress=json_data.get("DestinationIpAddress"),
            DestinationPort=json_data.get("DestinationPort"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IpVersion=json_data.get("IpVersion"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            Region=json_data.get("Region"),
            SourceIpAddress=json_data.get("SourceIpAddress"),
            SourcePort=json_data.get("SourcePort"),
            TenantId=json_data.get("TenantId"),
            ValueSpecs=json_data.get("ValueSpecs"),
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


