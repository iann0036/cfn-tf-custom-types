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
    Checksum: Optional[str]
    Compressed: Optional[bool]
    Created: Optional[str]
    Description: Optional[str]
    ExpiresAt: Optional[str]
    Id: Optional[str]
    IsFederated: Optional[bool]
    Name: Optional[str]
    Path: Optional[str]
    ReadOnly: Optional[bool]
    RestrictDownload: Optional[bool]
    Size: Optional[float]
    TenantRef: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Version: Optional[str]

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
            Checksum=json_data.get("Checksum"),
            Compressed=json_data.get("Compressed"),
            Created=json_data.get("Created"),
            Description=json_data.get("Description"),
            ExpiresAt=json_data.get("ExpiresAt"),
            Id=json_data.get("Id"),
            IsFederated=json_data.get("IsFederated"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            RestrictDownload=json_data.get("RestrictDownload"),
            Size=json_data.get("Size"),
            TenantRef=json_data.get("TenantRef"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


