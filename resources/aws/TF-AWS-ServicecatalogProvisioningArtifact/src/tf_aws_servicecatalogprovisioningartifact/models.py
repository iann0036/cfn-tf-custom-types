# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    AcceptLanguage: Optional[str]
    Active: Optional[bool]
    CreatedTime: Optional[str]
    Description: Optional[str]
    DisableTemplateValidation: Optional[bool]
    Guidance: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ProductId: Optional[str]
    TemplatePhysicalId: Optional[str]
    TemplateUrl: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AcceptLanguage=json_data.get("AcceptLanguage"),
            Active=json_data.get("Active"),
            CreatedTime=json_data.get("CreatedTime"),
            Description=json_data.get("Description"),
            DisableTemplateValidation=json_data.get("DisableTemplateValidation"),
            Guidance=json_data.get("Guidance"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProductId=json_data.get("ProductId"),
            TemplatePhysicalId=json_data.get("TemplatePhysicalId"),
            TemplateUrl=json_data.get("TemplateUrl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


