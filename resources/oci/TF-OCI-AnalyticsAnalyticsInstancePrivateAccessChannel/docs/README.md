# TF::OCI::AnalyticsAnalyticsInstancePrivateAccessChannel

This resource provides the Analytics Instance Private Access Channel resource in Oracle Cloud Infrastructure Analytics service.

Create a Private access Channel for the Analytics instance. The operation is long-running
and creates a new WorkRequest.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::AnalyticsAnalyticsInstancePrivateAccessChannel",
    "Properties" : {
        "<a href="#analyticsinstanceid" title="AnalyticsInstanceId">AnalyticsInstanceId</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#vcnid" title="VcnId">VcnId</a>" : <i>String</i>,
        "<a href="#privatesourcednszones" title="PrivateSourceDnsZones">PrivateSourceDnsZones</a>" : <i>[ <a href="privatesourcednszonesdefinition.md">PrivateSourceDnsZonesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::AnalyticsAnalyticsInstancePrivateAccessChannel
Properties:
    <a href="#analyticsinstanceid" title="AnalyticsInstanceId">AnalyticsInstanceId</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#vcnid" title="VcnId">VcnId</a>: <i>String</i>
    <a href="#privatesourcednszones" title="PrivateSourceDnsZones">PrivateSourceDnsZones</a>: <i>
      - <a href="privatesourcednszonesdefinition.md">PrivateSourceDnsZonesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AnalyticsInstanceId

The OCID of the AnalyticsInstance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) Display Name of the Private Access Channel.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

(Updatable) OCID of the customer subnet connected to private access channel.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcnId

(Updatable) OCID of the customer VCN peered with private access channel.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateSourceDnsZones

_Required_: No

_Type_: List of <a href="privatesourcednszonesdefinition.md">PrivateSourceDnsZonesDefinition</a>

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

#### EgressSourceIpAddresses

Returns the <code>EgressSourceIpAddresses</code> value.

#### Id

Returns the <code>Id</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### Key

Returns the <code>Key</code> value.

