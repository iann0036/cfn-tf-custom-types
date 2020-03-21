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
    CreateTime: Optional[str]
    DelegatedDomainName: Optional[str]
    Description: Optional[str]
    DomainRoles: Optional[Sequence[str]]
    Duration: Optional[str]
    ExpireTime: Optional[str]
    Name: Optional[str]
    Region: Optional[str]
    ProjectRole: Optional[Sequence["_ProjectRole"]]
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
            CreateTime=json_data.get("CreateTime"),
            DelegatedDomainName=json_data.get("DelegatedDomainName"),
            Description=json_data.get("Description"),
            DomainRoles=json_data.get("DomainRoles"),
            Duration=json_data.get("Duration"),
            ExpireTime=json_data.get("ExpireTime"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            ProjectRole=json_data.get("ProjectRole"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProjectRole:
    Project: Optional[str]
    Roles: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectRole"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectRole"]:
        if not json_data:
            return None
        return cls(
            Project=json_data.get("Project"),
            Roles=json_data.get("Roles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectRole = ProjectRole


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


