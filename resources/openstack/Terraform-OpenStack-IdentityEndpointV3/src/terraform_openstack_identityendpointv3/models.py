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
    EndpointRegion: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    ServiceId: Optional[str]
    ServiceName: Optional[str]
    ServiceType: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EndpointRegion=json_data.get("EndpointRegion"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            ServiceId=json_data.get("ServiceId"),
            ServiceName=json_data.get("ServiceName"),
            ServiceType=json_data.get("ServiceType"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


