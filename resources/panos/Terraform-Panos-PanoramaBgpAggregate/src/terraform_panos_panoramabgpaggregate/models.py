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
    AsPathLimit: Optional[float]
    AsPathType: Optional[str]
    AsPathValue: Optional[str]
    AsSet: Optional[bool]
    CommunityType: Optional[str]
    CommunityValue: Optional[str]
    Enable: Optional[bool]
    ExtendedCommunityType: Optional[str]
    ExtendedCommunityValue: Optional[str]
    LocalPreference: Optional[str]
    Med: Optional[str]
    Name: Optional[str]
    NextHop: Optional[str]
    Origin: Optional[str]
    Prefix: Optional[str]
    Summary: Optional[bool]
    Template: Optional[str]
    TemplateStack: Optional[str]
    VirtualRouter: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AsPathLimit=json_data.get("AsPathLimit"),
            AsPathType=json_data.get("AsPathType"),
            AsPathValue=json_data.get("AsPathValue"),
            AsSet=json_data.get("AsSet"),
            CommunityType=json_data.get("CommunityType"),
            CommunityValue=json_data.get("CommunityValue"),
            Enable=json_data.get("Enable"),
            ExtendedCommunityType=json_data.get("ExtendedCommunityType"),
            ExtendedCommunityValue=json_data.get("ExtendedCommunityValue"),
            LocalPreference=json_data.get("LocalPreference"),
            Med=json_data.get("Med"),
            Name=json_data.get("Name"),
            NextHop=json_data.get("NextHop"),
            Origin=json_data.get("Origin"),
            Prefix=json_data.get("Prefix"),
            Summary=json_data.get("Summary"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            VirtualRouter=json_data.get("VirtualRouter"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


