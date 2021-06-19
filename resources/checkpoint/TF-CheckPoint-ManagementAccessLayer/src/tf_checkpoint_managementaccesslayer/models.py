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
    AddDefaultRule: Optional[bool]
    ApplicationsAndUrlFiltering: Optional[bool]
    Color: Optional[str]
    Comments: Optional[str]
    ContentAwareness: Optional[bool]
    DetectUsingXForwardFor: Optional[bool]
    Firewall: Optional[bool]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    ImplicitCleanupAction: Optional[str]
    MobileAccess: Optional[bool]
    Name: Optional[str]
    Shared: Optional[bool]
    Tags: Optional[Sequence[str]]

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
            AddDefaultRule=json_data.get("AddDefaultRule"),
            ApplicationsAndUrlFiltering=json_data.get("ApplicationsAndUrlFiltering"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            ContentAwareness=json_data.get("ContentAwareness"),
            DetectUsingXForwardFor=json_data.get("DetectUsingXForwardFor"),
            Firewall=json_data.get("Firewall"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            ImplicitCleanupAction=json_data.get("ImplicitCleanupAction"),
            MobileAccess=json_data.get("MobileAccess"),
            Name=json_data.get("Name"),
            Shared=json_data.get("Shared"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


