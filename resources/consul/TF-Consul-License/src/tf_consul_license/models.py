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
    CustomerId: Optional[str]
    Datacenter: Optional[str]
    ExpirationTime: Optional[str]
    Features: Optional[Sequence[str]]
    Id: Optional[str]
    InstallationId: Optional[str]
    IssueTime: Optional[str]
    License: Optional[str]
    LicenseId: Optional[str]
    Product: Optional[str]
    StartTime: Optional[str]
    Valid: Optional[bool]
    Warnings: Optional[Sequence[str]]

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
            CustomerId=json_data.get("CustomerId"),
            Datacenter=json_data.get("Datacenter"),
            ExpirationTime=json_data.get("ExpirationTime"),
            Features=json_data.get("Features"),
            Id=json_data.get("Id"),
            InstallationId=json_data.get("InstallationId"),
            IssueTime=json_data.get("IssueTime"),
            License=json_data.get("License"),
            LicenseId=json_data.get("LicenseId"),
            Product=json_data.get("Product"),
            StartTime=json_data.get("StartTime"),
            Valid=json_data.get("Valid"),
            Warnings=json_data.get("Warnings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


