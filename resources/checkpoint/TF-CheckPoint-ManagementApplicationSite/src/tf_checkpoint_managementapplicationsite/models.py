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
    AdditionalCategories: Optional[Sequence[str]]
    ApplicationSignature: Optional[str]
    Color: Optional[str]
    Comments: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Name: Optional[str]
    PrimaryCategory: Optional[str]
    Tags: Optional[Sequence[str]]
    UrlList: Optional[Sequence[str]]
    UrlsDefinedAsRegularExpression: Optional[bool]

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
            AdditionalCategories=json_data.get("AdditionalCategories"),
            ApplicationSignature=json_data.get("ApplicationSignature"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Name=json_data.get("Name"),
            PrimaryCategory=json_data.get("PrimaryCategory"),
            Tags=json_data.get("Tags"),
            UrlList=json_data.get("UrlList"),
            UrlsDefinedAsRegularExpression=json_data.get("UrlsDefinedAsRegularExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


