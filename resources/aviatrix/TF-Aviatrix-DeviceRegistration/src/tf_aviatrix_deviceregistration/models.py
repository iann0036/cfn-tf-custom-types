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
    Address1: Optional[str]
    Address2: Optional[str]
    City: Optional[str]
    Country: Optional[str]
    Description: Optional[str]
    HostOs: Optional[str]
    Id: Optional[str]
    KeyFile: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PublicIp: Optional[str]
    SshPort: Optional[float]
    State: Optional[str]
    Username: Optional[str]
    ZipCode: Optional[str]

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
            Address1=json_data.get("Address1"),
            Address2=json_data.get("Address2"),
            City=json_data.get("City"),
            Country=json_data.get("Country"),
            Description=json_data.get("Description"),
            HostOs=json_data.get("HostOs"),
            Id=json_data.get("Id"),
            KeyFile=json_data.get("KeyFile"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PublicIp=json_data.get("PublicIp"),
            SshPort=json_data.get("SshPort"),
            State=json_data.get("State"),
            Username=json_data.get("Username"),
            ZipCode=json_data.get("ZipCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


