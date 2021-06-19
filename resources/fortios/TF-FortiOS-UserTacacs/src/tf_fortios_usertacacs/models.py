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
    AuthenType: Optional[str]
    Authorization: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    SecondaryKey: Optional[str]
    SecondaryServer: Optional[str]
    Server: Optional[str]
    SourceIp: Optional[str]
    TertiaryKey: Optional[str]
    TertiaryServer: Optional[str]
    Vdomparam: Optional[str]

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
            AuthenType=json_data.get("AuthenType"),
            Authorization=json_data.get("Authorization"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SecondaryKey=json_data.get("SecondaryKey"),
            SecondaryServer=json_data.get("SecondaryServer"),
            Server=json_data.get("Server"),
            SourceIp=json_data.get("SourceIp"),
            TertiaryKey=json_data.get("TertiaryKey"),
            TertiaryServer=json_data.get("TertiaryServer"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


