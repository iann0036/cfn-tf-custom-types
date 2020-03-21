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
    Content: Optional[str]
    ContentBase64: Optional[str]
    DirectoryPermission: Optional[str]
    FilePermission: Optional[str]
    Filename: Optional[str]
    SensitiveContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Content=json_data.get("Content"),
            ContentBase64=json_data.get("ContentBase64"),
            DirectoryPermission=json_data.get("DirectoryPermission"),
            FilePermission=json_data.get("FilePermission"),
            Filename=json_data.get("Filename"),
            SensitiveContent=json_data.get("SensitiveContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


