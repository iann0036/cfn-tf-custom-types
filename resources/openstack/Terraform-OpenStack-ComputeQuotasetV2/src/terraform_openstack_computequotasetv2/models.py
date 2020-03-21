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
    Cores: Optional[float]
    FixedIps: Optional[float]
    FloatingIps: Optional[float]
    Id: Optional[str]
    InjectedFileContentBytes: Optional[float]
    InjectedFilePathBytes: Optional[float]
    InjectedFiles: Optional[float]
    Instances: Optional[float]
    KeyPairs: Optional[float]
    MetadataItems: Optional[float]
    ProjectId: Optional[str]
    Ram: Optional[float]
    Region: Optional[str]
    SecurityGroupRules: Optional[float]
    SecurityGroups: Optional[float]
    ServerGroupMembers: Optional[float]
    ServerGroups: Optional[float]
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
            Cores=json_data.get("Cores"),
            FixedIps=json_data.get("FixedIps"),
            FloatingIps=json_data.get("FloatingIps"),
            Id=json_data.get("Id"),
            InjectedFileContentBytes=json_data.get("InjectedFileContentBytes"),
            InjectedFilePathBytes=json_data.get("InjectedFilePathBytes"),
            InjectedFiles=json_data.get("InjectedFiles"),
            Instances=json_data.get("Instances"),
            KeyPairs=json_data.get("KeyPairs"),
            MetadataItems=json_data.get("MetadataItems"),
            ProjectId=json_data.get("ProjectId"),
            Ram=json_data.get("Ram"),
            Region=json_data.get("Region"),
            SecurityGroupRules=json_data.get("SecurityGroupRules"),
            SecurityGroups=json_data.get("SecurityGroups"),
            ServerGroupMembers=json_data.get("ServerGroupMembers"),
            ServerGroups=json_data.get("ServerGroups"),
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


