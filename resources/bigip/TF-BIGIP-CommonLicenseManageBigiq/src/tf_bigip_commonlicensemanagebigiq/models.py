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
    AssignmentType: Optional[str]
    BigiqAddress: Optional[str]
    BigiqLoginRef: Optional[str]
    BigiqPassword: Optional[str]
    BigiqPort: Optional[str]
    BigiqTokenAuth: Optional[bool]
    BigiqUser: Optional[str]
    DeviceLicenseStatus: Optional[str]
    Hypervisor: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    LicensePoolname: Optional[str]
    MacAddress: Optional[str]
    Skukeyword1: Optional[str]
    Skukeyword2: Optional[str]
    Tenant: Optional[str]
    UnitOfMeasure: Optional[str]

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
            AssignmentType=json_data.get("AssignmentType"),
            BigiqAddress=json_data.get("BigiqAddress"),
            BigiqLoginRef=json_data.get("BigiqLoginRef"),
            BigiqPassword=json_data.get("BigiqPassword"),
            BigiqPort=json_data.get("BigiqPort"),
            BigiqTokenAuth=json_data.get("BigiqTokenAuth"),
            BigiqUser=json_data.get("BigiqUser"),
            DeviceLicenseStatus=json_data.get("DeviceLicenseStatus"),
            Hypervisor=json_data.get("Hypervisor"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            LicensePoolname=json_data.get("LicensePoolname"),
            MacAddress=json_data.get("MacAddress"),
            Skukeyword1=json_data.get("Skukeyword1"),
            Skukeyword2=json_data.get("Skukeyword2"),
            Tenant=json_data.get("Tenant"),
            UnitOfMeasure=json_data.get("UnitOfMeasure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


