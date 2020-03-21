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
    FullName: Optional[str]
    FullPath: Optional[str]
    LfsEnabled: Optional[bool]
    Name: Optional[str]
    ParentId: Optional[float]
    Path: Optional[str]
    RequestAccessEnabled: Optional[bool]
    RunnersToken: Optional[str]
    VisibilityLevel: Optional[str]
    WebUrl: Optional[str]

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
            FullName=json_data.get("FullName"),
            FullPath=json_data.get("FullPath"),
            LfsEnabled=json_data.get("LfsEnabled"),
            Name=json_data.get("Name"),
            ParentId=json_data.get("ParentId"),
            Path=json_data.get("Path"),
            RequestAccessEnabled=json_data.get("RequestAccessEnabled"),
            RunnersToken=json_data.get("RunnersToken"),
            VisibilityLevel=json_data.get("VisibilityLevel"),
            WebUrl=json_data.get("WebUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


