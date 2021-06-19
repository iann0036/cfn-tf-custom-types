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
    AutoAddNewNodes: Optional[str]
    DbClusterId: Optional[str]
    EndpointConfig: Optional[Sequence["_EndpointConfigDefinition"]]
    EndpointType: Optional[str]
    Id: Optional[str]
    NetType: Optional[str]
    Nodes: Optional[Sequence[str]]
    ReadWriteMode: Optional[str]
    SslConnectionString: Optional[str]
    SslEnabled: Optional[str]
    SslExpireTime: Optional[str]

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
            AutoAddNewNodes=json_data.get("AutoAddNewNodes"),
            DbClusterId=json_data.get("DbClusterId"),
            EndpointConfig=deserialize_list(json_data.get("EndpointConfig"), EndpointConfigDefinition),
            EndpointType=json_data.get("EndpointType"),
            Id=json_data.get("Id"),
            NetType=json_data.get("NetType"),
            Nodes=json_data.get("Nodes"),
            ReadWriteMode=json_data.get("ReadWriteMode"),
            SslConnectionString=json_data.get("SslConnectionString"),
            SslEnabled=json_data.get("SslEnabled"),
            SslExpireTime=json_data.get("SslExpireTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigDefinition = EndpointConfigDefinition


