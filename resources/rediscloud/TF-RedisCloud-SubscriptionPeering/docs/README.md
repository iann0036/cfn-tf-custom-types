# TF::RedisCloud::SubscriptionPeering

Creates an AWS or GCP VPC peering for an existing Redis Enterprise Cloud Subscription, allowing access to your subscription databases as if they were on the same network.

For AWS, peering should be accepted by the other side.
For GCP, the opposite peering request should be submitted.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::RedisCloud::SubscriptionPeering",
    "Properties" : {
        "<a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>" : <i>String</i>,
        "<a href="#gcpnetworkname" title="GcpNetworkName">GcpNetworkName</a>" : <i>String</i>,
        "<a href="#gcpprojectid" title="GcpProjectId">GcpProjectId</a>" : <i>String</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
        "<a href="#vpccidr" title="VpcCidr">VpcCidr</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::RedisCloud::SubscriptionPeering
Properties:
    <a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>: <i>String</i>
    <a href="#gcpnetworkname" title="GcpNetworkName">GcpNetworkName</a>: <i>String</i>
    <a href="#gcpprojectid" title="GcpProjectId">GcpProjectId</a>: <i>String</i>
    <a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
    <a href="#vpccidr" title="VpcCidr">VpcCidr</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AwsAccountId

AWS account ID that the VPC to be peered lives in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpNetworkName

The name of the network to be peered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpProjectId

GCP project ID that the VPC to be peered lives in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

The cloud provider to use with the vpc peering, (either `AWS` or `GCP`). Default: ‘AWS’.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

AWS Region that the VPC to be peered lives in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

A valid subscription predefined in the current account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcCidr

CIDR range of the VPC to be peered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Identifier of the VPC to be peered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AwsPeeringId

Returns the <code>AwsPeeringId</code> value.

#### GcpPeeringId

Returns the <code>GcpPeeringId</code> value.

#### GcpRedisNetworkName

Returns the <code>GcpRedisNetworkName</code> value.

#### GcpRedisProjectId

Returns the <code>GcpRedisProjectId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

