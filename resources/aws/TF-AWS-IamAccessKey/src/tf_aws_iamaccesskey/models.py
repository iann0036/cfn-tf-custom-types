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
    CreateDate: Optional[str]
    EncryptedSecret: Optional[str]
    Id: Optional[str]
    KeyFingerprint: Optional[str]
    PgpKey: Optional[str]
    Secret: Optional[str]
    SesSmtpPasswordV4: Optional[str]
    Status: Optional[str]
    User: Optional[str]

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
            CreateDate=json_data.get("CreateDate"),
            EncryptedSecret=json_data.get("EncryptedSecret"),
            Id=json_data.get("Id"),
            KeyFingerprint=json_data.get("KeyFingerprint"),
            PgpKey=json_data.get("PgpKey"),
            Secret=json_data.get("Secret"),
            SesSmtpPasswordV4=json_data.get("SesSmtpPasswordV4"),
            Status=json_data.get("Status"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


