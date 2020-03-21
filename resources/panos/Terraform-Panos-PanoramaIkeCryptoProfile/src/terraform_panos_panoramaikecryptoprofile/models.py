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
    AuthenticationMultiple: Optional[float]
    Authentications: Optional[Sequence[str]]
    DhGroups: Optional[Sequence[str]]
    Encryptions: Optional[Sequence[str]]
    LifetimeType: Optional[str]
    LifetimeValue: Optional[float]
    Name: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthenticationMultiple=json_data.get("AuthenticationMultiple"),
            Authentications=json_data.get("Authentications"),
            DhGroups=json_data.get("DhGroups"),
            Encryptions=json_data.get("Encryptions"),
            LifetimeType=json_data.get("LifetimeType"),
            LifetimeValue=json_data.get("LifetimeValue"),
            Name=json_data.get("Name"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


