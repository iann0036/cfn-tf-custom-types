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
    Arn: Optional[str]
    AssumeRolePolicy: Optional[str]
    CreateDate: Optional[str]
    Description: Optional[str]
    ForceDetachPolicies: Optional[bool]
    Id: Optional[str]
    MaxSessionDuration: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Path: Optional[str]
    PermissionsBoundary: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    UniqueId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AssumeRolePolicy=json_data.get("AssumeRolePolicy"),
            CreateDate=json_data.get("CreateDate"),
            Description=json_data.get("Description"),
            ForceDetachPolicies=json_data.get("ForceDetachPolicies"),
            Id=json_data.get("Id"),
            MaxSessionDuration=json_data.get("MaxSessionDuration"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Path=json_data.get("Path"),
            PermissionsBoundary=json_data.get("PermissionsBoundary"),
            Tags=json_data.get("Tags"),
            UniqueId=json_data.get("UniqueId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


