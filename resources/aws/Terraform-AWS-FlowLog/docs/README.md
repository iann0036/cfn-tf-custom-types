# Terraform::AWS::FlowLog

Provides a VPC/Subnet/ENI Flow Log to capture IP traffic for a specific network
interface, subnet, or VPC. Logs are sent to a CloudWatch Log Group or a S3 Bucket.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::FlowLog",
    "Properties" : {
        "<a href="#eniid" title="EniId">EniId</a>" : <i>String</i>,
        "<a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>" : <i>String</i>,
        "<a href="#logdestination" title="LogDestination">LogDestination</a>" : <i>String</i>,
        "<a href="#logdestinationtype" title="LogDestinationType">LogDestinationType</a>" : <i>String</i>,
        "<a href="#logformat" title="LogFormat">LogFormat</a>" : <i>String</i>,
        "<a href="#loggroupname" title="LogGroupName">LogGroupName</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#traffictype" title="TrafficType">TrafficType</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::FlowLog
Properties:
    <a href="#eniid" title="EniId">EniId</a>: <i>String</i>
    <a href="#iamrolearn" title="IamRoleArn">IamRoleArn</a>: <i>String</i>
    <a href="#logdestination" title="LogDestination">LogDestination</a>: <i>String</i>
    <a href="#logdestinationtype" title="LogDestinationType">LogDestinationType</a>: <i>String</i>
    <a href="#logformat" title="LogFormat">LogFormat</a>: <i>String</i>
    <a href="#loggroupname" title="LogGroupName">LogGroupName</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#traffictype" title="TrafficType">TrafficType</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### EniId

Elastic Network Interface ID to attach to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRoleArn

The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDestination

The ARN of the logging destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDestinationType

The type of the logging destination. Valid values: `cloud-watch-logs`, `s3`. Default: `cloud-watch-logs`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogFormat

The fields to include in the flow log record, in the order in which they should appear.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogGroupName

*Deprecated:* Use `log_destination` instead. The name of the CloudWatch log group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Subnet ID to attach to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficType

The type of traffic to capture. Valid values: `ACCEPT`,`REJECT`, `ALL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC ID to attach to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

