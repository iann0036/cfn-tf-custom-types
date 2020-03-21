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
    Bucket: Optional[str]
    Domain: Optional[str]
    Email: Optional[str]
    Entity: Optional[str]
    EntityId: Optional[str]
    Generation: Optional[float]
    Id: Optional[str]
    Object: Optional[str]
    ProjectTeam: Optional[Sequence["_ProjectTeam"]]
    Role: Optional[str]
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
            Bucket=json_data.get("Bucket"),
            Domain=json_data.get("Domain"),
            Email=json_data.get("Email"),
            Entity=json_data.get("Entity"),
            EntityId=json_data.get("EntityId"),
            Generation=json_data.get("Generation"),
            Id=json_data.get("Id"),
            Object=json_data.get("Object"),
            ProjectTeam=json_data.get("ProjectTeam"),
            Role=json_data.get("Role"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProjectTeam:
    ProjectNumber: Optional[str]
    Team: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectTeam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectTeam"]:
        if not json_data:
            return None
        return cls(
            ProjectNumber=json_data.get("ProjectNumber"),
            Team=json_data.get("Team"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectTeam = ProjectTeam


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


