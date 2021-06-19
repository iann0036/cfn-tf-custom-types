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
    All: Optional[float]
    ControlCpuHigh: Optional[float]
    DataCpuHigh: Optional[float]
    Fan: Optional[float]
    FileSysReadOnly: Optional[float]
    HighDiskUse: Optional[float]
    HighMemoryUse: Optional[float]
    HighTemp: Optional[float]
    Id: Optional[str]
    LicenseManagement: Optional[float]
    LowTemp: Optional[float]
    PacketDrop: Optional[float]
    Power: Optional[float]
    PriDisk: Optional[float]
    Restart: Optional[float]
    SecDisk: Optional[float]
    Shutdown: Optional[float]
    SmpResourceEvent: Optional[float]
    Start: Optional[float]
    SyslogSeverityOne: Optional[float]
    TacacsServerUpDown: Optional[float]
    Uuid: Optional[str]

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
            All=json_data.get("All"),
            ControlCpuHigh=json_data.get("ControlCpuHigh"),
            DataCpuHigh=json_data.get("DataCpuHigh"),
            Fan=json_data.get("Fan"),
            FileSysReadOnly=json_data.get("FileSysReadOnly"),
            HighDiskUse=json_data.get("HighDiskUse"),
            HighMemoryUse=json_data.get("HighMemoryUse"),
            HighTemp=json_data.get("HighTemp"),
            Id=json_data.get("Id"),
            LicenseManagement=json_data.get("LicenseManagement"),
            LowTemp=json_data.get("LowTemp"),
            PacketDrop=json_data.get("PacketDrop"),
            Power=json_data.get("Power"),
            PriDisk=json_data.get("PriDisk"),
            Restart=json_data.get("Restart"),
            SecDisk=json_data.get("SecDisk"),
            Shutdown=json_data.get("Shutdown"),
            SmpResourceEvent=json_data.get("SmpResourceEvent"),
            Start=json_data.get("Start"),
            SyslogSeverityOne=json_data.get("SyslogSeverityOne"),
            TacacsServerUpDown=json_data.get("TacacsServerUpDown"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


