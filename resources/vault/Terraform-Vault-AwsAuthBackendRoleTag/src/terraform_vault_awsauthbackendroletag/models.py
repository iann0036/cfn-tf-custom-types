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
    AllowInstanceMigration: Optional[bool]
    Backend: Optional[str]
    DisallowReauthentication: Optional[bool]
    InstanceId: Optional[str]
    MaxTtl: Optional[str]
    Policies: Optional[Sequence[str]]
    Role: Optional[str]
    TagKey: Optional[str]
    TagValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowInstanceMigration=json_data.get("AllowInstanceMigration"),
            Backend=json_data.get("Backend"),
            DisallowReauthentication=json_data.get("DisallowReauthentication"),
            InstanceId=json_data.get("InstanceId"),
            MaxTtl=json_data.get("MaxTtl"),
            Policies=json_data.get("Policies"),
            Role=json_data.get("Role"),
            TagKey=json_data.get("TagKey"),
            TagValue=json_data.get("TagValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


