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
    Description: Optional[str]
    Name: Optional[str]
    Orchestration: Optional[str]
    ProjectTemplateId: Optional[str]
    Member: Optional[Sequence["_Member"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Orchestration=json_data.get("Orchestration"),
            ProjectTemplateId=json_data.get("ProjectTemplateId"),
            Member=json_data.get("Member"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Member:
    ExternalId: Optional[str]
    ExternalIdType: Optional[str]
    Role: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Member"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Member"]:
        if not json_data:
            return None
        return cls(
            ExternalId=json_data.get("ExternalId"),
            ExternalIdType=json_data.get("ExternalIdType"),
            Role=json_data.get("Role"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Member = Member


