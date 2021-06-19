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
    ApiCredentialPassword: Optional[str]
    ApiCredentialType: Optional[str]
    Data: Optional[str]
    ExpiryDays: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    VirtualK8sName: Optional[str]
    VirtualK8sNamespace: Optional[str]

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
            ApiCredentialPassword=json_data.get("ApiCredentialPassword"),
            ApiCredentialType=json_data.get("ApiCredentialType"),
            Data=json_data.get("Data"),
            ExpiryDays=json_data.get("ExpiryDays"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            VirtualK8sName=json_data.get("VirtualK8sName"),
            VirtualK8sNamespace=json_data.get("VirtualK8sNamespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


