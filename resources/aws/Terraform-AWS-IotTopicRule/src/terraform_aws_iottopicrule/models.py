# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Sql: Optional[str]
    SqlVersion: Optional[str]
    CloudwatchAlarm: Optional[Sequence["_CloudwatchAlarm"]]
    CloudwatchMetric: Optional[Sequence["_CloudwatchMetric"]]
    Dynamodb: Optional[Sequence["_Dynamodb"]]
    Elasticsearch: Optional[Sequence["_Elasticsearch"]]
    Firehose: Optional[Sequence["_Firehose"]]
    Kinesis: Optional[Sequence["_Kinesis"]]
    Lambda: Optional[Sequence["_Lambda"]]
    Republish: Optional[Sequence["_Republish"]]
    S3: Optional[Sequence["_S3"]]
    Sns: Optional[Sequence["_Sns"]]
    Sqs: Optional[Sequence["_Sqs"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Sql=json_data.get("Sql"),
            SqlVersion=json_data.get("SqlVersion"),
            CloudwatchAlarm=json_data.get("CloudwatchAlarm"),
            CloudwatchMetric=json_data.get("CloudwatchMetric"),
            Dynamodb=json_data.get("Dynamodb"),
            Elasticsearch=json_data.get("Elasticsearch"),
            Firehose=json_data.get("Firehose"),
            Kinesis=json_data.get("Kinesis"),
            Lambda=json_data.get("Lambda"),
            Republish=json_data.get("Republish"),
            S3=json_data.get("S3"),
            Sns=json_data.get("Sns"),
            Sqs=json_data.get("Sqs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CloudwatchAlarm:
    AlarmName: Optional[str]
    RoleArn: Optional[str]
    StateReason: Optional[str]
    StateValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchAlarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchAlarm"]:
        if not json_data:
            return None
        return cls(
            AlarmName=json_data.get("AlarmName"),
            RoleArn=json_data.get("RoleArn"),
            StateReason=json_data.get("StateReason"),
            StateValue=json_data.get("StateValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchAlarm = CloudwatchAlarm


@dataclass
class CloudwatchMetric:
    MetricName: Optional[str]
    MetricNamespace: Optional[str]
    MetricTimestamp: Optional[str]
    MetricUnit: Optional[str]
    MetricValue: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchMetric"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            MetricNamespace=json_data.get("MetricNamespace"),
            MetricTimestamp=json_data.get("MetricTimestamp"),
            MetricUnit=json_data.get("MetricUnit"),
            MetricValue=json_data.get("MetricValue"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchMetric = CloudwatchMetric


@dataclass
class Dynamodb:
    HashKeyField: Optional[str]
    HashKeyType: Optional[str]
    HashKeyValue: Optional[str]
    PayloadField: Optional[str]
    RangeKeyField: Optional[str]
    RangeKeyType: Optional[str]
    RangeKeyValue: Optional[str]
    RoleArn: Optional[str]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dynamodb"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dynamodb"]:
        if not json_data:
            return None
        return cls(
            HashKeyField=json_data.get("HashKeyField"),
            HashKeyType=json_data.get("HashKeyType"),
            HashKeyValue=json_data.get("HashKeyValue"),
            PayloadField=json_data.get("PayloadField"),
            RangeKeyField=json_data.get("RangeKeyField"),
            RangeKeyType=json_data.get("RangeKeyType"),
            RangeKeyValue=json_data.get("RangeKeyValue"),
            RoleArn=json_data.get("RoleArn"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dynamodb = Dynamodb


@dataclass
class Elasticsearch:
    Endpoint: Optional[str]
    Id: Optional[str]
    Index: Optional[str]
    RoleArn: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Elasticsearch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Elasticsearch"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Index=json_data.get("Index"),
            RoleArn=json_data.get("RoleArn"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Elasticsearch = Elasticsearch


@dataclass
class Firehose:
    DeliveryStreamName: Optional[str]
    RoleArn: Optional[str]
    Separator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Firehose"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Firehose"]:
        if not json_data:
            return None
        return cls(
            DeliveryStreamName=json_data.get("DeliveryStreamName"),
            RoleArn=json_data.get("RoleArn"),
            Separator=json_data.get("Separator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Firehose = Firehose


@dataclass
class Kinesis:
    PartitionKey: Optional[str]
    RoleArn: Optional[str]
    StreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Kinesis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Kinesis"]:
        if not json_data:
            return None
        return cls(
            PartitionKey=json_data.get("PartitionKey"),
            RoleArn=json_data.get("RoleArn"),
            StreamName=json_data.get("StreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Kinesis = Kinesis


@dataclass
class Lambda:
    FunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Lambda"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lambda"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lambda = Lambda


@dataclass
class Republish:
    RoleArn: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Republish"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Republish"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Republish = Republish


@dataclass
class S3:
    BucketName: Optional[str]
    Key: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Key=json_data.get("Key"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


@dataclass
class Sns:
    MessageFormat: Optional[str]
    RoleArn: Optional[str]
    TargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sns"]:
        if not json_data:
            return None
        return cls(
            MessageFormat=json_data.get("MessageFormat"),
            RoleArn=json_data.get("RoleArn"),
            TargetArn=json_data.get("TargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sns = Sns


@dataclass
class Sqs:
    QueueUrl: Optional[str]
    RoleArn: Optional[str]
    UseBase64: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Sqs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sqs"]:
        if not json_data:
            return None
        return cls(
            QueueUrl=json_data.get("QueueUrl"),
            RoleArn=json_data.get("RoleArn"),
            UseBase64=json_data.get("UseBase64"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sqs = Sqs


