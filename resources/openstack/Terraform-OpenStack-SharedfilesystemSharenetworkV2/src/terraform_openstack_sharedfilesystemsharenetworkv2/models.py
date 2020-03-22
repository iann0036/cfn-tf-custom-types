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
    Cidr: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpVersion: Optional[float]
    Name: Optional[str]
    NetworkType: Optional[str]
    NeutronNetId: Optional[str]
    NeutronSubnetId: Optional[str]
    ProjectId: Optional[str]
    Region: Optional[str]
    SecurityServiceIds: Optional[Sequence[str]]
    SegmentationId: Optional[float]
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
            Cidr=json_data.get("Cidr"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpVersion=json_data.get("IpVersion"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            NeutronNetId=json_data.get("NeutronNetId"),
            NeutronSubnetId=json_data.get("NeutronSubnetId"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            SecurityServiceIds=json_data.get("SecurityServiceIds"),
            SegmentationId=json_data.get("SegmentationId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


