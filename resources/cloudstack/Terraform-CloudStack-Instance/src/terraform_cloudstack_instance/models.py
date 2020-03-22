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
    AffinityGroupIds: Optional[Sequence[str]]
    AffinityGroupNames: Optional[Sequence[str]]
    DisplayName: Optional[str]
    Expunge: Optional[bool]
    Group: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    Keypair: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    Project: Optional[str]
    RootDiskSize: Optional[float]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityGroupNames: Optional[Sequence[str]]
    ServiceOffering: Optional[str]
    StartVm: Optional[bool]
    Template: Optional[str]
    UserData: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AffinityGroupIds=json_data.get("AffinityGroupIds"),
            AffinityGroupNames=json_data.get("AffinityGroupNames"),
            DisplayName=json_data.get("DisplayName"),
            Expunge=json_data.get("Expunge"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            Keypair=json_data.get("Keypair"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            Project=json_data.get("Project"),
            RootDiskSize=json_data.get("RootDiskSize"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityGroupNames=json_data.get("SecurityGroupNames"),
            ServiceOffering=json_data.get("ServiceOffering"),
            StartVm=json_data.get("StartVm"),
            Template=json_data.get("Template"),
            UserData=json_data.get("UserData"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


