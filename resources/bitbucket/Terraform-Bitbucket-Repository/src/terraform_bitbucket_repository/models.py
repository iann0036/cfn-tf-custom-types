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
    CloneHttps: Optional[str]
    CloneSsh: Optional[str]
    Description: Optional[str]
    ForkPolicy: Optional[str]
    HasIssues: Optional[bool]
    HasWiki: Optional[bool]
    Id: Optional[str]
    IsPrivate: Optional[bool]
    Language: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    PipelinesEnabled: Optional[bool]
    ProjectKey: Optional[str]
    Scm: Optional[str]
    Slug: Optional[str]
    Website: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CloneHttps=json_data.get("CloneHttps"),
            CloneSsh=json_data.get("CloneSsh"),
            Description=json_data.get("Description"),
            ForkPolicy=json_data.get("ForkPolicy"),
            HasIssues=json_data.get("HasIssues"),
            HasWiki=json_data.get("HasWiki"),
            Id=json_data.get("Id"),
            IsPrivate=json_data.get("IsPrivate"),
            Language=json_data.get("Language"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            PipelinesEnabled=json_data.get("PipelinesEnabled"),
            ProjectKey=json_data.get("ProjectKey"),
            Scm=json_data.get("Scm"),
            Slug=json_data.get("Slug"),
            Website=json_data.get("Website"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


