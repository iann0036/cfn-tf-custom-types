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
    Caname: Optional[str]
    HostTrustedChecking: Optional[str]
    HostkeyDsa1024: Optional[str]
    HostkeyEcdsa256: Optional[str]
    HostkeyEcdsa384: Optional[str]
    HostkeyEcdsa521: Optional[str]
    HostkeyEd25519: Optional[str]
    HostkeyRsa2048: Optional[str]
    Id: Optional[str]
    UntrustedCaname: Optional[str]
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
            Caname=json_data.get("Caname"),
            HostTrustedChecking=json_data.get("HostTrustedChecking"),
            HostkeyDsa1024=json_data.get("HostkeyDsa1024"),
            HostkeyEcdsa256=json_data.get("HostkeyEcdsa256"),
            HostkeyEcdsa384=json_data.get("HostkeyEcdsa384"),
            HostkeyEcdsa521=json_data.get("HostkeyEcdsa521"),
            HostkeyEd25519=json_data.get("HostkeyEd25519"),
            HostkeyRsa2048=json_data.get("HostkeyRsa2048"),
            Id=json_data.get("Id"),
            UntrustedCaname=json_data.get("UntrustedCaname"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


