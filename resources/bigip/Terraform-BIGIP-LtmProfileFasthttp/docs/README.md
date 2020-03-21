# Terraform::BIGIP::LtmProfileFasthttp

CloudFormation equivalent of bigip_ltm_profile_fasthttp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileFasthttp",
    "Properties" : {
        "<a href="#connpoolmaxreuse" title="ConnpoolMaxreuse">ConnpoolMaxreuse</a>" : <i>Double</i>,
        "<a href="#connpoolmaxsize" title="ConnpoolMaxsize">ConnpoolMaxsize</a>" : <i>Double</i>,
        "<a href="#connpoolminsize" title="ConnpoolMinsize">ConnpoolMinsize</a>" : <i>Double</i>,
        "<a href="#connpoolreplenish" title="ConnpoolReplenish">ConnpoolReplenish</a>" : <i>String</i>,
        "<a href="#connpoolstep" title="ConnpoolStep">ConnpoolStep</a>" : <i>Double</i>,
        "<a href="#connpoolidletimeoutoverride" title="ConnpoolidleTimeoutoverride">ConnpoolidleTimeoutoverride</a>" : <i>Double</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#forcehttp10response" title="Forcehttp10response">Forcehttp10response</a>" : <i>String</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#maxheadersize" title="MaxheaderSize">MaxheaderSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileFasthttp
Properties:
    <a href="#connpoolmaxreuse" title="ConnpoolMaxreuse">ConnpoolMaxreuse</a>: <i>Double</i>
    <a href="#connpoolmaxsize" title="ConnpoolMaxsize">ConnpoolMaxsize</a>: <i>Double</i>
    <a href="#connpoolminsize" title="ConnpoolMinsize">ConnpoolMinsize</a>: <i>Double</i>
    <a href="#connpoolreplenish" title="ConnpoolReplenish">ConnpoolReplenish</a>: <i>String</i>
    <a href="#connpoolstep" title="ConnpoolStep">ConnpoolStep</a>: <i>Double</i>
    <a href="#connpoolidletimeoutoverride" title="ConnpoolidleTimeoutoverride">ConnpoolidleTimeoutoverride</a>: <i>Double</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#forcehttp10response" title="Forcehttp10response">Forcehttp10response</a>: <i>String</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#maxheadersize" title="MaxheaderSize">MaxheaderSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ConnpoolMaxreuse

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolMaxsize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolMinsize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolReplenish

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolStep

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolidleTimeoutoverride

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forcehttp10response

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxheaderSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

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

