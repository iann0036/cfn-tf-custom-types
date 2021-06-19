# TF::Exoscale::Ipaddress

Provides an Exoscale [Elastic IP address][eip-doc] resource. This can be used to create, update and delete Elastic IPs.

See [`exoscale_secondary_ipaddress`][r-secondary_ipaddress] for usage with Compute instances.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Exoscale::Ipaddress",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#healthcheckinterval" title="HealthcheckInterval">HealthcheckInterval</a>" : <i>Double</i>,
        "<a href="#healthcheckmode" title="HealthcheckMode">HealthcheckMode</a>" : <i>String</i>,
        "<a href="#healthcheckpath" title="HealthcheckPath">HealthcheckPath</a>" : <i>String</i>,
        "<a href="#healthcheckport" title="HealthcheckPort">HealthcheckPort</a>" : <i>Double</i>,
        "<a href="#healthcheckstrikesfail" title="HealthcheckStrikesFail">HealthcheckStrikesFail</a>" : <i>Double</i>,
        "<a href="#healthcheckstrikesok" title="HealthcheckStrikesOk">HealthcheckStrikesOk</a>" : <i>Double</i>,
        "<a href="#healthchecktimeout" title="HealthcheckTimeout">HealthcheckTimeout</a>" : <i>Double</i>,
        "<a href="#healthchecktlsskipverify" title="HealthcheckTlsSkipVerify">HealthcheckTlsSkipVerify</a>" : <i>Boolean</i>,
        "<a href="#healthchecktlssni" title="HealthcheckTlsSni">HealthcheckTlsSni</a>" : <i>String</i>,
        "<a href="#reversedns" title="ReverseDns">ReverseDns</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Exoscale::Ipaddress
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#healthcheckinterval" title="HealthcheckInterval">HealthcheckInterval</a>: <i>Double</i>
    <a href="#healthcheckmode" title="HealthcheckMode">HealthcheckMode</a>: <i>String</i>
    <a href="#healthcheckpath" title="HealthcheckPath">HealthcheckPath</a>: <i>String</i>
    <a href="#healthcheckport" title="HealthcheckPort">HealthcheckPort</a>: <i>Double</i>
    <a href="#healthcheckstrikesfail" title="HealthcheckStrikesFail">HealthcheckStrikesFail</a>: <i>Double</i>
    <a href="#healthcheckstrikesok" title="HealthcheckStrikesOk">HealthcheckStrikesOk</a>: <i>Double</i>
    <a href="#healthchecktimeout" title="HealthcheckTimeout">HealthcheckTimeout</a>: <i>Double</i>
    <a href="#healthchecktlsskipverify" title="HealthcheckTlsSkipVerify">HealthcheckTlsSkipVerify</a>: <i>Boolean</i>
    <a href="#healthchecktlssni" title="HealthcheckTlsSni">HealthcheckTlsSni</a>: <i>String</i>
    <a href="#reversedns" title="ReverseDns">ReverseDns</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckStrikesFail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckStrikesOk

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckTlsSkipVerify

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckTlsSni

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseDns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

