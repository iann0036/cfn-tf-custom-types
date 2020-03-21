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
    BeginTime: Optional[str]
    Cert: Optional[str]
    CreateTime: Optional[str]
    Domain: Optional[str]
    EndTime: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    ProductZhName: Optional[str]
    ProjectId: Optional[float]
    Status: Optional[float]
    SubjectNames: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BeginTime=json_data.get("BeginTime"),
            Cert=json_data.get("Cert"),
            CreateTime=json_data.get("CreateTime"),
            Domain=json_data.get("Domain"),
            EndTime=json_data.get("EndTime"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            ProductZhName=json_data.get("ProductZhName"),
            ProjectId=json_data.get("ProjectId"),
            Status=json_data.get("Status"),
            SubjectNames=json_data.get("SubjectNames"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


