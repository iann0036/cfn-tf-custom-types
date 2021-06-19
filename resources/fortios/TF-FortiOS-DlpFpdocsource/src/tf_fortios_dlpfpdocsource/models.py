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
    Date: Optional[float]
    FilePath: Optional[str]
    FilePattern: Optional[str]
    Id: Optional[str]
    KeepModified: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Period: Optional[str]
    RemoveDeleted: Optional[str]
    ScanOnCreation: Optional[str]
    ScanSubdirectories: Optional[str]
    Sensitivity: Optional[str]
    Server: Optional[str]
    ServerType: Optional[str]
    TodHour: Optional[float]
    TodMin: Optional[float]
    Username: Optional[str]
    Vdom: Optional[str]
    Vdomparam: Optional[str]
    Weekday: Optional[str]

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
            Date=json_data.get("Date"),
            FilePath=json_data.get("FilePath"),
            FilePattern=json_data.get("FilePattern"),
            Id=json_data.get("Id"),
            KeepModified=json_data.get("KeepModified"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Period=json_data.get("Period"),
            RemoveDeleted=json_data.get("RemoveDeleted"),
            ScanOnCreation=json_data.get("ScanOnCreation"),
            ScanSubdirectories=json_data.get("ScanSubdirectories"),
            Sensitivity=json_data.get("Sensitivity"),
            Server=json_data.get("Server"),
            ServerType=json_data.get("ServerType"),
            TodHour=json_data.get("TodHour"),
            TodMin=json_data.get("TodMin"),
            Username=json_data.get("Username"),
            Vdom=json_data.get("Vdom"),
            Vdomparam=json_data.get("Vdomparam"),
            Weekday=json_data.get("Weekday"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


