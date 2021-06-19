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
    Certificate: Optional[str]
    DynamicSortSubtable: Optional[str]
    EncAlgorithm: Optional[str]
    Facility: Optional[str]
    Format: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    MaxLogRate: Optional[float]
    Mode: Optional[str]
    Port: Optional[float]
    Priority: Optional[str]
    Server: Optional[str]
    SourceIp: Optional[str]
    SslMinProtoVersion: Optional[str]
    Status: Optional[str]
    SyslogType: Optional[float]
    Vdomparam: Optional[str]
    CustomFieldName: Optional[Sequence["_CustomFieldNameDefinition"]]

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
            Certificate=json_data.get("Certificate"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EncAlgorithm=json_data.get("EncAlgorithm"),
            Facility=json_data.get("Facility"),
            Format=json_data.get("Format"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            MaxLogRate=json_data.get("MaxLogRate"),
            Mode=json_data.get("Mode"),
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Server=json_data.get("Server"),
            SourceIp=json_data.get("SourceIp"),
            SslMinProtoVersion=json_data.get("SslMinProtoVersion"),
            Status=json_data.get("Status"),
            SyslogType=json_data.get("SyslogType"),
            Vdomparam=json_data.get("Vdomparam"),
            CustomFieldName=deserialize_list(json_data.get("CustomFieldName"), CustomFieldNameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomFieldNameDefinition(BaseModel):
    Custom: Optional[str]
    Id: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomFieldNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomFieldNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Custom=json_data.get("Custom"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomFieldNameDefinition = CustomFieldNameDefinition


