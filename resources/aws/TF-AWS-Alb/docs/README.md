# TF::AWS::Alb

CloudFormation equivalent of aws_alb

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Alb",
    "Properties" : {
        "<a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>" : <i>String</i>,
        "<a href="#dropinvalidheaderfields" title="DropInvalidHeaderFields">DropInvalidHeaderFields</a>" : <i>Boolean</i>,
        "<a href="#enablecrosszoneloadbalancing" title="EnableCrossZoneLoadBalancing">EnableCrossZoneLoadBalancing</a>" : <i>Boolean</i>,
        "<a href="#enabledeletionprotection" title="EnableDeletionProtection">EnableDeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>Boolean</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#internal" title="Internal">Internal</a>" : <i>Boolean</i>,
        "<a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>" : <i>String</i>,
        "<a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#accesslogs" title="AccessLogs">AccessLogs</a>" : <i>[ <a href="accesslogsdefinition.md">AccessLogsDefinition</a>, ... ]</i>,
        "<a href="#subnetmapping" title="SubnetMapping">SubnetMapping</a>" : <i>[ <a href="subnetmappingdefinition.md">SubnetMappingDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Alb
Properties:
    <a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>: <i>String</i>
    <a href="#dropinvalidheaderfields" title="DropInvalidHeaderFields">DropInvalidHeaderFields</a>: <i>Boolean</i>
    <a href="#enablecrosszoneloadbalancing" title="EnableCrossZoneLoadBalancing">EnableCrossZoneLoadBalancing</a>: <i>Boolean</i>
    <a href="#enabledeletionprotection" title="EnableDeletionProtection">EnableDeletionProtection</a>: <i>Boolean</i>
    <a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>Boolean</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#internal" title="Internal">Internal</a>: <i>Boolean</i>
    <a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>: <i>String</i>
    <a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#accesslogs" title="AccessLogs">AccessLogs</a>: <i>
      - <a href="accesslogsdefinition.md">AccessLogsDefinition</a></i>
    <a href="#subnetmapping" title="SubnetMapping">SubnetMapping</a>: <i>
      - <a href="subnetmappingdefinition.md">SubnetMappingDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CustomerOwnedIpv4Pool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropInvalidHeaderFields

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCrossZoneLoadBalancing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDeletionProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttp2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLogs

_Required_: No

_Type_: List of <a href="accesslogsdefinition.md">AccessLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetMapping

_Required_: No

_Type_: List of <a href="subnetmappingdefinition.md">SubnetMappingDefinition</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### ArnSuffix

Returns the <code>ArnSuffix</code> value.

#### DnsName

Returns the <code>DnsName</code> value.

#### Id

Returns the <code>Id</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

#### ZoneId

Returns the <code>ZoneId</code> value.

