# TF::Akamai::DnsZone

Use the `akamai_dns_zone` resource to configure a DNS zone that integrates with your existing DNS infrastructure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::DnsZone",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#contract" title="Contract">Contract</a>" : <i>String</i>,
        "<a href="#endcustomerid" title="EndCustomerId">EndCustomerId</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#masters" title="Masters">Masters</a>" : <i>[ String, ... ]</i>,
        "<a href="#signandserve" title="SignAndServe">SignAndServe</a>" : <i>Boolean</i>,
        "<a href="#signandservealgorithm" title="SignAndServeAlgorithm">SignAndServeAlgorithm</a>" : <i>String</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#tsigkey" title="TsigKey">TsigKey</a>" : <i>[ <a href="tsigkeydefinition.md">TsigKeyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::DnsZone
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#contract" title="Contract">Contract</a>: <i>String</i>
    <a href="#endcustomerid" title="EndCustomerId">EndCustomerId</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#masters" title="Masters">Masters</a>: <i>
      - String</i>
    <a href="#signandserve" title="SignAndServe">SignAndServe</a>: <i>Boolean</i>
    <a href="#signandservealgorithm" title="SignAndServeAlgorithm">SignAndServeAlgorithm</a>: <i>String</i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#tsigkey" title="TsigKey">TsigKey</a>: <i>
      - <a href="tsigkeydefinition.md">TsigKeyDefinition</a></i>
</pre>

## Properties

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contract

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndCustomerId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Masters

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignAndServe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignAndServeAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TsigKey

_Required_: No

_Type_: List of <a href="tsigkeydefinition.md">TsigKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActivationState

Returns the <code>ActivationState</code> value.

#### AliasCount

Returns the <code>AliasCount</code> value.

#### Id

Returns the <code>Id</code> value.

#### VersionId

Returns the <code>VersionId</code> value.

