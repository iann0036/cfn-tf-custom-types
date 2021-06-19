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
    CheckSites: Optional[Sequence[float]]
    ExpectedStatusCode: Optional[float]
    Fqdn: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Interval: Optional[str]
    IntervalPolicy: Optional[str]
    IpVersion: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Port: Optional[float]
    ProtocolType: Optional[str]
    SearchString: Optional[str]
    VerificationPolicy: Optional[str]

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
            CheckSites=json_data.get("CheckSites"),
            ExpectedStatusCode=json_data.get("ExpectedStatusCode"),
            Fqdn=json_data.get("Fqdn"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            IntervalPolicy=json_data.get("IntervalPolicy"),
            IpVersion=json_data.get("IpVersion"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            ProtocolType=json_data.get("ProtocolType"),
            SearchString=json_data.get("SearchString"),
            VerificationPolicy=json_data.get("VerificationPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


